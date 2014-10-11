'use strict';

angular.module('ugracing').controller('dashboardController', ['$scope', '$interval', 'UpdateData', 'DataStructures', function ($scope, $interval, UpdateData, DataStructures) {

	// Initialize
	$scope.labels = DataStructures.dataLabels();
	$scope.data = DataStructures.allData();

	// Keep updating the data forever forever forever forever forever...
	$interval(function() {
		console.log($scope.data);
		$scope.data = UpdateData.all();

	}, 5000);

	// Set up charts
	var chart1 = $('#chart-1');
	var chart2 = $('#chart-2');


	var data = [],
	totalPoints = 300;
	function getRandomData() {
		if (data.length > 0) data = data.slice(1);
		// Do a random walk
		while (data.length < totalPoints) {
			var prev = data.length > 0 ? data[data.length - 1] : 50, y = prev + Math.random() * 10 - 5;
			if (y < 0) {
				y = 0;
			} else if (y > 100) {
				y = 100;
			}
			data.push(y);
		}
		// Zip the generated y values with the x values
		var res = [];
		for (var i = 0; i < data.length; ++i) {
			res.push([i, data[i]])
		}
		return res;
	}

	var plot = function(target) {
		$.plot(target, [ getRandomData() ], {
			series: {
				shadowSize: 0	// Drawing is faster without shadows
			},
			yaxis: {
				min: 0,
				max: 100
			},
			xaxis: {
				show: false
			}
		});
	};

	plot(chart1);
	plot(chart2);

}]);