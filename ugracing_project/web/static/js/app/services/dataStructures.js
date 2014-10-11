'use strict';

angular.module('ugracing').factory('DataStructures', function(){

  var DataStructures = {};

  DataStrctures.allData = function() {
    return Object.freeze({
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
    });
  };

  return DataStructures;
  
});