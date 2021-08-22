
from django.urls import path
from . import views
from .views import BookAPIView,Bookdetails,GenericAPIView
urlpatterns = [
    path('books/',BookAPIView.as_view()),
    path('detail/<int:id>/', Bookdetails.as_view()),
    path('generic/book/<int:id>/',GenericAPIView.as_view()),
    #path('books/', views.book_list),Bookdetails
    #path('detail/<int:pk>/',views.book_detail)

]