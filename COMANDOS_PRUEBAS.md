# Comandos para ejecutar pruebas del framework

Este documento describe los comandos necesarios para ejecutar los tests del proyecto en cualquier máquina, por ejemplo, al clonar desde GitHub.

## 1. Instalación de dependencias

En la raíz del proyecto, ejecuta:
```bash
pip install -r requirements.txt
```
Si no existe `requirements.txt`, instala manualmente:
```bash
pip install selenium requests pytest pytest-html
```

## 2. Ejecutar todas las pruebas (UI y API)

```bash
python -m pytest tests --html=report.html --self-contained-html --disable-warnings
```
Esto ejecuta todos los tests y genera el reporte HTML.

## 3. Ejecutar solo pruebas de UI

```bash
python -m pytest tests/test_login_ui.py tests/test_cart_ui.py tests/test_checkout_ui.py tests/test_navigation_ui.py tests/test_sort_ui.py tests/test_cart_state_ui.py --html=report_ui.html --self-contained-html --disable-warnings
```

## 4. Ejecutar solo pruebas de API

```bash
python -m pytest tests/test_api_jsonplaceholder.py --html=report_api.html --self-contained-html --disable-warnings
```

## 5. Ejecutar un test específico

Ejemplo (solo el test de login):
```bash
python -m pytest tests/test_login_ui.py --html=report_login.html --self-contained-html --disable-warnings
```

## 6. Ver el reporte

Abre el archivo `report.html` (o el que corresponda) en tu navegador para ver los resultados.

---

**Notas:**
- Todos los comandos deben ejecutarse en la raíz del proyecto.
- Si usas otro navegador, asegúrate de tener el driver correspondiente instalado.
- Los tests de UI requieren acceso a la web y pueden abrir ventanas del navegador.
- Los tests de API usan la API pública JSONPlaceholder.

**Listo para ejecutar y revisar!**
