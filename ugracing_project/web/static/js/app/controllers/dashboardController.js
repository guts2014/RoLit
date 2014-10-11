'use strict';

angular.module('ugracing').controller('dashboardController', ['$scope', 'UpdateData', 'DataStructures', function ($scope, UpdateData, DataStructures) {

	// Initialize
	$scope.labels = DataStructures.dataLabels();
	$scope.data = DataStructures.allData();

}]);