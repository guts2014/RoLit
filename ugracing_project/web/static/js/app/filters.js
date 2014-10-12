'use strict';

angular.module('ugracing').filter('reverse', function() {
  return function(items) {
    return items.slice().reverse();
  };
});