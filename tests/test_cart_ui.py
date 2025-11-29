"""
CP_UI_002 - Test de Carrito (añadir y eliminar)

Descripción:
- Valida la funcionalidad real del carrito: agregar un producto y eliminarlo, usando datos y acciones que reflejan el comportamiento del usuario final.

Importancia pedagógica:
- Muestra cómo se orquesta un flujo completo UI usando Page Objects y fixtures.
- Refuerza la idea de pruebas independientes, comprobaciones explícitas y validación de estados reales en la aplicación.
"""

import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.fixture(scope="function")
def driver():
    """
    Inicializa el navegador para cada caso de prueba y lo cierra al finalizar.
    Permite que cada test sea independiente y refleje el flujo real de usuario.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.ui
def test_add_and_remove_product_from_cart(driver):
    """
    CP_UI_002 - Añadir y eliminar producto del carrito (flujo real)
    Protocolo:
    1. Iniciar sesión con usuario válido (flujo real de login).
    2. Añadir el primer producto disponible al carrito (sin forzar datos, usando la UI).
    3. Verificar que el carrito contiene 1 elemento (estado real tras la acción).
    4. Eliminar el producto y verificar que el carrito queda vacío (validación de la funcionalidad de eliminación).
    Este test refleja el comportamiento real del usuario y valida el estado de la aplicación tras cada acción.
    """
    logger.info("CP_UI_002: Añadir y eliminar producto del carrito")
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    products_page.add_first_product_to_cart()
    products_page.go_to_cart()
    assert len(cart_page.get_cart_items()) == 1, "No se añadió el producto al carrito"
    cart_page.remove_first_item()
    assert len(cart_page.get_cart_items()) == 0, "No se eliminó el producto del carrito"
