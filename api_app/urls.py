from django.urls import path
from . import views 

urlpatterns= [
    # path('studentapi/', views.StudentList.as_view()),
    # path('studentapi/', views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>/',views.StudentRetrieve.as_view()),
    # path('studentapi/<int:pk>/',views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>/',views.StudentDestroy.as_view()),
    
    # To access all the methods togetherly----->
    path('studentapi/', views.LCStudentAPI.as_view()),
    path('studentapi/<int:pk>/',views.RUDStudentAPI.as_view()),
]