from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CartPage:
    # Localizadores de elementos de la página del carrito
    CHECKOUT_BUTTON = (By.ID, "checkout")  # Botón para iniciar el proceso de checkout
    CART_ITEMS = (By.CLASS_NAME, "cart_item")  # Elementos que representan productos en el carrito
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button.cart_button")  # Botón para eliminar productos

    def __init__(self, driver: WebDriver):
        """
        Constructor de la Page Object CartPage.
        Recibe el WebDriver y lo asocia a la instancia para interactuar con la página.
        """
        self.driver = driver

    def get_cart_items(self):
        """
        Devuelve una lista de elementos que representan los productos en el carrito.
        Permite validar la cantidad y el contenido del carrito.
        """
        return self.driver.find_elements(*self.CART_ITEMS)

    def click_checkout(self):
        """
        Hace clic en el botón de checkout para iniciar el proceso de compra.
        Es el paso previo para la validación del flujo de compra.
        """
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def remove_first_item(self):
        """
        Elimina el primer producto del carrito haciendo clic en el botón correspondiente.
        Útil para validar la funcionalidad de eliminación de productos.
        """
        self.driver.find_element(*self.REMOVE_BUTTON).click()
