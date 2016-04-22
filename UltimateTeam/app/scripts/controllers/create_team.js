'use strict';

var app = angular.module('frontendApp')

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/createteam', {
    templateUrl: 'views/create_team.html',
    controller: 'CreateTeamCtrl'
  });
}])

.controller('CreateTeamCtrl', ['$scope', '$http', '$rootScope',
	function($scope, $http, $rootScope, $element) {
		// $scope.selectedPlayers = [];

		$http.get($rootScope.serverHost + 'players/').success(function(data) {
			$scope.players = data['results'];
		});

		$scope.searchTerm;

		$scope.clearSearchTerm = function() {
			$scope.searchTerm = '';
		};

		$scope.createTeam = function() {
			$scope.team.owner = $rootScope.user;
			console.log("Posting " + JSON.stringify($scope.team));
			$http.post($rootScope.serverHost + 'teams/', $scope.team)
				.then(function() {
					$rootScope.showSimpleToast('Team created!');
					$rootScope.goToState('teams');
				});
		};

	}]);
