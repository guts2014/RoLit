'use strict';

angular.module('ugracing').service('UpdateData', function($http, $q){

  var UpdateData = {};

  UpdateData.makeRequest = function(endpoint) {
    $http.get(endpoint).
    success(function(data, status, headers, config) {
      console.log(data);
    }).
    error(function(data, status, headers, config) {
      console.log('Error: could not connect to API endpoint.');
    });
  };

  UpdateData.all = function() {
    return UpdateData.makeRequest('telemetry-api/get-latest-values/');
  };

  return UpdateData;
  
});