from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CheckoutPage:
    # Localizadores de elementos de la página de checkout
    FIRST_NAME_INPUT = (By.ID, "first-name")  # Campo para el nombre
    LAST_NAME_INPUT = (By.ID, "last-name")  # Campo para el apellido
    POSTAL_CODE_INPUT = (By.ID, "postal-code")  # Campo para el código postal
    CONTINUE_BUTTON = (By.ID, "continue")  # Botón para continuar con el checkout
    FINISH_BUTTON = (By.ID, "finish")  # Botón para finalizar la compra
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")  # Mensaje de éxito tras finalizar
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")  # Mensaje de error en el formulario

    def __init__(self, driver: WebDriver):
        """
        Constructor de la Page Object CheckoutPage.
        Recibe el WebDriver y lo asocia a la instancia para interactuar con la página de checkout.
        """
        self.driver = driver

    def fill_checkout_info(self, first_name, last_name, postal_code):
        """
        Completa el formulario de checkout con los datos recibidos y avanza al siguiente paso.
        Permite validar el flujo de compra y la gestión de datos obligatorios.
        """
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def finish_checkout(self):
        """
        Hace clic en el botón de finalizar para completar la compra.
        Permite validar el cierre exitoso del proceso de checkout.
        """
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def get_success_message(self):
        """
        Devuelve el texto del mensaje de éxito tras finalizar la compra.
        Útil para validar que el proceso se completó correctamente.
        """
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text

    def get_error_message(self):
        """
        Devuelve el mensaje de error si el formulario de checkout falla (por datos faltantes o inválidos).
        Si no hay error, retorna None. Permite validar la gestión de errores en el flujo de compra.
        """
        try:
            return self.driver.find_element(*self.ERROR_MESSAGE).text
        except Exception:
            return None
