'use strict';

angular.module('ugracing').factory('DataStructures', function(){

  var DataStructures = {};

  DataStructures.allData = function() {
    return {
        battery: null,
        brake: null,
        coolant_t: null,
        fuel: null,
        gear: null,
        map: null,
        mat: null,
        o2: null,
        rpm: null,
        speed: null,
        throttle: null,
        wheel_t_1: null,
        wheel_t_2: null,
        wheel_t_3: null,
        wheel_t_4: null,
        wheel_v_1: null,
        wheel_v_2: null,
        wheel_v_3: null,
        wheel_v_4: null
    };
  };

  DataStructures.allDataChartable = function() {

    var chartableData = DataStructures.allData();
    var labels = DataStructures.dataLabels();

    angular.forEach(chartableData, function(value, key) {
        chartableData[key] = {
            label: labels[key],
            data: []
        };
    });

    return chartableData;

  };

  DataStructures.dataLabels = function() {
    return {
        battery: 'Battery',
        brake: 'Brake',
        coolant_t: 'Coolant temperature',
        fuel: 'Fuel',
        gear: 'Gear',
        map: 'Manifold pressure',
        mat: 'Manifold temperature',
        o2: 'Oxygen',
        rpm: 'RPM',
        speed: 'Speed',
        throttle: 'Throttle',
        wheel_t_1: 'Wheel 1 temperature',
        wheel_t_2: 'Wheel 2 temperature',
        wheel_t_3: 'Wheel 3 temperature',
        wheel_t_4: 'Wheel 4 temperature',
        wheel_v_1: 'Wheel 1 velocity',
        wheel_v_2: 'Wheel 2 velocity',
        wheel_v_3: 'Wheel 3 velocity',
        wheel_v_4: 'Wheel 4 velocity'
    };
  };

  return DataStructures;
  
});