from django.urls import path
from .views import UserViewset, UserAPIView
urlpatterns = [
    path('users/', UserViewset.as_view({
        'get': 'list',
        'post': 'create',

    })),
    path('users/<str:pK>', UserViewset.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('user', UserAPIView.as_view())
]
