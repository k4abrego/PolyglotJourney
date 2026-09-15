package com.example.aplicacionecuacionsegundogrado.model

import java.util.Locale
import kotlin.math.abs
import kotlin.math.sqrt

data class ResultadoCalculo(
    val raiz1: String = "",
    val raiz2: String = "",
    val error: String = ""
)
class CalculadoraEcuacion {

    fun resolver(a: Double, b: Double, c: Double): ResultadoCalculo {
        if (!a.isFinite() || !b.isFinite() || !c.isFinite()) {
            return ResultadoCalculo(error = "Todos los coeficientes deben ser números válidos")
        }

        if (a == 0.0) {
            return ResultadoCalculo(error = "No es una ecuación de segundo grado")
        }

        val discriminante = b * b - 4 * a * c
        return if (discriminante >= 0) {
            val raiz1 = (-b + sqrt(discriminante)) / (2 * a)
            val raiz2 = (-b - sqrt(discriminante)) / (2 * a)

            if (!raiz1.isFinite() || !raiz2.isFinite()) {
                ResultadoCalculo(error = "No fue posible calcular las raices")
            } else {
                ResultadoCalculo(
                    raiz1 = formatear(raiz1),
                    raiz2 = formatear(raiz2)
                )
            }
        } else {
            val parteReal = -b / (2 * a)
            val parteImaginaria = sqrt(abs(discriminante)) / abs(2 * a)

            if (!parteReal.isFinite() || !parteImaginaria.isFinite()) {
                ResultadoCalculo(error = "No fue posible calcular las raíces")
            } else {
                ResultadoCalculo(
                    raiz1 = "${formatear(parteReal)} + ${formatear(parteImaginaria)}i",
                    raiz2 = "${formatear(parteReal)} - ${formatear(parteImaginaria)}i"
                )
            }
        }
    }

    private fun formatear(numero: Double): String {
        val resultado = if (abs(numero) < 0.005) 0.0 else numero
        return String.format(Locale.US, "%.2f", resultado)
    }
}
