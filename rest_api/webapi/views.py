from webapi.models import Player, Team
from webapi.serializers import PlayerSerializer, TeamSerializer, UserSerializer
from webapi.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	This viewset automatically provides 'list' and 'detail' actions
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer

class PlayerViewSet(viewsets.ModelViewSet):
	"""
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
	queryset = Player.objects.all()
	serializer_class = PlayerSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class TeamViewSet(viewsets.ModelViewSet):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)