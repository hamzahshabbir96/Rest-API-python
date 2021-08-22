from rest_framework import serializers
from .models import BookCollection


#model serializer

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookCollection
        #fields=['id','title','author','language','genre','date']
        fields='__all__'

'''class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    language = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return BookCollection.objects.create(validated_data)


    def update(self, instance, validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.language = validated_data.get('language', instance.language)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance
'''