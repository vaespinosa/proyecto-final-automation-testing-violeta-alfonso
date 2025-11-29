# Framework de Automatización de Pruebas

## Propósito del Proyecto
Este proyecto implementa un framework profesional y pedagógico para automatización de pruebas de aplicaciones web y APIs. Permite validar funcionalidades reales, detectar errores y asegurar la calidad del software mediante pruebas independientes y reportes claros.

## Asistencia técnica y automatización

Para la realización de este proyecto se utilizó una herramienta de inteligencia artificial como apoyo en la programación. Su uso potenció el trabajo del tester, facilitando la resolución de problemas, la automatización de tareas y el aprendizaje continuo en el desarrollo de pruebas automatizadas.

## Tecnologías Utilizadas
- **Python 3**
- **Selenium WebDriver** (automatización UI)
- **Requests** (cliente HTTP para pruebas de API sobre JSONPlaceholder)
- **Pytest** (ejecución y parametrización de tests)
- **pytest-html** (reportes HTML visuales)

## Estructura del Proyecto
```
proyecto-final-automation-testing-violeta-alfonso/
├── data/                # Datos de prueba (CSV)
│   └── login_data.csv   # Dataset para login parametrizado
├── logs/                # Logs de ejecución detallados
├── pages/               # Page Objects (UI)
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── screenshots/         # Capturas automáticas de fallos UI
├── tests/               # Casos de prueba UI y API
│   ├── test_login_ui.py
│   ├── test_cart_ui.py
│   ├── test_checkout_ui.py
│   ├── test_navigation_ui.py
│   ├── test_sort_ui.py
│   ├── test_cart_state_ui.py
│   └── test_api_jsonplaceholder.py
├── utils/               # Utilidades (logger, screenshots, data loader)
│   ├── logger.py
│   ├── screenshot.py
│   └── data_loader.py
├── pytest.ini           # Configuración de Pytest y reportes
├── README.md            # Documentación principal
```

## Instalación de Dependencias
1. Instala Python 3 y pip si no los tienes.
2. Ejecuta en terminal (en la raíz del proyecto):
   ```
   pip install -r requirements.txt
   ```
   Si no existe `requirements.txt`, instala manualmente:
   ```
   pip install selenium requests pytest pytest-html
   ```

## Ejecución de Pruebas
1. Ubícate en la raíz del proyecto.
2. Ejecuta:
   ```
   python -m pytest --html=report.html --self-contained-html --disable-warnings
   ```
   Esto ejecutará todos los tests UI y API y generará el reporte HTML completo.

## Interpretación de Reportes
- El reporte HTML se genera como `report.html` en la raíz.
- Ábrelo con tu navegador para ver:
   - Estado de cada test (OK/FAIL)
   - Descripción detallada de cada caso (docstring)
   - Mensajes de error y logs
   - Capturas de pantalla en caso de fallos UI
   - Resumen visual y profesional

## Logs

- El framework escribe logs detallados en `logs/test_log.log` (archivo en modo `append`).
- Comandos útiles en PowerShell:
   - Ver últimas 50 líneas:
      ```powershell
      Get-Content .\logs\test_log.log -Tail 50
      ```
   - Tailing en vivo:
      ```powershell
      Get-Content .\logs\test_log.log -Wait
      ```
   - Borrar el log (reiniciar):
      ```powershell
      Remove-Item .\logs\test_log.log -Force
      ```
   - Ejecutar pytest y ver logs en consola en tiempo real:
      ```powershell
      python -m pytest -s
      python -m pytest -o log_cli=true
      ```

Estas opciones facilitan la depuración y revisión de la trazabilidad de las ejecuciones.

## CI / Artifacts

He incluido un workflow de GitHub Actions (`.github/workflows/ci.yml`) que se ejecuta en `push` y `pull_request` sobre `main`/`master`. El workflow:

- Instala dependencias desde `requirements.txt` (si existe).
- Ejecuta `pytest` y genera `report_all.html`.
- Publica como artifacts los siguientes archivos para descarga desde la interfaz de GitHub Actions:
   - `report_all.html` (reporte HTML completo)
   - `logs/test_log.log` (archivo de logs)
   - la carpeta `screenshots/` (capturas generadas durante la ejecución)

Para ver los artifacts en GitHub: entra al repositorio → pestaña **Actions** → selecciona el workflow/job reciente → en la página del run busca la sección **Artifacts** y descarga los archivos.

Nota: en local `screenshots/` sólo se llenará si hay fallos o si tu ejecución de tests fuerza capturas (el hook en `conftest.py` toma capturas cuando existe el fixture `driver`).

## Casos de Prueba Incluidos

### UI (Selenium)
- **test_login_ui.py**: Login parametrizado con datos reales, validando éxito y errores.
- **test_cart_ui.py**: Añadir y eliminar producto del carrito, validando estados reales.
- **test_checkout_ui.py**: Flujo de compra exitoso y manejo de datos incompletos en checkout.
- **test_navigation_ui.py**: Navegación a detalles de producto desde la lista.
- **test_sort_ui.py**: Ordenamiento de productos por precio (low to high).
- **test_cart_state_ui.py**: Estado dinámico del carrito: agrega y elimina productos, valida el contador y el estado visual/lógico tras cada acción.

### API (JSONPlaceholder)
- **test_api_jsonplaceholder.py**: 5 casos defendibles sobre la API pública JSONPlaceholder (usando Requests como cliente HTTP):
   1. GET /posts: Validación de respuesta y estructura.
   2. GET /users/1: Validación de datos de usuario.
   3. POST /posts: Creación de post y validación de datos.
   4. DELETE /posts/1: Eliminación de post y validación de respuesta.
   5. Flujo encadenado: Crear y luego eliminar un post.

## Funcionalidad Esperada
- Todas las pruebas se ejecutan de manera consistente y son independientes entre sí.
- La falla de una prueba no afecta la ejecución de las demás.
- Los reportes generados son claros, visuales y autoexplicativos, mostrando docstrings y capturas.
- La estructura modular del código facilita la incorporación de nuevas pruebas y el mantenimiento.

## Nota sobre las pruebas de API y JSONPlaceholder

Las pruebas de API utilizan la biblioteca `requests` como cliente HTTP para interactuar con la API pública JSONPlaceholder. Esto significa que:
- Si la API está disponible y responde correctamente, los tests pasan y el reporte es exitoso.
- Si la API falla, cambia su estructura, requiere autenticación o no está disponible, los tests pueden fallar, reflejando el estado real del servicio externo.
- Este comportamiento es profesional y esperado en proyectos reales, ya que valida la robustez del framework y la capacidad de detectar errores genuinos.

**Importante:** Los resultados de los tests de API pueden variar según la disponibilidad y el estado de JSONPlaceholder. El framework está correctamente implementado y listo para testear cualquier API real, siguiendo las mejores prácticas de la industria .

---

**¡Listo para entregar y ejecutar!**
