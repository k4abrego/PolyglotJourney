package mx.rmr.menulateral

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.CenterAlignedTopAppBar
import androidx.compose.material3.DrawerState
import androidx.compose.material3.DrawerValue
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.ModalDrawerSheet
import androidx.compose.material3.ModalNavigationDrawer
import androidx.compose.material3.NavigationDrawerItem
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.material3.rememberDrawerState
import androidx.compose.runtime.Composable
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlinx.coroutines.launch
import mx.rmr.menulateral.ui.theme.MenuLateralTheme
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.AccessTime
import androidx.compose.material.icons.filled.AddAPhoto
import androidx.compose.material.icons.filled.AutoAwesome
import androidx.compose.material.icons.filled.Menu
import androidx.compose.material3.FloatingActionButton
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.tooling.preview.Preview
import androidx.navigation.NavGraph.Companion.findStartDestination
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController


sealed class Pantalla(
    val ruta: String,      //Ruta única, id único
    val etiqueta: String,  //Nombre de la pantalla/opción
    val icono: ImageVector
) {
    companion object {
        var listaPantallas = listOf(primera, segunda) //Todas las pantallas en la navegación
        const val RUTA_A = "primera"
        const val RUTA_B = "segunda"
    }
    private data object primera : Pantalla(
        RUTA_A,
        "Opción A",
        Icons.Default.AccessTime
    )
    private object segunda : Pantalla(
        RUTA_B,
        "Opción B",
        Icons.Default.AutoAwesome
    )
}
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            MenuLateralTheme {
                AppMenuLateral()
                }
            }
        }
    }

@Composable
fun AppMenuLateral(modifier: Modifier = Modifier){
    val estadoMenu = rememberDrawerState(DrawerValue.Closed)
    val navController = rememberNavController()
    val coroutineScope = rememberCoroutineScope()

    ModalNavigationDrawer(
        drawerState = estadoMenu,
        drawerContent = {
            //Componente para el menú
            ModalDrawerSheet() {
                Text("MENU LATERAL")
                HorizontalDivider()
                Pantalla.listaPantallas.forEach { pantalla ->
                    NavigationDrawerItem(
                        label = { Text(pantalla.etiqueta) },
                        selected = false,
                        icon = {
                            Icon(pantalla.icono, contentDescription = null)
                               },
                        onClick = {
                            navController.navigate(pantalla.ruta){
                                popUpTo(navController.graph.findStartDestination().id) {
                                    saveState = true
                                    inclusive = false //saca también la pantalla principal
                                }
                                launchSingleTop = true
                                restoreState = true
                            }
                            coroutineScope.launch {
                                estadoMenu.close()
                            }
                        }
                    )
                }
            }
        }
    ) {
        //Componente de la App principal
        AppPrincipal(estadoMenu, navController)
    }
}
@Composable
fun AppNavHost(navController: NavHostController, modifier: Modifier = Modifier){
    NavHost(
        navController = navController,
        startDestination = Pantalla.RUTA_A,
        modifier = modifier.fillMaxSize()
    ) {
        composable(Pantalla.RUTA_A){
            PantallaA()
        }
        composable(Pantalla.RUTA_B){
            PantallaB()
        }
    }
}

@Composable
fun AppPrincipal(estadoMenu: DrawerState, navController: NavHostController, modifier: Modifier = Modifier) {
    Scaffold(
        topBar = {
            AppTopBar(estadoMenu, modifier)
        },
        bottomBar = {
            Text(
                text = "Barra de navegación inferior",
                textAlign = TextAlign.Center,
                modifier = Modifier.fillMaxWidth()
            )
        },
        floatingActionButton = {
            BotonFlotante()
        }
    ) { innerPadding ->
        AppNavHost(
            navController,
            modifier.padding(innerPadding)
        )
    }
}

@Composable
private fun PantallaA(modifier: Modifier = Modifier){
    Card(
        elevation = CardDefaults.cardElevation(4.dp),
        shape = RoundedCornerShape(12.dp),
        modifier = modifier.fillMaxSize().padding(16.dp)
    ) {
        Column(
            modifier = modifier.fillMaxSize(),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.SpaceEvenly
        ) {
            Text("Karen Abrego")
            Text("A01753979")
            Image(painterResource(R.drawable.imagen), contentDescription = "")
        }
    }
}

@Composable
fun PantallaB(){
    Text("Hola, estás en la pantalla B")
}

@Composable
fun BotonFlotante(modifier: Modifier = Modifier){
    FloatingActionButton(
        onClick = { },
        modifier = modifier.padding(end = 8.dp, bottom = 8.dp)
    ) {
        Icon(
            imageVector = Icons.Filled.AddAPhoto,
            contentDescription = null
        )
    }
}
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AppTopBar(estadoMenu: DrawerState, modifier: Modifier = Modifier){
    val coroutineScope = rememberCoroutineScope()
    CenterAlignedTopAppBar(
        colors = TopAppBarDefaults.topAppBarColors(
            containerColor = MaterialTheme.colorScheme.primaryContainer,
            titleContentColor = MaterialTheme.colorScheme.primary,
        ),
        navigationIcon = {
            IconButton(onClick =  {
                coroutineScope.launch { estadoMenu.open() } }) {
                Icon(
                    imageVector = Icons.Filled.Menu,
                    contentDescription = null
                )
            }
                         },
        title = {
            Text (
                text = "Piedra, Papel o Tijeras",
                fontSize = 18.sp,
                textAlign = TextAlign.Center,
                modifier = Modifier
                    .padding(16.dp)
                    .fillMaxWidth()
            )
        }
    )
}

@Preview (widthDp = 300, heightDp = 500)
@Composable
private fun MenuPreview(){
    MenuLateralTheme {
        AppMenuLateral()
    }
}