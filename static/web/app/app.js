'use strict';
var app = angular.module('appium', [
    'ngResource',
    'ngCookies',
    'appium.services.devices', 
    'appium.services.testcases',
    'appium.services.restClient',
    'appium.services.coordinates',
    'ngMessages', 
    'ui.router',
    'ngSanitize',
    ]);

app.run(
  ['$rootScope', '$state', '$stateParams', '$cookies',
    function ($rootScope,   $state,   $stateParams, $cookies) {

    }
  ]
).config(function($stateProvider, $urlRouterProvider, $locationProvider) {

    $urlRouterProvider.otherwise('/');
    $locationProvider.html5Mode(true);
    $locationProvider.hashPrefix = '!';
        
});

        