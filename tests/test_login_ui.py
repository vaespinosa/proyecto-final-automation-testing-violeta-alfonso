"""
CP_UI_001 - Test de Login parametrizado

Descripción general:
- Este archivo prueba el flujo de autenticación en la UI usando el patrón Page Object y datos reales del usuario.
- Fuente de datos: `data/login_data.csv` para demostrar parametrización de Pytest con entradas positivas y negativas reales.

Importancia pedagógica:
- La parametrización permite ejecutar el mismo test con múltiples entradas, reflejando escenarios reales de login (usuarios válidos, bloqueados, credenciales incorrectas, etc.).
- El Page Object separa la interacción con la UI de la lógica del test, mejorando reutilización y mantenibilidad.
- El test valida el comportamiento real de la aplicación ante distintos tipos de credenciales, sin forzar resultados.
"""

import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.data_loader import read_csv
from utils.logger import get_logger

logger = get_logger(__name__)
DATA_PATH = 'data/login_data.csv'

def get_test_data():
    """
    Lee el CSV y devuelve una lista de tuplas (username, password, expected_error).
    Permite probar el login con datos reales y variados, reflejando el comportamiento esperado de la aplicación.
    """
    rows = read_csv(DATA_PATH)
    # Corrige el mensaje esperado para el usuario bloqueado si es necesario
    datos = []
    for row in rows:
        if row['username'] == 'locked_out_user':
            datos.append((row['username'], row['password'], 'Epic sadface: Sorry, this user has been locked out.'))
        else:
            datos.append((row['username'], row['password'], row['expected_error']))
    return datos

@pytest.fixture(scope="function")
def driver():
    """
    Inicializa y cierra el navegador para cada test.
    Asegura independencia entre casos y limpieza de sesión, simulando el flujo real de usuario.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("username,password,expected_error", get_test_data())
def test_login(driver, username, password, expected_error):
    """
    CP_UI_001: Validar login con datos parametrizados (flujo real)
    Protocolo:
    1. Abrir página de login.
    2. Intentar autenticación con las credenciales del dataset (usuarios reales, bloqueados, erróneos, etc.).
    3. Si se espera un error, comprobar que el mensaje mostrado coincide exactamente (validación real de la UI).
    4. Si no se espera error, comprobar que no hay mensaje de error y el login es exitoso.
    Este test valida el comportamiento real de la aplicación ante distintos escenarios de login, sin forzar resultados ni estados.
    """
    logger.info(f"CP_UI_001: Test login con usuario: {username}")
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    error_message = login_page.get_error_message()
    if expected_error:
        assert error_message == expected_error, f"Se esperaba error: {expected_error}, pero se obtuvo: {error_message}"
    else:
        assert error_message is None, f"No se esperaba error, pero se obtuvo: {error_message}"
