'use strict';

angular.module('frontendApp')

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/simulator', {
    templateUrl: 'views/simulator.html',
    controller: 'SimCtrl'
  });
}])

.controller('SimCtrl', ['$scope', '$http', '$rootScope',
	function($scope, $http, $rootScope) {
		$scope.team1;
		$scope.team2;

		$http.get($rootScope.serverHost + 'teams/').success(function(data) {
			$scope.teams = data['results'];
		});

		$scope.searchTerm1;
		$scope.searchTerm2;

		$scope.clearSearchTerm = function() {
			$scope.searchTerm1 = '';
			$scope.searchTerm2 = '';
		};

		$scope.simulate = function(team1, team2) {
			if (!team1 || !team2) {
				$scope.showSimpleToast('Enter both teams!');
				return false;
			}
			$scope.dataLoaded = false;
			$http.get($rootScope.serverHost + 'simulate/' + team1 + '/' + team2).success(function(data) {
				$scope.results = data['results'];
				$scope.dataLoaded = true;
			});
		}
	}])