from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from webapi import views

urlpatterns = format_suffix_patterns([
	url(r'^$', views.api_root),
	url(r'^players/$', views.PlayerList.as_view(), name='player-list'),
	url(r'^players/(?P<pk>[0-9]+)/$', views.PlayerDetail.as_view(), name='player-detail'),
	url(r'^teams/$', views.TeamList.as_view(), name='team-list'),
	url(r'^teams/(?P<pk>[0-9]+)/$', views.TeamDetail.as_view(), name='team-detail'),
	url(r'^users/$', views.UserList.as_view(), name='user-list'),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
])

# Login and logout views for the browsable API
urlpatterns += [
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]