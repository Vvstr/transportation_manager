from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Новый маршрут по умолчанию
    path('greenhouse/<int:pk>/', views.greenhouse_detail, name='greenhouse_detail'),
    path('crop/<int:pk>/', views.crop_detail, name='crop_detail'),
    path('greenhouse/create/', views.create_greenhouse, name='create_greenhouse'),
    path('greenhouse/<int:greenhouse_pk>/crop/create/', views.create_crop, name='create_crop'),
    path('crop/<int:crop_pk>/sowing/create/', views.create_sowing_schedule, name='create_sowing_schedule'),
    path('crop/<int:crop_pk>/irrigation/create/', views.create_irrigation_schedule, name='create_irrigation_schedule'),
    path('crop/<int:crop_pk>/fertilization/create/', views.create_fertilization_schedule,
         name='create_fertilization_schedule'),
    path('crop/<int:crop_pk>/harvest/create/', views.create_harvest_schedule, name='create_harvest_schedule'),
    path('agronomists/', views.agronomists, name='agronomists'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('index/', views.index, name='index'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
