"""
CP_UI_006 - Navegación a detalles de producto

Descripción:
- Verifica que al seleccionar un producto desde la lista se muestran correctamente sus detalles, usando el flujo real de la aplicación y datos dinámicos.

Notas pedagógicas:
- Este test demuestra localización dinámica de elementos (obtener nombre y buscar el enlace por texto), reflejando la interacción real del usuario.
- Ejemplifica interacción directa con el DOM y verificación en `page_source`, validando el estado real de la UI tras la acción.
- El test no fuerza datos ni rutas, sino que navega y valida como lo haría un usuario final.
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
    Inicializa y cierra el navegador por test.
    Permite que cada caso sea independiente y refleje el flujo real de usuario.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.ui
def test_navigate_to_product_details(driver):
    """
    CP_UI_006: Navegar a detalles de producto (flujo real)
    Protocolo:
    1. Login con usuario válido (flujo real de login).
    2. Obtener el nombre del primer producto mostrado (dato dinámico, no forzado).
    3. Hacer clic en el enlace del producto y verificar que sus detalles aparecen en la página (validación real de la UI).
    Este test valida la navegación y visualización de detalles como lo haría un usuario final, sin forzar datos ni rutas.
    """
    logger.info("CP_UI_006: Navegar a detalles de producto")
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    product_name = products_page.get_first_product_name()
    from selenium.webdriver.common.by import By
    product_link = driver.find_element(By.LINK_TEXT, product_name)
    product_link.click()
    assert product_name in driver.page_source, "No se muestran los detalles del producto"
