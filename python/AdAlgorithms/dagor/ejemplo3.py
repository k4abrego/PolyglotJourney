from dagor import JuegoOrugas, JugadorOrugasAleatorio, JugadorOrugasInteractivo

jugador1 = JugadorOrugasInteractivo
jugador2 = JugadorOrugasAleatorio
juego = JuegoOrugas(jugador1, jugador2, 10,10)
juego.inicia()