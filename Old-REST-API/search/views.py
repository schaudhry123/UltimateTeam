from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Player, Team

""" Home View """
class IndexView(generic.ListView):
	template_name = 'search/index.html'
	# context_object_name = 'home_list'
	context_object_name = 'latest_player_list'

	def get_queryset(self):
		"""Return all players"""
		return Player.objects.all()

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		# context['player'] = Player.objects.all()
		context.update({
			'latest_team_list': Team.objects.all()
		})
		return context


""" List all players """
class PlayersView(generic.ListView):
	template_name = 'search/players.html'
	context_object_name = 'latest_player_list'

	def get_queryset(self):
		return Player.objects.all()

""" List all teams """
class TeamsView(generic.ListView):
	template_name = 'search/teams.html'
	context_object_name = 'latest_team_list'

	def get_queryset(self):
		return Team.objects.all()



"""" Show a single player """
class PlayerView(generic.DetailView):
	model = Player
	template_name = 'search/player.html'

""" Show a single team """
class TeamView(generic.DetailView):
	model = Team
	template_name = 'search/team.html'
