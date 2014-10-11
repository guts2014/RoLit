'use strict';

angular.module('ugracing').factory('DataLabels', function(){

  // Map tags to human-readable labels
  var DataLabels = Object.freeze({
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
  });

  return DataLabels;
  
});