from django.urls import include, path

urlpatterns = [
    path('users/', include('users.urls')),
    path('topic/', include('topic.urls')),
    path('auth/', include('rest_auth.urls')),
]
