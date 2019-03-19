from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from topic import views

urlpatterns = [
    path('getAllPosts/', views.PostList.as_view()),
    path('getPost/<int:pk>/', views.PostDetail.as_view()),

    path('getAllCategory/', views.CategoryList.as_view()),
    path('getCategory/<int:pk>/', views.CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
