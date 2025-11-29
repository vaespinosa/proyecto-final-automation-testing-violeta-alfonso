

# Documentación Técnica y Pedagógica

## Resumen del Proyecto
Framework profesional de automatización de pruebas para aplicaciones web y APIs, desarrollado en Python. Incluye validaciones reales, reportes HTML, logging detallado y estructura modular, siguiendo consignas pedagógicas y estándares de la industria.

## Tecnologías Utilizadas
- Python 3
- Selenium WebDriver (UI)
- Requests (cliente HTTP para API JSONPlaceholder)
- Pytest (framework de testing y parametrización)
- pytest-html (reportes visuales)

## Estructura del Proyecto
```
proyecto-final-automation-testing-violeta-alfonso/
├── data/                # Datos de prueba (CSV)
├── logs/                # Logs de ejecución
├── pages/               # Page Objects (UI)
├── screenshots/         # Capturas automáticas de fallos UI
├── tests/               # Casos de prueba UI y API
├── utils/               # Utilidades (logger, screenshots, data loader)
├── pytest.ini           # Configuración de Pytest y reportes
├── README.md            # Documentación principal
├── DOCUMENTACION.md     # Documentación técnica y pedagógica
```

## Casos de Prueba Implementados

### UI (Selenium)
- **test_login_ui.py**: Login parametrizado con datos reales, validando éxito y errores.
- **test_cart_ui.py**: Añadir y eliminar producto del carrito, validando estados reales.
- **test_checkout_ui.py**: Flujo de compra exitoso y manejo de datos incompletos en checkout.
- **test_navigation_ui.py**: Navegación a detalles de producto desde la lista.
- **test_sort_ui.py**: Ordenamiento de productos por precio (low to high).
- **test_cart_state_ui.py**: Estado dinámico del carrito: agrega y elimina productos, valida el contador y el estado visual/lógico tras cada acción.

### API (JSONPlaceholder)
- **test_api_jsonplaceholder.py**: 5 casos defendibles sobre la API pública JSONPlaceholder:
  1. GET /posts: Validación de respuesta y estructura.
  2. GET /users/1: Validación de datos de usuario.
  3. POST /posts: Creación de post y validación de datos.
  4. DELETE /posts/1: Eliminación de post y validación de respuesta.
  5. Flujo encadenado: Crear y luego eliminar un post.

## Ejecución de Pruebas
1. Ubícate en la raíz del proyecto.
2. Ejecuta:
   ```
   python -m pytest --html=report.html --self-contained-html --disable-warnings
   ```
   Esto ejecutará todos los tests UI y API y generará el reporte HTML completo.

## Reportes y Logging
- El reporte HTML se genera como `report.html` en la raíz y muestra:
  - Estado de cada test (OK/FAIL)
  - Descripción detallada de cada caso (docstring)
  - Mensajes de error y logs
  - Capturas de pantalla en caso de fallos UI
- Los logs detallados se guardan en la carpeta `logs` y permiten depuración avanzada.

### Logs (ubicación y comandos útiles)

- **Ubicación del archivo principal de logs:** `logs/test_log.log` (se crea automáticamente y se abre en modo `append`).
- **Ver las últimas N líneas (PowerShell):**
  ```powershell
  Get-Content .\logs\test_log.log -Tail 50
  ```
- **Ver en vivo (tail -f) en PowerShell:**
  ```powershell
  Get-Content .\logs\test_log.log -Wait
  ```
- **Forzar escritura de prueba rápida (fuera de pytest):**
  ```powershell
  python -c "from utils.logger import get_logger; l=get_logger('sanity_test'); l.info('Prueba de escritura al log (sanity_test)')"
  ```
- **Eliminar el archivo de log (reiniciar):**
  ```powershell
  Remove-Item .\logs\test_log.log -Force
  ```
- **Mostrar todos los archivos `test_log.log` en el proyecto (por si se creó en otra ruta):**
  ```powershell
  Get-ChildItem -Path . -Filter test_log.log -Recurse
  ```

Nota: Pytest captura la salida de consola por defecto. Si quieres ver los mensajes de log en tiempo real durante la ejecución de tests, ejecuta Pytest con la opción `-s` o activa `log_cli`:

```powershell
python -m pytest tests\test_api_jsonplaceholder.py -s
python -m pytest tests\test_api_jsonplaceholder.py -o log_cli=true
```

## Pedagogía y Buenas Prácticas
- Todos los tests reflejan flujos reales y validaciones robustas.
- Se utiliza Page Object Model para separar lógica y UI.
- Los tests son independientes y parametrizados.
- La estructura modular facilita el mantenimiento y la extensión.
- Los reportes y logs permiten defensa profesional y revisión clara.

## Consideraciones sobre APIs externas
- Los tests de API usan JSONPlaceholder, una API pública sin autenticación.
- Los resultados pueden variar según la disponibilidad y estado de la API.
- El framework está listo para adaptarse a cualquier API real siguiendo las mejores prácticas.

---

**Estado actual:**
- Todos los tests UI y API pasan correctamente.
- El reporte HTML y los logs se generan y reflejan la ejecución real.
- La documentación está actualizada y alineada con el código y la estructura vigente.

**Listo para entrega y defensa profesional.**