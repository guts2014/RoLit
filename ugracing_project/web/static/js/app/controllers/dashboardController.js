'use strict';

angular.module('ugracing').controller('dashboardController', ['$scope', '$http', '$interval', 'UpdateData', 'DataStructures', function ($scope, $http, $interval, UpdateData, DataStructures) {

	// Initialize
	$scope.labels = DataStructures.dataLabels();
	$scope.data = DataStructures.allData();
	var chartableDataset = DataStructures.allDataChartable();
	$scope.chartableDatasetArray = [];
	var count = 0;

	// Set up charts
	var chart1 = $('#chart-1');

	// Function that updates chartable data
	var constructChartableDataset = function(data) {
		if (angular.isUndefined(data)) {
			return;
		}		
		angular.forEach(data, function(value, key) {
			if ($scope.labels.hasOwnProperty(key)) {
				if (value == null && chartableDataset[key].data.length) {
					value = chartableDataset[key].data[chartableDataset[key].data.length - 1][1];
				}
				chartableDataset[key].data.push([count, parseInt(value)]);				
				count++;
				if (chartableDataset[key].data.length > 200) {
					chartableDataset[key].data.splice(0, 1);
				}
			}

		});
	};
	var constructChartableDatasetArray = function() {
		var newArray = [];
		var colour = 0;
		angular.forEach(chartableDataset, function(value, key) {
			value.color = colour;
			colour++;
			newArray.push(value);
		});
		$scope.chartableDatasetArray = newArray;
	};

	// Keep updating the data forever
	$interval(function() {
		//'telemetry-api/get-latest-values/'
	    $http.get('http://192.168.173.1:8000/telemetry-api/get-latest-values/')
	    		.success(function(data, status, headers, config) {
	   	  			$scope.data = data;
	   	  			constructChartableDataset($scope.data);
	   	  			constructChartableDatasetArray();
	    		})
	    		.error(function(data, status, headers, config) {
	      			console.log('Error: could not connect to API endpoint.');
	    		});
	}, 100);

		// Set up the control widget

		var updateInterval = 30;

		var plot = $.plot("#chart-1", [ getRandomData() ], {
			series: {
				shadowSize: 0	// Drawing is faster without shadows
			},
			yaxis: {
				min: 0
			},
			xaxis: {
				show: false
			},
			legend: {
				show: false
			}
		});

		function update() {
			if ($scope.chartableDatasetArray.length) {
				plot.setData($scope.chartableDatasetArray);
				plot.setupGrid();
				plot.draw();
				
			}
			setTimeout(update, updateInterval);
		}

		update();



}]);