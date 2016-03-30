angular
    .module('apiApp', [])
    .controller('apiAppCtrl', ['$http', controladorPrincipal]);

function controladorPrincipal($http) {
    var vm=this;

    // Realizamos un GET de todas las preguntas a mostrar
    $http.get("http://localhost:8000/preguntas.json").success(function(respuesta){
        vm.preguntas = respuesta;
    });

    // Realiza un PUT sobre la API para cambiar la opcion seleccionada y establecer el salto
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

    // Si salto es mayor a la pregunta que se le pasa devuelve false
    vm.salto = null
    vm.mostrar = function(first, pregunta) {
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