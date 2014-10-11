'use strict';

angular.module('ugracing').controller('dashboardController', ['$scope', 'UpdateData', 'DataLabels', 'DataStructures', function ($scope, UpdateData, DataLabels, DataStructures) {

	// Initialize
	var data = DataStructures.allData();

	console.log(data);

}]);