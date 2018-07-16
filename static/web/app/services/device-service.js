angular.module('appium.services.devices', [])
	.factory('devices', ['$resource', function($resource) {
        return $resource('/api/devices/:device_name', {device_name: '@device_name'},
            { 
                get:    {method:'GET'},
                save:   {method:'POST'},
                query:  {method:'GET', isArray:true},
                remove: {method:'DELETE'},
                delete: {method:'DELETE'} 
        });
    }]);
