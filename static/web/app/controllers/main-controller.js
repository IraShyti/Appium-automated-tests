app.controller('MainController', ['$scope', '$location', 'restClient', 'devices', 'testcases', 'coordinates',
	function ($scope, $location, restClient, devices, testcases, coordinates) {


		$scope.selectedDeviceIndexList = [];
		$scope.selectedTestCaseIndexList = [];
		$scope.logs = [];
		$scope.newDevice = {"device_name":"", "platform_version":"", "platform_name":"","display_name":"","device_index":0};
		$scope.removedeviceIndex = 0;
		$scope.removedevice = {"device_name":"", "platform_version":"", "platform_name":"","display_name":"","device_index":0};
		$scope.fields = 0
		$scope.the_platform = ""

		console.log($scope.selectedDeviceIndexList.length);

		loadDevices = function() {
			var deviceList = devices.query(function() {
		    	$scope.deviceList = deviceList;
		    	console.log(deviceList);
			});	
		}
		loadDevices();
		

		
/*
		var printTestCaseList;
		for(var i=0 ; i< testcases.length; i++){
			if($scope.testCaseList[i].test_platform == 'android'){
				printTestCaseList[i] = $scope.testCaseList[i];
				console.log(i);
			}
		}
*/

		$scope.addDevice = function(){
			
			$scope.newDevice.device_index = $scope.deviceList.sort(function(lhs, rhs) {
    			return rhs.device_index - lhs.device_index;
			})[0].device_index + 1;

			console.log($scope.newDevice.device_index);
			console.log($scope.newDevice);

			if($scope.newDevice.device_name == ""){
				console.log("bosh");
				fields = 0;}

			else{
				fields = 1;
				devices.save({}, $scope.newDevice, function() {
				loadDevices();
				});
			}
			$scope.fields = fields
		}

		$scope.addCoordinate = function(){

			console.log($scope.newCoordinate.x_coordinate);
			console.log($scope.newCoordinate.y_coordinate);

			coordinates.save({}, $scope.newCoordinate, function() {
				loadCoordinates();
				});
		}

		$scope.removeDevice = function(){

			console.log($scope.selectedDeviceIndexList);
			$scope.removedevice.device_name = $scope.deviceList[$scope.selectedDeviceIndexList].device_name;
			$scope.removedevice.device_display_name = $scope.deviceList[$scope.selectedDeviceIndexList].device_display_name;
			$scope.removedevice.platform_version = $scope.deviceList[$scope.selectedDeviceIndexList].platform_version;
			$scope.removedevice.platform_name = $scope.deviceList[$scope.selectedDeviceIndexList].platform_name;
			console.log($scope.removedevice.device_name);
			console.log($scope.removedevice.device_display_name);
			console.log($scope.removedevice.platform_version);
			console.log($scope.removedevice.platform_name);

			devices.remove({'device_name':$scope.removedevice.device_name}, $scope.removedevice, function() {
				console.log('ok');
				loadDevices();
			});
		}

		var testCaseList = testcases.query(function() {
    		$scope.testCaseList = testCaseList;
		}) ;



		$scope.selectDevice = function(index) {

			console.log("in function list length = " + $scope.selectedDeviceIndexList.length);


			var deviceIndex = $scope.selectedDeviceIndexList.indexOf(index);
			console.log("deviceIndex : " + deviceIndex);

			$scope.selectedDeviceIndexList = [];
			

			if($scope.selectedDeviceIndexList.length == 0){
				$scope.selectedDeviceIndexList.push(index);
					console.log($scope.selectedDeviceIndexList[0]);
					console.log("index : " + index);
					console.log("device index : " + $scope.deviceList[index].device_index);
					console.log($scope.deviceList[index].platform_name);

				
					if($scope.deviceList[index].platform_name == "Android"){
						$scope.the_platform = 'android';
						}
					else{
						$scope.the_platform = 'ios';
						}
					//console.log("platform : " + $scope.the_platform);
					//console.log($scope.testCaseList.length);
    				//console.log($scope.testCaseList);

				}	


			else{
				if($scope.selectedDeviceIndexList[0] == index){
					$scope.selectedDeviceIndexList.pop(index);
					$scope.the_platform = "";
					console.log("platform : " +$scope.the_platform)

				}
				else{
					alert("You can select just one device");
					console.log("Cant add");
					console.log("platform : " +$scope.the_platform)
				}
			}


			var printTestCaseList = new Array();
					var j = 0;
					console.log("u fut");
					console.log("platform : " +$scope.the_platform)
					for(var i=0 ; i< $scope.testCaseList.length; i++){
						//console.log($scope.testCaseList[i].test_platform);
						if($scope.testCaseList[i].test_platform == $scope.the_platform){
						//console.log("testCastList : " + $scope.testCaseList[i].test_platform)
						printTestCaseList[j] = $scope.testCaseList[i];

						//console.log(i);
						//console.log(" print test case list : " + printTestCaseList[j]);
						j++;
						}
					}

			$scope.testCaseList = printTestCaseList;
			console.log($scope.selectedDeviceIndexList.length);

			};



		$scope.selectTestCase = function(index) {

			var itemIndex = $scope.selectedTestCaseIndexList.indexOf(index);
			if(itemIndex != -1) {
				$scope.selectedTestCaseIndexList.splice(itemIndex,1)
			} else {
				$scope.selectedTestCaseIndexList.push(index);
			}
		};

		$scope.startAppium = function(flag) {
			

		}

		$scope.startTest = function(start) {

			$scope.logs = [];
			angular.element('#st-control-4').click();
			var now = new Date();
   			var strDateTime = [AddZero(now.getDate()), AddZero(now.getMonth() + 1), now.getFullYear()].join("-");
   			document.getElementById("Console").innerHTML = "Now: " + strDateTime;
   			$scope.strDateTime = strDateTime;

			/*
			restClient.starttest($scope.testCaseList[$scope.selectedTestCaseIndex].attribute_name, $scope.deviceList[$scope.selectedDeviceIndex].device_name, start)
				.success(function(data) {

				})
				.error(function(data, status) {
					alert("Test did not start!");
				});
			*/

			$scope.selectedTestCaseIndexList.sort();
			var test_names_list = []
			for (var i = 0; i < $scope.selectedTestCaseIndexList.length; i++) {
				test_names_list.push($scope.testCaseList[$scope.selectedTestCaseIndexList[i]].attribute_name);
			};

			$scope.selectedDeviceIndexList.sort();
			var device_names_list = []
			for (var i = 0; i < $scope.selectedDeviceIndexList.length; i++) {
				device_names_list.push($scope.deviceList[$scope.selectedDeviceIndexList[i]].device_name);
			};

			restClient.starttest(test_names_list, device_names_list)
				.success(function(data) {

				})
				.error(function(data, status) {
					alert("Test did not start!");
				});

		}

		function AddZero(num) {
   			 return (num >= 0 && num < 10) ? "0" + num : num + "";
		}

		Array.prototype.inArray = function(comparer) { 
		    for(var i=0; i < this.length; i++) { 
		        if(comparer(this[i])) return true; 
		    }
		    return false; 
		}; 

		Array.prototype.pushIfNotExist = function(element, comparer) { 
		    if (!this.inArray(comparer)) {
		        this.unshift(element);
		    }
		};

		$scope.addLog = function(log) {

			console.log('id: ' + log.log_id + ' body: ' + log.body + ' type: ' + log.log_type + " status:" + log.status + "download: " + log.download );
			//logs = $scope.logs;
			//logs.push(log);
			//$scope.logs = logs;
			$scope.logs.pushIfNotExist(log, function(e) {
				return e.log_id === log.log_id 
			});
			
		};

		var updater = {
    		errorSleepTime: 500,
    		cursor: null,

    		poll: function() {
        	

        		args = {}
        		if (updater.cursor) 
        			args['cursor'] = updater.cursor;

        		restClient.logs(args)
				.success(function(data) {
					updater.onSuccess(data);
				})
				.error(function(data, status) {
  					console.log('Repos error', status, data);
  					updater.onError(data);
				});
    		},

		    onSuccess: function(response) {
		        
		        console.log(response.messages[0]);
		        console.log(response.messages);

					console.log('id: ' + response.messages[0].log_id + ' body: ' + response.messages[0].body);
					$scope.addLog(response.messages[0]);

				/*
		        for (message in response.messages) {


					console.log('id: ' + message.log_id + ' body: ' + message.body);
		        	$scope.addLog(message);
		        }
		        */

		        updater.errorSleepTime = 500;
		        window.setTimeout(updater.poll, 0);
		    },

		    onError: function(response) {
		        updater.errorSleepTime *= 2;
		        console.log("Poll error; sleeping for", updater.errorSleepTime, "ms");
		        window.setTimeout(updater.poll, updater.errorSleepTime);
		    }
		};

		updater.poll();

}]);



/*


var updater = {
    errorSleepTime: 500,
    cursor: null,

    poll: function() {
        var args = {"_xsrf": getCookie("_xsrf")};
        if (updater.cursor) args.cursor = updater.cursor;
        $.ajax({url: "/a/message/updates", type: "POST", dataType: "text",
                data: $.param(args), success: updater.onSuccess,
                error: updater.onError});
    },

    onSuccess: function(response) {
        try {
            updater.newMessages(eval("(" + response + ")"));
        } catch (e) {
            updater.onError();
            return;
        }
        updater.errorSleepTime = 500;
        window.setTimeout(updater.poll, 0);
    },

    onError: function(response) {
        updater.errorSleepTime *= 2;
        console.log("Poll error; sleeping for", updater.errorSleepTime, "ms");
        window.setTimeout(updater.poll, updater.errorSleepTime);
    },

    newMessages: function(response) {
        if (!response.messages) return;
        updater.cursor = response.cursor;
        var messages = response.messages;
        updater.cursor = messages[messages.length - 1].id;
        console.log(messages.length, "new messages, cursor:", updater.cursor);
        for (var i = 0; i < messages.length; i++) {
            updater.showMessage(messages[i]);
        }
    },

    showMessage: function(message) {
        var existing = $("#m" + message.id);
        if (existing.length > 0) return;
        var node = $(message.html);
        node.hide();
        $("#inbox").append(node);
        node.slideDown();
    }
};

*/