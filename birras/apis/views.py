from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

#imortar los serializadores
from .serializers import MeetingSerializer
from .serializers import UserSerializer

#importar los modelos a utilizar
from meeting.models import Meeting 
from user.models import User 

# Create your views here.


#muestra el listado de router
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		#Rutas para meeting
		'ListMeeting' : '/meeting-list/',
		'Detail-view-meeting' : '/meeting-detail/<str:id>/',
		'CreateMeeting' : '/meeting-create/',
		'UpdateMeeting' : '/meeting-update/<str:id>/',
		'DeleteMeeting' : '/meeting-delete/<str:id>/',
		#Rutas para user
		'ListUser' : '/user-list/',
		'Detail-view-user' : '/user-detail/<str:id>/',
		'CreateUser' : '/user-create/',
		'UpdateUser' : '/user-update/<str:id>/',
		'DeleteUser' : '/user-delete/<str:id>/',
	}
	return Response(api_urls)


'''
	Aqui comienzan las vistas para lo que refiere a meeting
'''

#listado de objetos meeting
@api_view(['GET'])
def MeetingList(request):
	meetings = Meeting.objects.all()
	serializer = MeetingSerializer(meetings, many=True)
	return Response(serializer.data)

#objetos meeting especifico
@api_view(['GET'])
def MeetingDetail(request, id):
	meetings = Meeting.objects.get(id=id)
	serializer = MeetingSerializer(meetings, many=False)
	return Response(serializer.data)

#crea objetos meeting
@api_view(['POST'])
def MeetingCreate(request):
	serializer = MeetingSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

#actualiza objetos meeting
@api_view(['POST'])
def MeetingUpdate(request, id):
	meeting = Meeting.objects.get(id=id)
	serializer = MeetingSerializer(instance=meeting, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

#eliminar objetos meeting
@api_view(['DELETE'])
def MeetingDelete(request, id):
	meeting = Meeting.objects.get(id=id)
	meeting.delete()

	return Response('Item succsesfully delete!')

'''
	Aqui terminan las vistas para lo que refiere a meeting
'''



'''
	Aqui comienzan las vistas para lo que refiere a user
'''

#listado de objetos user
@api_view(['GET'])
def UserList(request):
	users = User.objects.all()
	serializer = UserSerializer(users, many=True)
	return Response(serializer.data)

#objetos user especifico
@api_view(['GET'])
def UserDetail(request, id):
	users = User.objects.get(id=id)
	serializer = UserSerializer(users, many=False)
	return Response(serializer.data)

#crea objetos user
@api_view(['POST'])
def UserCreate(request):
	serializer = UserSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

#actualiza objetos user
@api_view(['POST'])
def UserUpdate(request, id):
	user = User.objects.get(id=id)
	serializer = UserSerializer(instance=user, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

#eliminar objetos user
@api_view(['DELETE'])
def UserDelete(request, id):
	user = User.objects.get(id=id)
	user.delete()

	return Response('Item succsesfully delete!')

'''
	Aqui terminan las vistas para lo que refiere a user
'''