"""Pruebas de las funciones que revisan los datos del producto."""

import unittest

from src.analisis import (
    calcular_completitud,
    contar_campos_completos,
    normalizar_valor,
)


class TestAnalisis(unittest.TestCase):
    def test_normalizar_simbolo_libra(self):
        self.assertEqual(normalizar_valor(" Â£51.77 "), "£51.77")

    def test_contar_campos_completos(self):
        datos = {"titulo": "A Light in the Attic", "precio": "£51.77"}
        campos = ("titulo", "precio", "disponibilidad")
        self.assertEqual(contar_campos_completos(datos, campos), 2)

    def test_calcular_completitud_total(self):
        datos = {"titulo": "A Light in the Attic", "precio": "£51.77"}
        campos = ("titulo", "precio")
        self.assertEqual(calcular_completitud(datos, campos), 100.0)

    def test_calcular_completitud_parcial(self):
        datos = {"titulo": "A Light in the Attic", "precio": ""}
        campos = ("titulo", "precio")
        self.assertEqual(calcular_completitud(datos, campos), 50.0)

    def test_calcular_completitud_sin_campos(self):
        self.assertEqual(calcular_completitud({}, ()), 0.0)


if __name__ == "__main__":
    unittest.main()
