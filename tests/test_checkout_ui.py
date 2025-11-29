"""
CP_UI_003 / CP_UI_004 - Tests de Checkout

Descripción general:
- CP_UI_003 valida un flujo de compra exitoso desde selección hasta confirmación, usando datos y acciones reales de usuario.
- CP_UI_004 valida el manejo de datos incompletos en el formulario de checkout, reflejando el comportamiento esperado ante errores de usuario.

Pedagogía y estructura:
- Demuestra cómo encadenar acciones entre Page Objects (`ProductsPage`, `CartPage`, `CheckoutPage`) para simular flujos completos y reales.
- Muestra verificaciones en distintos puntos del flujo (existencia de mensaje de éxito o error) y cómo validar el estado real de la aplicación.
"""

import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
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
def test_checkout_success(driver):
    """
    CP_UI_003: Flujo de checkout exitoso (flujo real)
    Protocolo:
    1. Login con usuario válido (flujo real de login).
    2. Añadir el primer producto disponible al carrito (sin forzar datos, usando la UI).
    3. Navegar al carrito y proceder al checkout.
    4. Rellenar el formulario con datos válidos y completar la compra.
    5. Verificar que se muestra el mensaje de confirmación real de la aplicación.
    Este test refleja el comportamiento real del usuario y valida el estado final tras la compra.
    """
    logger.info("CP_UI_003: Checkout exitoso")
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    products_page.add_first_product_to_cart()
    products_page.go_to_cart()
    cart_page.click_checkout()
    checkout_page.fill_checkout_info("Violeta", "Alfonso", "1234")
    checkout_page.finish_checkout()
    success_message = checkout_page.get_success_message()
    assert "Thank you for your order!" in success_message, "No se completó el checkout correctamente"


@pytest.mark.ui
def test_checkout_missing_data(driver):
    """
    CP_UI_004: Checkout con datos incompletos (flujo real)
    Protocolo:
    1. Login y flujo hasta la pantalla de checkout.
    2. Enviar el formulario dejando campos obligatorios vacíos (simulando error real de usuario).
    3. Verificar que se muestra el mensaje de error adecuado, como lo haría la aplicación ante datos faltantes.
    Este test valida el manejo real de errores y la robustez del formulario.
    """
    logger.info("CP_UI_004: Checkout con datos incompletos")
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    products_page.add_first_product_to_cart()
    products_page.go_to_cart()
    cart_page.click_checkout()
    checkout_page.fill_checkout_info("Violeta", "", "1234")
    error_message = checkout_page.get_error_message()
    assert error_message is not None and error_message != "", "No se mostró mensaje de error por datos incompletos"
