'use strict';

angular.module('ugracing').service('UpdateData', function($http, $q){

  var UpdateData = {};

  UpdateData.makeRequest = function(endpoint) {
    return $http({
      method: "POST",
      url: endpoint
    });
  };

  UpdateData.all = function() {
    return UpdateData.makeRequest('telemetry-api/get-all-values/');
  };

  return UpdateData;
  
});