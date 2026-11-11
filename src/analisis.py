"""Funciones sencillas para revisar los datos obtenidos en el scraping."""

CAMPOS_ESPERADOS = (
    "titulo",
    "precio",
    "disponibilidad",
    "upc",
    "tipo_producto",
    "precio_sin_impuestos",
    "precio_con_impuestos",
    "impuesto",
    "numero_resenas",
    "calificacion",
)


def normalizar_valor(valor):
    """Limpia espacios y corrige el símbolo de libra si viene mal codificado."""
    if valor is None:
        return ""

    texto = str(valor).replace("Â£", "£")
    return " ".join(texto.strip().split())


def contar_campos_completos(datos, campos=CAMPOS_ESPERADOS):
    """Cuenta cuántos campos esperados tienen un valor."""
    return sum(
        1 for campo in campos if normalizar_valor(datos.get(campo)) != ""
    )


def calcular_completitud(datos, campos=CAMPOS_ESPERADOS):
    """Calcula el porcentaje de campos completos."""
    if not campos:
        return 0.0

    completos = contar_campos_completos(datos, campos)
    return round((completos / len(campos)) * 100, 2)
