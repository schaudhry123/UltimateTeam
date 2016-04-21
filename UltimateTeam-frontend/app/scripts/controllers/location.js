'use strict';

angular.module('frontendApp')

.controller(':LocationCtrl', function($http, $rootScope, $scope) {
  $scope.user = $rootScope.user;

  $scope.updateUser = function() {
    $rootScope.user = $scope.user;
    $rootScope.goToState('location');
  };
});
  