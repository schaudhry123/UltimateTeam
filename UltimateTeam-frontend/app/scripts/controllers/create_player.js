'use strict';

angular.module('frontendApp')

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/createplayer', {
    templateUrl: 'views/create_player.html',
    controller: 'CreatePlayerCtrl'
  });
}])

.controller('CreatePlayerCtrl', ['$scope', '$http',
	function($scope, $http) {
		$http.get('http://ultimate-team-rest-api.herokuapp.com/createplayer/').success(function(data) {
			$scope.teams = data['results'];
		});
	}])
