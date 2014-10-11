'use strict';

angular.module('ugracing').controller('dashboardController', ['$scope', 'UpdateData', 'DataLabels', function ($scope, UpdateData, DataLabels) {

	// Initialize
	var data = DataStructures.allData();

	console.log(data);

}]);