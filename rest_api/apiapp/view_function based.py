from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import BookCollection
from .serializers import BookSerializer
from rest_framework.decorators import api_view
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def book_list(request):
    if request.method == 'GET':
        books=BookCollection.objects.all()
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def book_detail(request,pk):
    try:
        book=BookCollection.objects.get(pk=pk)

    except BookCollection.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        serializer = BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method =='DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
@csrf_exempt
def book_list(request):
    if request.method == 'GET':
        books=BookCollection.objects.all()
        serializer=BookSerializer(books,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        data=JSONParser().parse(request)
        serializer=BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
'''

'''
@csrf_exempt
def book_detail(request,pk):
    try:
        book=BookCollection.objects.get(pk=pk)
    except BookCollection.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BookSerializer(book,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)

    elif request.method =='DELETE':
        book.delete()
        return HttpResponse(status=204)'''
