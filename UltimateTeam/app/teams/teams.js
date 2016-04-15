'use strict';

angular.module('ultimateTeam.teams', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/teams', {
    templateUrl: 'teams/teams.html',
    controller: 'TeamListCtrl'
  });
}])

.controller('TeamListCtrl', ['$scope', '$http',
	function($scope, $http) {
		$http.get('http://ultimate-team-rest-api.herokuapp.com/teams/').success(function(data) {
			$scope.teams = data['results'];
		});
	}])

.controller('TeamDetailCtrl', ['$scope', '$routeParams', '$http',
	function($scope, $routeParams, $http) {
		$http.get('http://ultimate-team-rest-api.herokuapp.com/teams/' + $routeParams.id + '.json').success(function(data) {
			$scope.team = data;
		});
	}]);