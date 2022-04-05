from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('addbook', views.add_book),
    path('deletebook/<str:pk>', views.delete_book),
    path('updatebook/<str:pk>', views.update_book),
    path('loginuser/', views.loginuser),
    path('logoutuser/', views.logoutuser),
    path('loginuser/register/', views.register),
    path('register/', views.BookList.as_view())
]
