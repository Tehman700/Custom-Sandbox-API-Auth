from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginView, name='logins'),
    path('registers/', views.registerView, name = 'register'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('logout/' ,  views.logout_view, name = 'logout'),

    path('admin_panel/', views.admin_panel, name='admin_panel' ),

    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
]


