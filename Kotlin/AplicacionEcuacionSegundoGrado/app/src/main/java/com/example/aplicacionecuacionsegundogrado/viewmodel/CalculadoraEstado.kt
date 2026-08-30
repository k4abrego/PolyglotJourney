package com.example.aplicacionecuacionsegundogrado.viewmodel

data class CalculadoraEstado(
    val a: Double = Double.NaN,
    val b: Double = Double.NaN,
    val c: Double = Double.NaN,
    val raiz1: String = "",
    val raiz2: String = "",
    val mensajeError: String = ""
)
