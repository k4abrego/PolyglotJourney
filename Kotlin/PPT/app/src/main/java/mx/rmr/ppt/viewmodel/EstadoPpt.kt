package mx.rmr.ppt.viewmodel

import mx.rmr.ppt.model.Elemento
import mx.rmr.ppt.model.GanadorJuego
import mx.rmr.ppt.model.GanadorPartida

data class EstadoPpt(
    var puntosJugador: Int = 0,
    var puntosAndroid: Int = 0,

    var elementoJugador: Elemento? = null,
    var elementoAndroid: Elemento? = null,
    var resultadoJuego: GanadorJuego? = null,

    var resultadoPartida: GanadorPartida = GanadorPartida.NINGUNO
)