from rest_framework import serializers
from webapi.models import Player, Team

class PlayerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Player
		fields = ('id', 'player_name', 'position', 'nationality', 'player_league')

class TeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Team
		fields = ('id', 'team_name', 'manager', 'league', 'location', 'team_titles')