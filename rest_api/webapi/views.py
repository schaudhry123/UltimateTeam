from webapi.models import Player, Team
from webapi.serializers import PlayerSerializer, TeamSerializer, UserSerializer
from webapi.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from django.contrib.auth.models import User

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class PlayerList(generics.ListCreateAPIView):
	queryset = Player.objects.all()
	serializer_class = PlayerSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Player.objects.all()
	serializer_class = PlayerSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class TeamList(generics.ListCreateAPIView):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)