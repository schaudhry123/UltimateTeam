from django.conf.urls import url
from . import views

app_name = 'search'
urlpatterns = [
	# /search/
	url(r'^$', views.IndexView.as_view(), name="home_list"),

	# /search/players
	url(r'^players/', views.PlayersView.as_view(), name="players"),
	# /search/teams
	url(r'^teams/$', views.TeamsView.as_view(), name="teams"),

	# /search/players/1
	url(r'^player/(?P<pk>[0-9]+)/$', views.PlayerView.as_view(), name='player'),
	# /search/teams/2
    url(r'^team/(?P<pk>[0-9]+)/$', views.TeamView.as_view(), name='team'),

]