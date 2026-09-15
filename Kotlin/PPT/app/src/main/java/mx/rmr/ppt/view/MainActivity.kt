package mx.rmr.ppt.view

import android.annotation.SuppressLint
import android.os.Bundle
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.activity.viewModels
import androidx.compose.foundation.Image
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.twotone.Info
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.BottomAppBar
import androidx.compose.material3.CenterAlignedTopAppBar
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.NavigationBarItem
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.currentBackStackEntryAsState
import androidx.navigation.compose.rememberNavController
import mx.rmr.ppt.R
import mx.rmr.ppt.model.Elemento
import mx.rmr.ppt.model.GanadorPartida
import mx.rmr.ppt.ui.theme.PPTTheme
import mx.rmr.ppt.viewmodel.PptVM

class MainActivity : ComponentActivity()
{
    // View Model
    private val viewModel: PptVM by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            PPTTheme {
                //PptApp(viewModel)
                AppPrincipal(viewModel)
            }
        }
    }
}

@Composable
fun AppPrincipal(pptVM: PptVM, modifier: Modifier = Modifier) {
    val navController = rememberNavController()
    Scaffold(
        topBar = { PptAppBar() },
        content = { innerPadding ->
           AppNavHost(
              pptVM,
              navController = navController,
              modifier = modifier.padding(innerPadding)
            )
            //PptApp(pptVM, modifier = modifier.padding(innerPadding))
        },
        bottomBar = { AppBottomBar(navController)}
    )
}

@Composable
fun AppNavHost(
    pptVM: PptVM,
    navController: NavHostController,
    modifier: Modifier = Modifier
) {
    NavHost(
        navController = navController,
        startDestination = Pantalla.RUTA_PPT_APP,
        modifier = modifier.fillMaxSize()
    ) {
        composable(Pantalla.RUTA_PPT_APP) {
            PptApp(pptVM)
        }
        composable(Pantalla.RUTA_ACERCA_DE) {
            AcercaDe()
        }
    }
}


@Composable
fun AppBottomBar(navController: NavHostController, modifier: Modifier = Modifier) {
    BottomAppBar {
        val pilaNavegacion by navController.currentBackStackEntryAsState()
        val pantallaActual = pilaNavegacion?.destination
// Genera el menú inferior
        Pantalla.listaPantallas.forEach { pantalla ->
            NavigationBarItem(
                selected = pantallaActual?.route == pantalla.ruta,
                onClick = {
                    navController.navigate(pantalla.ruta) {
                        popUpTo(navController.graph.startDestinationId) {
                            saveState = true
                            inclusive = true // saca también la pantalla inicial
                        }
                        launchSingleTop = true // Navega solo si no estamos ahí
                        restoreState = true
                    }
                },
                label = { Text(pantalla.etiqueta) },
                icon = {
                    Icon(
                        pantalla.icono,
                        pantalla.etiqueta
                    )
                },
                alwaysShowLabel = true
            )
        }
    }
}


@Composable
fun PptApp(pptVM: PptVM, modifier: Modifier = Modifier) {
    // Estado
    val estado = pptVM.estado.collectAsState()
        Column(
            modifier = modifier
                .padding(16.dp)
                .fillMaxSize()
        ) {
            Row(
                modifier = Modifier.fillMaxWidth()
            ) {
                Column(
                    modifier = Modifier
                        .fillMaxWidth()
                        .weight(1f)
                ) {
                    Etiqueta("Jugador")
                    Marcador(estado.value.puntosJugador)
                }
                Column(
                    modifier = Modifier
                        .fillMaxWidth()
                        .weight(1f)
                ) {
                    Etiqueta("Android")
                    Marcador(estado.value.puntosAndroid)
                }
            }
            // Botones
            BotonElemento(Elemento.PIEDRA, onClick = {
                pptVM.actualizarElementoJugador(Elemento.PIEDRA)
                pptVM.jugar()
            })

            // Renglón con los otros dos botones
            Row (
                horizontalArrangement = Arrangement.SpaceAround,
                modifier = Modifier.fillMaxWidth()
            ) {
                BotonElemento(Elemento.PAPEL,
                    onClick = {
                        pptVM.actualizarElementoJugador(Elemento.PAPEL)
                        pptVM.jugar()
                    },
                    modifier = Modifier.weight(1f)
                )
                BotonElemento(Elemento.TIJERAS,
                    onClick = {
                        pptVM.actualizarElementoJugador(Elemento.TIJERAS)
                        pptVM.jugar()
                    },
                    modifier = Modifier.weight(1f)
                )
            }
    }
    // Resultado del juego individual
    if (estado.value.resultadoJuego != null) {
        val resultado = "${estado.value.elementoJugador} vs ${estado.value.elementoAndroid} -> ${estado.value.resultadoJuego}"
        Toast.makeText(LocalContext.current, resultado, Toast.LENGTH_SHORT).show()
    }

    // Resultado de la partida
    if (estado.value.resultadoPartida != GanadorPartida.NINGUNO) {
        ResultadoPartida(estado.value.resultadoPartida) {
            pptVM.reset()
        }
    }
}

@Composable
fun ResultadoPartida(ganador: GanadorPartida, onClick: () -> Unit) {
    AlertDialog(
        onDismissRequest = {},
        title = { Text(text = "Resultado") },
        text = { Text(text = "Ganador: $ganador") },
        icon = {
            Icon(imageVector = Icons.TwoTone.Info, contentDescription = "Info")
        },
        confirmButton = {
            TextButton(onClick = { onClick() }) {
                Text(text = "Reiniciar la partida")
            }
        },
    )
}

@Composable
fun BotonElemento(elemento: Elemento, onClick: () -> Unit, modifier: Modifier = Modifier) {
    IconButton(onClick = {
        onClick()
    },
        modifier = modifier
            .height(128.dp)
            .width(128.dp)) {
        val idImagen = when (elemento) {
            Elemento.PIEDRA -> R.drawable.piedra
            Elemento.PAPEL -> R.drawable.papel
            Elemento.TIJERAS -> R.drawable.tijeras
        }
        Image(painter = painterResource(id = idImagen), contentDescription = "Piedra")
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun PptAppBar(modifier: Modifier = Modifier) {
    CenterAlignedTopAppBar(
        colors = TopAppBarDefaults.topAppBarColors(
            containerColor = MaterialTheme.colorScheme.primaryContainer,
            titleContentColor = MaterialTheme.colorScheme.primary
        ),
        title = {
            Text("Piedra, Papel o Tijeras",
                textAlign = TextAlign.Center,
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(16.dp)
            )
        },
        //actions = {Icon(Icons.Outlined.MoreVert, contentDescription = null)},
        //navigationIcon = {Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = null)}
    )
}


@Composable
private fun Etiqueta(texto: String, modifier: Modifier = Modifier) {
    Text(
        text = texto,
        textAlign = TextAlign.Center,
        modifier = modifier
            .fillMaxWidth()
            .padding(4.dp)
    )
}

@Composable
private fun Marcador(valor: Int, modifier: Modifier = Modifier) {
    Text(
        text = "%02d".format(valor),
        textAlign = TextAlign.Center,
        style = MaterialTheme.typography.headlineSmall,
        modifier = modifier
            .fillMaxWidth()
            .padding(start = 8.dp, end = 8.dp)
            .border(width = 2.dp, color = Color.LightGray)
    )
}

@SuppressLint("ViewModelConstructorInComposable")
@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    PPTTheme {
        AppPrincipal(PptVM())
    }
}