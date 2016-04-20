'use strict';

angular.module('frontendApp')

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/players', {
    templateUrl: 'views/player-list.html',
    controller: 'PlayerListCtrl'
  });
}])

.controller('PlayerListCtrl', ['$scope', '$http',
	function($scope, $http) {
		$http.get('http://ultimate-team-rest-api.herokuapp.com/players/').success(function(data) {
			$scope.players = data['results'];
		});
	}])

.controller('PlayerDetailCtrl', ['$scope', '$routeParams', '$http',
	function($scope, $routeParams, $http) {
		$http.get('http://ultimate-team-rest-api.herokuapp.com/players/' + $routeParams.id + '.json').success(function(data) {
			$scope.player = data;
		});
	}])

.controller('NewPlayerCtrl', ['$scope', '$http',
	function($scope, $http) {
		$scope.lol = "Lol";
	}])