from django.db import models

# Create your models here.
class Team(models.Model):
	team_name = models.CharField(max_length=100, null=True)
	manager = models.CharField(max_length=100, null=True)
	league = models.CharField(max_length=100, null=True)
	location = models.CharField(max_length=100, null=True)
	team_titles = models.IntegerField(default=0, null=True)

	# For printing string
	def __str__(self):
		return self.team_name

	# Has won any titles
	def has_won_titles(self):
		return self.team_titles > 0

class Player(models.Model):
	player_name = models.CharField(max_length=100, null=True)
	position = models.CharField(max_length=3, null=True)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
	nationality = models.CharField(max_length=100, null=True)
	player_league = models.CharField(max_length=100, null=True)
	height = models.CharField(max_length=5, null=True)
	weight = models.CharField(max_length=10, null=True)
	age = models.IntegerField(null=True)
	appearances = models.IntegerField(null=True)
	goals = models.IntegerField(null=True)
	assists = models.IntegerField(null=True)
	fouls_per_game = models.FloatField(null=True)
	yellow_cards = models.IntegerField(null=True)
	red_cards = models.IntegerField(null=True)

	def __str__(self):
		return self.player_name

class Attacker(Player):
	key_passes_per_game = models.FloatField(null=True)
	shots_per_game = models.FloatField(null=True)
	dripples_per_game = models.FloatField(null=True)

class Midfielder(Player):
	tackles = models.IntegerField(null=True);
	key_passes_per_game = models.FloatField(null=True)
	shots_per_game = models.FloatField(null=True)
	dripples_per_game = models.FloatField(null=True)

class Defender(Player):
	tackles = models.IntegerField(null=True)
	clearances = models.FloatField(null=True)
	interceptions_per_game = models.FloatField(null=True)