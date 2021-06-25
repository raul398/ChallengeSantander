from rest_framework import serializers
from meeting.models import Meeting #importar el modelo de meeting
from user.models import User #importar el modelo de user


class MeetingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Meeting #Este es el modelo que se va aserializar
		fields = '__all__' #Los campos que se van a serializar


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User #Este es el modelo que se va aserializar
		fields = '__all__' #Los campos que se van a serializar