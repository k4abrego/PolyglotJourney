package mx.rmr.ppt.model

class PiedraPapelTijeras
{
    var puntosJugador: Int = 0
        private set
    var puntosAndroid: Int = 0
        private set

    private val PUNTAJE_GANADOR = 3

    fun reset() {
        puntosJugador = 0
        puntosAndroid = 0
    }

//    fun generarElemento(): Elemento {
//        return Elemento.entries.random()
//    }

    fun generarElemento() = Elemento.entries.random()

    fun jugar(elementoJugador: Elemento, elementoAndroid: Elemento): GanadorJuego {

        // Empate
        if (elementoJugador == elementoAndroid) {
            return GanadorJuego.EMPATE
        }

        if (elementoJugador == Elemento.PIEDRA && elementoAndroid == Elemento.TIJERAS
            || elementoJugador == Elemento.PAPEL && elementoAndroid == Elemento.PIEDRA
            || elementoJugador == Elemento.TIJERAS && elementoAndroid == Elemento.PAPEL) {
            puntosJugador++
            return GanadorJuego.JUGADOR
        }

        puntosAndroid++
        return GanadorJuego.ANDROID
    }



    fun probarGanador(): GanadorPartida {
        if (puntosJugador == PUNTAJE_GANADOR) {
            return GanadorPartida.JUGADOR
        } else if (puntosAndroid == PUNTAJE_GANADOR) {
            return GanadorPartida.ANDROID
        }
        return GanadorPartida.NINGUNO
    }
}