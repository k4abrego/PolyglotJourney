from dagor import JuegoD10, JugadorD10Interactivo, JugadorD10Estrategico, JugadorD10Aleatorio 

jugador1 = JugadorD10Interactivo('Humano') 
jugador2 = JugadorD10Aleatorio('Random') 
juego = JuegoD10(jugador1, jugador2) 
juego.inicia() 
