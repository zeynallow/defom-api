from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from topic import views

urlpatterns = [
    path('posts/', views.PostView.as_view()),
    path('posts/<int:pk>', views.PostView.as_view()),

    path('categories/', views.CategoryView.as_view()),
    path('category/<int:pk>/', views.CategoryView.as_view()),

    path('replies/', views.ReplyView.as_view()),
    path('replies/<int:pk>/', views.ReplyView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
