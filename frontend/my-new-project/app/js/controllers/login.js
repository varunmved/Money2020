angular.module('bae.controllers')
.controller('LoginCtrl', ['$scope', 'Authentication', 
  function($scope, Authentication) {
    $scope.login = function() {
      Authentication.login();
    };
  }
]);
