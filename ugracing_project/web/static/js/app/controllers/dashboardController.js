'use strict';

angular.module('ugracing').controller('dashboardController', ['$scope', 'UpdateData', function ($scope, UpdateData) {

	$scope.items = [1, 2, 3, 5, 8, 13];

	console.log(UpdateData.all());

}]);