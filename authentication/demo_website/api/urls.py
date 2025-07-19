from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('register/', views.registerView, name = 'register'),
    path('home/', views.homeView, name = 'home'),
    
    
    # path('adminreg/', views.admin_regView),
    # path('adminlogin/' , views.admin_logView),
    # path('adminhome/', views.adminHomeView)  
    
]





teh = []