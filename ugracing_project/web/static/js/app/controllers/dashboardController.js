'use strict';

angular.module('ugracing').controller('dashboardController', ['$scope', '$http', '$interval', 'DataStructures', function ($scope, $http, $interval, DataStructures) {

	// Initialize
	$scope.labels = DataStructures.dataLabels();
	$scope.data = DataStructures.allData();
	var chartableDataset = DataStructures.allDataChartable();
	$scope.chartableDatasetArray = [];
	var count = 0;

	// Set up the chart
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
			newArray.push(value);
			colour++;
		});
		$scope.chartableDatasetArray = newArray;
	};

	// Add options to the graph
	var choiceContainer = $('#legend');
	constructChartableDatasetArray();
	angular.forEach($scope.chartableDatasetArray, function(value, key) {
		choiceContainer.append("<input type='checkbox' name='" + key +"' checked='checked' id='id" + key + "'></input>" + "<label for='id" + key + "'>&nbsp;" + value.label + "</label><br/>");
	});

	// Keep updating the data forever
	$interval(function() {
		//'telemetry-api/get-latest-values/'
	    $http.get('http://192.168.173.1:8000/telemetry-api/get-latest-values/')
	    		.success(function(data, status, headers, config) {
	   	  			for (var key in data) {
	   	  				if (data[key] != null) {
	   	  					$scope.data[key] = data[key];
	   	  				}
	   	  			}
	   	  			constructChartableDataset($scope.data);
	   	  			constructChartableDatasetArray();
	    		})
	    		.error(function(data, status, headers, config) {
	      			console.log('Error: could not connect to API endpoint.');
	    		});
	}, 200);

	var updateInterval = 30;
	var plot = $.plot("#chart-1", $scope.chartableDatasetArray, {
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
		},
		colors: ['rgb(237,194,64)', '#8e44ad', 'rgb(203,75,75)', 'rgb(77,167,77)', 'rgb(148,64,237)', 'rgb(189,155,51)', 'rgb(140,172,198)', 'rgb(162,60,60)', 'rgb(61,133,61)', 'rgb(118,51,189)', '#27ae60', '#2c3e50', 'rgb(243,90,90)', 'rgb(92,200,92)', 'rgb(177,76,255)', 'rgb(142,116,38)', 'rgb(105,129,148)', 'rgb(121,45,45)', 'rgb(46,100,46)']
	});
	var filterArray = function(arr) {
		var output = [];
		angular.forEach(arr, function(value, key) {
			if ($('#id' + value.color).is(':checked')) {
				output.push(value);
			}
		});		
		return output;
	};
	function paint() {
		var series = plot.getData();
		for (var i = 0; i < series.length; i++) {
			$('#id' + i).next().css('background-color', series[i].color).css('color', 'white').css('margin-left', '5px').css('padding-right', '5px');
		}
	};
	function update() {		
		if ($scope.chartableDatasetArray.length) {
			plot.setData(filterArray($scope.chartableDatasetArray));			
			plot.setupGrid();
			plot.draw();
		}
		setTimeout(update, updateInterval);
	}

	update();
	paint();




}]);