'use strict';

angular.module('ultimateTeam.home', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/home', {
    templateUrl: 'home/home.html',
    controller: 'HomeCtrl'
  });
}])

.controller('HomeCtrl', ['$scope', '$http',
	function($scope, $http) {
		$http.get('http://ultimate-team-rest-api.herokuapp.com/players/').success(function(data) {
			$scope.players = data['results'];
		});

	}]);