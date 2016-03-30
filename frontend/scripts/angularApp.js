angular
    .module('apiApp', [])
    .controller('apiAppCtrl', ['$http', controladorPrincipal]);

function controladorPrincipal($http) {
    var vm=this;

    $http.get("http://localhost:8000/preguntas.json").success(function(respuesta){
        console.log("res:", respuesta);
        vm.preguntas = respuesta;
    });

    vm.select = 1

    vm.click = function(pregunta, opcion_seleccionada, salto) {
        if (!isNaN(parseFloat(opcion_seleccionada)) && isFinite(opcion_seleccionada)) {
            pregunta.opcion_seleccionada = opcion_seleccionada;
            pregunta.salto = salto;

            $http.put("http://localhost:8000/preguntas/" + pregunta.pk + ".json", pregunta)
                .success(function(respuesta) {
                    console.log(respuesta);
                });
        };
    }

    vm.salto = null
    vm.saltar = function(first, pregunta) {
        if (first) {
            vm.salto = pregunta.salto
            return true
        }

        if (vm.salto > pregunta.pk){
            return false
        }

        vm.salto = pregunta.salto
        return true
    }
}