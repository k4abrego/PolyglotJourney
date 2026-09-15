package com.example.aplicacionecuacionsegundogrado.viewmodel

import androidx.lifecycle.ViewModel
import com.example.aplicacionecuacionsegundogrado.model.CalculadoraEcuacion
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow

class CalculadoraEcuacionVM : ViewModel() {
    // Modelo
    private val modelo = CalculadoraEcuacion()

    // Estado
    private val _estado = MutableStateFlow(CalculadoraEstado())
    val estado: StateFlow<CalculadoraEstado> = _estado

    fun actualizarA(a: Double) {
        _estado.value = _estado.value.copy(
            a = a, raiz1 = "", raiz2 = "", mensajeError = ""
        )
    }

    fun actualizarB(b: Double) {
        _estado.value = _estado.value.copy(
            b = b, raiz1 = "", raiz2 = "", mensajeError = ""
        )
    }

    fun actualizarC(c: Double) {
        _estado.value = _estado.value.copy(
            c = c, raiz1 = "", raiz2 = "", mensajeError = ""
        )
    }

    fun calcularSoluciones() {
        val resultado = modelo.resolver(
            _estado.value.a,
            _estado.value.b,
            _estado.value.c
        )

        _estado.value = _estado.value.copy(
            raiz1 = resultado.raiz1,
            raiz2 = resultado.raiz2,
            mensajeError = resultado.error
        )
    }

    fun ocultarError() {
        _estado.value = _estado.value.copy(mensajeError = "")
    }
}
