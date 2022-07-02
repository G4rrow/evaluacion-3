from django.urls import path, include
from auth_proyecto import views
app_name = "auth"
urlpatterns = [
	path('login/', views.auth_login, name = 'login'),
	path('logout', views.auth_logout, name = 'logout'),
]
