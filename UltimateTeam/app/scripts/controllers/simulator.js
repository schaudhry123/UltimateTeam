'use strict';

angular.module('frontendApp')

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/simulator', {
    templateUrl: 'views/simulator.html',
    controller: 'SimCtrl'
  });
}])

.controller('SimCtrl', ['$scope', '$http',
	function($scope, $http) {
		$http.get('http://ultimate-team-rest-api.herokuapp.com/teams/').success(function(data) {
			$scope.teams = data['results'];
		});
	}])