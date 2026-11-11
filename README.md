# Proyecto de scraping con Git, GitHub y DevOps

## Descripción
Este proyecto continúa la Evidencia de Aprendizaje 1 de Programación para Análisis de Datos. Se toma como referencia la extracción de información del libro **A Light in the Attic** en la página de demostración Books to Scrape.

El notebook de la primera evidencia se guarda en la carpeta `notebooks/`. El proyecto también incluye funciones sencillas para revisar los datos extraídos, pruebas automáticas y un flujo de trabajo con GitHub Actions.

> Books to Scrape es una página de demostración. Sus precios y calificaciones no representan precios comerciales reales.

## Estructura

```text
EA2_Proyecto_Scraping_DevOps/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── docs/
│   └── index.html
├── notebooks/
│   └── (aquí va el notebook de la Evidencia 1)
├── src/
│   └── analisis.py
├── tests/
│   └── test_analisis.py
├── .gitignore
└── README.md
```

## ¿Qué hace el proyecto?

- Conserva el notebook donde se aplicaron BeautifulSoup, Selenium y Scrapy.
- Cuenta cuántos campos de un producto tienen información.
- Calcula el porcentaje de completitud de los datos.
- Normaliza valores de texto, incluidos los símbolos de moneda.
- Ejecuta pruebas automáticas con GitHub Actions.
- Publica una página sencilla del proyecto mediante GitHub Pages cuando los cambios llegan a `main` y las pruebas terminan correctamente.

## Ejecutar las pruebas en Windows

Se necesita Python 3.10 o superior. Desde la carpeta principal del proyecto, abre una terminal y ejecuta:

```bash
python -m unittest discover -s tests -v
```

Para revisar el estilo del código, instala Ruff y ejecuta:

```bash
python -m pip install ruff
ruff check src tests
```

## Flujo de trabajo

1. Los cambios se guardan en una rama de trabajo.
2. Se registran con commits que expliquen qué se modificó.
3. Se crea una Pull Request para revisar los cambios.
4. GitHub Actions ejecuta la revisión de estilo y las pruebas automáticas.
5. Cuando la Pull Request se fusiona con `main`, GitHub Actions publica la página del proyecto en GitHub Pages.

## Alcance

La automatización comprueba las funciones de preparación y revisión de datos incluidas en `src/analisis.py`. El notebook de scraping se ejecuta aparte en Google Colab, porque Selenium y el acceso a páginas externas requieren un entorno distinto al de las pruebas básicas del repositorio.
