'use strict';

angular.module('confusionApp')
    .constant("baseURL", "http://localhost:3000/")
    .service('menuFactory', ['$http', 'baseURL', function($http, baseURL) {
            
        this.getDishes = function(){
            return $http.get(baseURL+"dishes");
        };
            
        this.getDish = function (index) {
            return $http.get(baseURL+"dishes/"+index);
        };
            
    }]);