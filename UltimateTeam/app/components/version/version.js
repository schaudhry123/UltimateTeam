'use strict';

angular.module('ultimateTeam.version', [
  'ultimateTeam.version.interpolate-filter',
  'ultimateTeam.version.version-directive'
])

.value('version', '0.1');
