from rest_framework import serializers
from webapi.models import Player, Team
from django.contrib.auth.models import User

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Player
		fields = ('url', 'owner', 'player_name', 'position', 'team', 'nationality', 'player_league')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Team
		fields = ('url', 'owner', 'team_name', 'manager', 'league', 'location', 'team_titles')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	players = serializers.HyperlinkedRelatedField(many=True, view_name='player-detail', read_only=True)
	teams = serializers.HyperlinkedRelatedField(many=True, view_name='team-detail', read_only=True)

	class Meta:
		model = User
		fields = ('url', 'username', 'players', 'teams')