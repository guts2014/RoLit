'use strict';

angular.module('ugracing').directive('dashboardStat', function() {
    return {
        restrict: 'A',
        scope: {
        	colour: "@colour",
        	icon: "@icon"
        },
        templateUrl: 'static/views/directives/dashboard-stat.html'
    };
});