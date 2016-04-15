'use strict';

// Declare app level module which depends on views, and components
angular.module('ultimateTeam', [
  'ngRoute',
  'ultimateTeam.home',
  'ultimateTeam.players',
  'ultimateTeam.teams',
  'ultimateTeam.version'
]).
config(['$routeProvider',
	function($routeProvider) {
		$routeProvider.
			when('/home', {
				templateUrl: 'home/home.html',
				controller: 'HomeCtrl'
			}).
			when('/players', {
				templateUrl: 'players/player-list.html',
				controller: 'PlayerListCtrl'
			}).
			when('/players/:id', {
				templateUrl: 'players/player-detail.html',
				controller: 'PlayerDetailCtrl'
			}).
			when('/teams', {
				templateUrl: 'teams/team-list.html',
				controller: 'TeamListCtrl'
			}).
			when('/teams/:id', {
				templateUrl: 'teams/team-detail.html',
				controller: 'TeamDetailCtrl'
			}).
			otherwise({
				redirectTo: '/home'
			});
  // $routeProvider.otherwise({redirectTo: '/home'});
	}]);