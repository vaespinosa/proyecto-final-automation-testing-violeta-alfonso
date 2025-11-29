from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    # Localizadores y URL de la página de login
    URL = "https://www.saucedemo.com/"  # URL de la página de autenticación
    USERNAME_INPUT = (By.ID, "user-name")  # Campo para el nombre de usuario
    PASSWORD_INPUT = (By.ID, "password")  # Campo para la contraseña
    LOGIN_BUTTON = (By.ID, "login-button")  # Botón para iniciar sesión
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")  # Mensaje de error en login

    def __init__(self, driver: WebDriver):
        """
        Constructor de la Page Object LoginPage.
        Recibe el WebDriver y lo asocia a la instancia para interactuar con la página de login.
        """
        self.driver = driver

    def open(self):
        """
        Abre la página de login en el navegador.
        Permite iniciar el flujo de autenticación desde la URL base.
        """
        self.driver.get(self.URL)

    def login(self, username, password):
        """
        Completa los campos de usuario y contraseña y hace clic en el botón de login.
        Permite validar el acceso con diferentes credenciales.
        """
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        """
        Devuelve el mensaje de error si el login falla (por credenciales incorrectas o bloqueo).
        Si no hay error, retorna None. Permite validar la gestión de errores en la autenticación.
        """
        try:
            return self.driver.find_element(*self.ERROR_MESSAGE).text
        except Exception:
            return None
