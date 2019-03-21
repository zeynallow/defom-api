from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from users import views

urlpatterns = [
    path('get/', views.UserView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
