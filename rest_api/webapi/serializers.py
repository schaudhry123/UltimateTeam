from rest_framework import serializers
from webapi.models import Player, Team
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	players = serializers.PrimaryKeyRelatedField(many=True, queryset=Player.objects.all())
	teams = serializers.PrimaryKeyRelatedField(many=True, queryset=Team.objects.all())

	class Meta:
		model = User
		fields = {'id', 'username', 'players', 'teams'}

class PlayerSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Player
		fields = ('id', 'owner', 'player_name', 'position', 'nationality', 'player_league')

class TeamSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Team
		fields = ('id', 'owner', 'team_name', 'manager', 'league', 'location', 'team_titles')