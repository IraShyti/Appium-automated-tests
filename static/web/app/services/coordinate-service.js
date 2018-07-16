angular.module('appium.services.coordinates', [])
	.factory('coordinates', ['$resource', function($resource) {
        return $resource('/api/coordinates/:x_coordinate', {x_coordinate: '@x_coordinate'},
            { 
                get:    {method:'GET'},
                save:   {method:'POST'}
        });
    }]);