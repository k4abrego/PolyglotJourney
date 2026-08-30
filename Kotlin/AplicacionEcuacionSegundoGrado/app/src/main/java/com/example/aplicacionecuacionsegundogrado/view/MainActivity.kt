package com.example.aplicacionecuacionsegundogrado.view

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.activity.viewModels
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.ElevatedButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.aplicacionecuacionsegundogrado.ui.theme.AplicacionEcuacionSegundoGradoTheme
import com.example.aplicacionecuacionsegundogrado.viewmodel.CalculadoraEcuacionVM
import com.example.aplicacionecuacionsegundogrado.viewmodel.CalculadoraEstado
import kotlinx.coroutines.flow.StateFlow

// VISTA
class MainActivity : ComponentActivity() {
    private val viewModel: CalculadoraEcuacionVM by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            AplicacionEcuacionSegundoGradoTheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    CalculadoraApp(
                        viewModel,
                        modifier = Modifier.padding(innerPadding)
                    )
                }
            }
        }
    }
}

@Composable
fun CalculadoraApp(
    calculadoraVM: CalculadoraEcuacionVM,
    modifier: Modifier = Modifier
) {
    Column(
        horizontalAlignment = Alignment.CenterHorizontally,
        modifier = modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        Titulo("Ecuaciones de 2do grado")
        Formula("ax^2 + bx + c = 0")
        Espacio(16.dp)

        CampoCoeficiente("a:", calculadoraVM::actualizarA)
        Espacio(8.dp)
        CampoCoeficiente("b:", calculadoraVM::actualizarB)
        Espacio(8.dp)
        CampoCoeficiente("c:", calculadoraVM::actualizarC)
        Espacio(16.dp)

        BotonCalcular(calculadoraVM)
        Espacio(24.dp)
        Resultado("Raíz 1:", calculadoraVM.estado, true)
        Espacio(8.dp)
        Resultado("Raíz 2:", calculadoraVM.estado, false)
        AlertaError(calculadoraVM.estado, calculadoraVM)
    }
}

@Composable
fun CampoCoeficiente(
    etiqueta: String,
    actualizarValor: (Double) -> Unit,
    modifier: Modifier = Modifier
) {
    var texto by remember { mutableStateOf("") }
    var hayError by remember { mutableStateOf(false) }

    Row(
        verticalAlignment = Alignment.CenterVertically,
        modifier = modifier.fillMaxWidth()
    ) {
        Text(etiqueta, fontSize = 20.sp, modifier = Modifier.width(32.dp))
        OutlinedTextField(
            value = texto,
            onValueChange = {
                texto = it
                try {
                    val numero = it.toDouble()
                    if (!numero.isFinite()) {
                        throw NumberFormatException()
                    }
                    actualizarValor(numero)
                    hayError = false
                } catch (e: NumberFormatException) {
                    actualizarValor(Double.NaN)
                    hayError = true
                }
            },
            singleLine = true,
            isError = hayError,
            supportingText = {
                if (hayError) {
                    Text("casilla vacía")
                }
            },
            keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
            modifier = Modifier.fillMaxWidth()
        )
    }
}

@Composable
fun BotonCalcular(
    calculadoraVM: CalculadoraEcuacionVM,
    modifier: Modifier = Modifier
) {
    ElevatedButton(
        onClick = { calculadoraVM.calcularSoluciones() },
        modifier = modifier
    ) {
        Text("Resolver")
    }
}

@Composable
fun Resultado(
    etiqueta: String,
    estado: StateFlow<CalculadoraEstado>,
    primeraRaiz: Boolean,
    modifier: Modifier = Modifier
) {
    val estadoActual = estado.collectAsState()
    val valor = if (primeraRaiz) estadoActual.value.raiz1 else estadoActual.value.raiz2

    Row(
        verticalAlignment = Alignment.CenterVertically,
        modifier = modifier.fillMaxWidth()
    ) {
        Text(etiqueta, modifier = Modifier.width(70.dp))
        OutlinedTextField(
            value = valor,
            onValueChange = {},
            readOnly = true,
            singleLine = true,
            modifier = Modifier.fillMaxWidth()
        )
    }
}

@Composable
fun AlertaError(
    estado: StateFlow<CalculadoraEstado>,
    calculadoraVM: CalculadoraEcuacionVM
) {
    val estadoActual = estado.collectAsState()

    if (estadoActual.value.mensajeError.isNotEmpty()) {
        AlertDialog(
            onDismissRequest = { calculadoraVM.ocultarError() },
            title = { Text("Aviso") },
            text = { Text(estadoActual.value.mensajeError) },
            confirmButton = {
                TextButton(onClick = { calculadoraVM.ocultarError() }) {
                    Text("Aceptar")
                }
            }
        )
    }
}

@Composable
fun Titulo(texto: String, modifier: Modifier = Modifier) {
    Text(
        texto,
        textAlign = TextAlign.Center,
        fontSize = 30.sp,
        fontWeight = FontWeight.Bold,
        modifier = modifier
            .fillMaxWidth()
            .padding(bottom = 12.dp)
    )
}

@Composable
fun Formula(texto: String, modifier: Modifier = Modifier) {
    Text(
        texto,
        textAlign = TextAlign.Center,
        fontSize = 30.sp,
        fontWeight = FontWeight.Bold,
        modifier = modifier.fillMaxWidth()
    )
}

@Composable
fun Espacio(altura: Dp) {
    Spacer(modifier = Modifier.height(altura))
}
