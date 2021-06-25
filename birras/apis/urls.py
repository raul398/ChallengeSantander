from django.urls import path
from . import views

urlpatterns = [
	#descriptions
	path('', views.apiOverview, name='api-overview'),
	#Rutas para meeting
	path('meeting-list/', views.MeetingList, name='meeting-list'),
	path('meeting-detail/<str:id>/', views.MeetingDetail, name='meeting-detail'),
	path('meeting-create/', views.MeetingCreate, name='meeting-create'),
	path('meeting-update/<str:id>/', views.MeetingUpdate, name='meeting-update'),
	path('meeting-delete/<str:id>/', views.MeetingDelete, name='meeting-delete'),
	#Rutas para user
	path('user-list/', views.UserList, name='user-list'),
	path('user-detail/<str:id>/', views.UserDetail, name='user-detail'),
	path('user-create/', views.UserCreate, name='user-create'),
	path('user-update/<str:id>/', views.UserUpdate, name='user-update'),
	path('user-delete/<str:id>/', views.UserDelete, name='user-delete'),
]