from django.urls import path
from .views import access_user
# from .views import get_users, create_user, user_detail

urlpatterns=[
    # path('users/',get_users,name='get_users'),
    path('access/',access_user.as_view({'get': 'list'})),
    path('create/',access_user.as_view({'post': 'create'})), 
    path('delete/<int:pk>/', access_user.as_view({'delete': 'destroy'})),
    path('update/<int:pk>/',access_user.as_view({'put':'update'})),
    # path('users/create',create_user,name='crate_users'),
    # path('users/<int:pk>',user_detail,name='user_detail')
]