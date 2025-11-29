"""
CP_UI_008 - Estado dinámico del carrito

Descripción:
- Este test valida el comportamiento real del carrito al agregar y eliminar productos, verificando que el contador y el estado del carrito se actualizan correctamente.
- Refleja el flujo de usuario final y la interacción con la UI, defendible y relevante para cualquier aplicación de e-commerce.

Puntos pedagógicos:
- Demuestra cómo automatizar la verificación de estados dinámicos en la UI.
- Refuerza la importancia de validar la actualización visual y lógica tras acciones del usuario.
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
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.ui
def test_cart_dynamic_state(driver):
    """
    CP_UI_008: Validar estado dinámico del carrito
    Protocolo:
    1. Login con usuario válido.
    2. Agregar dos productos al carrito.
    3. Verificar que el contador del carrito muestra '2'.
    4. Eliminar un producto y verificar que el contador muestra '1'.
    5. Eliminar el último producto y verificar que el carrito queda vacío.
    """
    logger.info("CP_UI_008: Estado dinámico del carrito")
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    from selenium.webdriver.common.by import By
    add_buttons = driver.find_elements(By.CSS_SELECTOR, "button.btn_inventory")
    add_buttons[0].click()
    add_buttons[1].click()
    # Verificar contador del carrito
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_count_text = cart_icon.text
    cart_count = int(cart_count_text) if cart_count_text.isdigit() else 0
    assert cart_count == 2, f"El contador del carrito debería ser 2, pero es {cart_count}"
    # Ir al carrito y eliminar un producto
    products_page.go_to_cart()
    cart_page.remove_first_item()
    # Verificar cantidad de productos en el carrito
    updated_items = cart_page.get_cart_items()
    assert len(updated_items) == 1, f"El carrito debería tener 1 producto tras eliminar uno, pero tiene {len(updated_items)}"
    # Eliminar el último producto
    cart_page.remove_first_item()
    final_items = cart_page.get_cart_items()
    assert len(final_items) == 0, f"El carrito debería estar vacío, pero tiene {len(final_items)}"
