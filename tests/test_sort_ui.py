"""
CP_UI_005 - Ordenamiento de productos por precio

Descripción:
- Este test valida que la funcionalidad de ordenamiento por precio (de menor a mayor) muestra los productos en el orden correcto, usando el flujo real de la aplicación y datos dinámicos.

Punto pedagógico:
- Enseña cómo automatizar la selección de opciones en un `select` y cómo capturar y procesar datos de la UI (precios), reflejando la interacción real del usuario.
- El test no fuerza datos ni estados, sino que valida el comportamiento esperado de la aplicación tras la acción de ordenamiento.
"""

import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.fixture(scope="function")
def driver():
    """
    Inicializa el navegador (Chrome) para cada test.
    Permite que cada caso sea independiente y refleje el flujo real de usuario.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.ui
def test_sort_products_by_price(driver):
    """
    CP_UI_005: Verificar ordenamiento por precio (flujo real)
    Protocolo:
    1. Login con usuario válido (flujo real de login).
    2. Seleccionar la opción 'Price (low to high)' en el select de ordenamiento (interacción real con la UI).
    3. Extraer los precios mostrados y comprobar que están ordenados ascendentemente (validación real de la UI tras la acción).
    Este test valida el comportamiento esperado de la aplicación ante la acción de ordenamiento, sin forzar datos ni estados.
    """
    logger.info("CP_UI_005: Ordenar productos por precio")
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    # Esperar a que el select de ordenamiento esté presente y sea interactuable
    wait = WebDriverWait(driver, 10)
    sort_select = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "product_sort_container")))
    sort_select.click()
    # Seleccionar la opción 'Price (low to high)'
    option_lohi = wait.until(EC.presence_of_element_located((By.XPATH, "//option[@value='lohi']")))
    option_lohi.click()
    # Esperar a que los precios se actualicen
    wait.until(lambda d: len(d.find_elements(By.CLASS_NAME, "inventory_item_price")) > 0)
    prices = [float(el.text.replace('$','')) for el in driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
    assert prices == sorted(prices), f"Los productos no están ordenados por precio de menor a mayor. Precios: {prices}"
