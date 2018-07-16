angular.module('appium.services.testcases', [])
	.factory('testcases', ['$resource', function($resource) {
        return $resource('/api/test_cases/:name', {name: '@name'},
            { 
                get:    {method:'GET'},
                save:   {method:'POST'},
                query:  {method:'GET', isArray:true},
                remove: {method:'DELETE'},
                delete: {method:'DELETE'} 
        });
    }]);
