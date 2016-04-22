'use strict';

angular.module('frontendApp')

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/players', {
    templateUrl: 'views/player-list.html',
    controller: 'PlayerListCtrl'
  });
}])

.controller('PlayerListCtrl', ['$scope', '$http', '$rootScope',
	function($scope, $http, $rootScope) {
		$http.get($rootScope.serverHost + 'players/').success(function(data) {
			$scope.players = data['results'];
		});

		$scope.createplayer = function() {
			$rootScope.goToState('createplayer');
		}
	}])

.controller('PlayerDetailCtrl', ['$scope', '$routeParams', '$http', '$rootScope',
	function($scope, $routeParams, $http, $rootScope) {
		$http.get($rootScope.serverHost + 'players/' + $routeParams.id + '.json').success(function(data) {
			$scope.player = data;
		});
	}])

.controller('CreatePlayerCtrl', ['$scope', '$http', '$rootScope',
	function($scope, $http, $rootScope) {
		$http.get($rootScope.serverHost + 'teams/').success(function(data) {
			$scope.teams = data['results'];
		});

		$scope.createPlayer = function() {
			$scope.player.owner = $rootScope.user;
			$http.post($rootScope.serverHost + 'players/', $scope.player)
				.then(function() {
					$rootScope.showSimpleToast('Player created!');
					$rootScope.goToState('players');
				});
		};
	}])