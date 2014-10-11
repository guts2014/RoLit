'use strict';

angular.module('ugracing').controller('dashboardController', ['$scope', 'UpdateData', 'DataLabels', function ($scope, UpdateData, DataLabels) {

	// Get initial data
	var data = UpdateData.all();

	console.log(DataLabels.o2);

}]);