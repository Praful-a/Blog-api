from django.urls import path, include

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('login/', views.login_view, name='login'),
    path('account/', views.account_view, name='account'),
    path('must_authenticate', views.must_authenticate_view, name='must_authenticated')
]
