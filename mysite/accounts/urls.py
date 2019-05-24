from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('profile/', views.redirect_user, name='profile'),
    re_path('profile/(?P<pk>\d+)/', views.UserDetail.as_view(), name='user-profile'),
    path('', include('django.contrib.auth.urls')),
    path('signin/', views.SignIn.as_view(), name='signin'),
    re_path('profile_edit/(?P<pk>\d+)/', views.UserEdit.as_view(), name='profile_edit'),
]