package mx.rmr.ppt.view

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Home
import androidx.compose.material.icons.filled.Info
import androidx.compose.ui.graphics.vector.ImageVector

//sealed
sealed class Pantalla(
    val ruta: String, // Ruta única, id único
    val etiqueta: String, // Nombre de la pantalla/opción
    val icono: ImageVector
)
{
    // Rutas
    companion object { // Miembros de la clase
        var listaPantallas = listOf(PptApp, AcercaDe) // Todas las pantallas en la navegación
        const val RUTA_PPT_APP = "PptApp"
        const val RUTA_ACERCA_DE = "AcercaDe"
    }
    private data object PptApp:
        Pantalla(RUTA_PPT_APP, "PPT", Icons.Default.Home)
    private data object AcercaDe:
        Pantalla(RUTA_ACERCA_DE, "Acerca de", Icons.Default.Info)
}





