from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class ProductsPage:
    # Localizadores de elementos de la página de productos
    PRODUCT_ADD_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")  # Botón para agregar productos al carrito
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")  # Icono para acceder al carrito
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")  # Nombre de los productos listados

    def __init__(self, driver: WebDriver):
        """
        Constructor de la Page Object ProductsPage.
        Recibe el WebDriver y lo asocia a la instancia para interactuar con la página de productos.
        """
        self.driver = driver

    def add_first_product_to_cart(self):
        """
        Hace clic en el botón de agregar del primer producto listado.
        Permite validar la funcionalidad de agregar productos al carrito.
        """
        self.driver.find_elements(*self.PRODUCT_ADD_BUTTON)[0].click()

    def go_to_cart(self):
        """
        Hace clic en el icono del carrito para navegar a la página del carrito.
        Permite validar la navegación entre páginas y el acceso al carrito.
        """
        self.driver.find_element(*self.CART_ICON).click()

    def get_first_product_name(self):
        """
        Devuelve el nombre del primer producto listado en la página.
        Útil para validar la correcta visualización y selección de productos.
        """
        return self.driver.find_elements(*self.PRODUCT_NAME)[0].text
