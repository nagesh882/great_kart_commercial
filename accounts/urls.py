from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('dashbord/', views.dashbord, name="dashbord"),

    path('activate/<uidb64>/<token>/', views.activate, name="activate"),
    
]
