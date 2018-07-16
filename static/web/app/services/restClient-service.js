var baseUrl = '/api/';
//var staticUrl = 'http://localhost/';

angular.module('appium.services.restClient', [])
	.factory('restClient', ['$http', function($http) {

    	var starttest = function(test_name_list, device_name_list) {

            var test_names = '';
            for (var i = 0; i < test_name_list.length; i++) {
                var test_name = test_name_list[i];
                test_names += 'test_name=' + test_name + '&';
            };
            //test_names = test_names.slice(0,-1);

            var device_names = '';
            for (var i = 0; i < device_name_list.length; i++) {
                var device_name = device_name_list[i];
                device_names += 'device_name=' + device_name + '&';
            }
            device_names = device_names.slice(0,-1);

    		return $http({
    			method: 'GET',
    			url: baseUrl + 'starttest?' + test_names + device_names
    		});
    	};


        var getRequestWithParameters = function(items, data) {
            return $http({
                method: 'GET',
                url: baseUrl + items,
                data: data
            });
        };


        var getIP = function(items, data) {
            return $http({
                method: 'GET',
                url: baseUrl + items,
                data: data
            });
        };

        var postRequest = function(data) {
            return $http({
                method: 'POST',
                url: baseUrl + 'logs',
                data: data
            });
        };
    	return {
            ip : function() {return getIP();},
            logs : function(data) { return postRequest('data'); },
            starttest : function(test_name_list, device_name_list) { return starttest(test_name_list,device_name_list);}

    	};



    }]);