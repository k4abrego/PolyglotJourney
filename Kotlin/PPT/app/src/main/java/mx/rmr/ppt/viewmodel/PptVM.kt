package mx.rmr.ppt.viewmodel

import androidx.lifecycle.ViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import mx.rmr.ppt.model.Elemento
import mx.rmr.ppt.model.GanadorPartida
import mx.rmr.ppt.model.PiedraPapelTijeras

class PptVM: ViewModel()
{
    // Modelo
    private val modeloPpt = PiedraPapelTijeras()

    // Estado
    private val _estado = MutableStateFlow(EstadoPpt())
    val estado: StateFlow<EstadoPpt> = _estado

    // Interface
    fun actualizarElementoJugador(elemento: Elemento) {
        _estado.value = _estado.value.copy(elementoJugador = elemento)
    }

    fun jugar() {
        generarElementoAndroid()
        val elementoJugador = _estado.value.elementoJugador
        val elementoAndroid = _estado.value.elementoAndroid

        if (elementoJugador != null && elementoAndroid != null) {
            val resultadoJuego = modeloPpt.jugar(elementoJugador, elementoAndroid)
            val resultadoPartida = modeloPpt.probarGanador()

            _estado.value = _estado.value.copy(
                puntosJugador = modeloPpt.puntosJugador,
                puntosAndroid = modeloPpt.puntosAndroid,
                resultadoJuego = resultadoJuego,
                resultadoPartida = resultadoPartida
            )
        }
    }

    fun reset() {

        modeloPpt.reset()
        _estado.value = _estado.value.copy(
            puntosJugador = modeloPpt.puntosJugador,
            puntosAndroid = modeloPpt.puntosAndroid,
            elementoJugador = null,
            elementoAndroid = null,
            resultadoJuego = null,
            resultadoPartida = GanadorPartida.NINGUNO
        )
    }

    private fun generarElementoAndroid() {
        val elemento = modeloPpt.generarElemento()
        _estado.value = _estado.value.copy(elementoAndroid = elemento)
    }
}