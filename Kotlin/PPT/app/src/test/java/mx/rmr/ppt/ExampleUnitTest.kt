package mx.rmr.ppt

import mx.rmr.ppt.model.Elemento
import mx.rmr.ppt.model.GanadorJuego
import mx.rmr.ppt.model.GanadorPartida
import mx.rmr.ppt.model.PiedraPapelTijeras
import mx.rmr.ppt.viewmodel.PptVM
import org.junit.Test

import org.junit.Assert.*
import org.junit.Before

/**
 * Example local unit test, which will execute on the development machine (host).
 *
 * See [testing documentation](http://d.android.com/tools/testing).
 */
class ExampleUnitTest
{
    private lateinit var juego: PiedraPapelTijeras

    @Before
    fun setup() {
        juego = PiedraPapelTijeras()
    }

    @Test
    fun `Simula una partida completa en ViewModel`() {
        val viewModel = PptVM()
        while (viewModel.estado.value.resultadoPartida == GanadorPartida.NINGUNO) {
            viewModel.actualizarElementoJugador(Elemento.PIEDRA)
            viewModel.jugar()
            println()
            println(viewModel.estado.value)
            println("Puntos: ${viewModel.estado.value.puntosJugador} - ${viewModel.estado.value.puntosAndroid}")
        }
        println("Gana: ${viewModel.estado.value.resultadoPartida}")
        assertEquals(1, 1)
    }

    @Test
    fun probarEmpate() {
        //val juego = PiedraPapelTijeras()

        for (elementoJ in Elemento.entries) {
            for (elementoA in Elemento.entries) {
                if (elementoJ == elementoA) {
                    assertEquals(GanadorJuego.EMPATE,
                        juego.jugar(elementoJ, elementoA))
                } else {
                    assertNotEquals(GanadorJuego.EMPATE,
                        juego.jugar(elementoJ, elementoA))
                }
            }
        }
    }

    @Test
    fun probarGanador() {
        assertEquals(GanadorPartida.NINGUNO, juego.probarGanador())

        juego.jugar(Elemento.PIEDRA, Elemento.TIJERAS)
        juego.jugar(Elemento.PIEDRA, Elemento.TIJERAS)
        juego.jugar(Elemento.PIEDRA, Elemento.TIJERAS)
        assertEquals(GanadorPartida.JUGADOR, juego.probarGanador())

        juego.jugar(Elemento.PIEDRA, Elemento.PAPEL)
        juego.jugar(Elemento.PIEDRA, Elemento.PAPEL)
        juego.jugar(Elemento.PIEDRA, Elemento.PAPEL)
        assertEquals(GanadorPartida.ANDROID, juego.probarGanador())
    }

    @Test
    fun probarContadores() {
        juego.jugar(Elemento.PIEDRA, Elemento.PIEDRA)
        assertEquals(0, juego.puntosJugador)
        assertEquals(0, juego.puntosAndroid)

        juego.jugar(Elemento.PIEDRA, Elemento.TIJERAS)
        assertEquals(1, juego.puntosJugador)

        juego.jugar(Elemento.PIEDRA, Elemento.PAPEL)
        assertEquals(1, juego.puntosAndroid)

        juego.jugar(Elemento.PIEDRA, Elemento.PIEDRA)
        assertEquals(1, juego.puntosJugador)
        assertEquals(1, juego.puntosAndroid)
    }

    @Test
    fun probarJugadorGana() {

        for (elementoJ in Elemento.entries) {
            for (elementoA in Elemento.entries) {
                if (elementoJ == Elemento.PIEDRA && elementoA == Elemento.TIJERAS
                    || elementoJ == Elemento.PAPEL && elementoA == Elemento.PIEDRA
                    || elementoJ == Elemento.TIJERAS && elementoA == Elemento.PAPEL) {
                        assertEquals(GanadorJuego.JUGADOR,
                        juego.jugar(elementoJ, elementoA))
                } else {
                    assertNotEquals(GanadorJuego.JUGADOR,
                        juego.jugar(elementoJ, elementoA))
                }
            }
        }
    }

    @Test
    fun addition_isCorrect() {
        assertEquals(4, 2 + 2)
    }
}