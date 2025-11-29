
# Casos de Prueba UI (Selenium)

Todos los casos se implementan en la carpeta `tests/` usando Selenium WebDriver y Page Object Model.

1. **Login parametrizado (test_login_ui.py)**
	- Validar login exitoso y manejo de errores con usuarios reales, bloqueados e inválidos.
	- Usa datos externos y parametrización para cubrir múltiples escenarios.

2. **Añadir y eliminar producto del carrito (test_cart_ui.py)**
	- Agregar un producto al carrito y eliminarlo, validando el estado real tras cada acción.

3. **Checkout exitoso y con datos incompletos (test_checkout_ui.py)**
	- Simular compra exitosa con datos válidos.
	- Validar el manejo de errores al enviar datos incompletos en el formulario de checkout.

4. **Navegación a detalles de producto (test_navigation_ui.py)**
	- Seleccionar un producto desde la lista y verificar que se muestran correctamente sus detalles.

5. **Ordenamiento de productos por precio (test_sort_ui.py)**
	- Seleccionar la opción 'Price (low to high)' y validar que los productos se muestran ordenados ascendentemente.

6. **Estado dinámico del carrito (test_cart_state_ui.py)**
	- Agregar y eliminar productos, verificando que el contador y el estado del carrito se actualizan correctamente tras cada acción.

Todos los casos incluyen validaciones robustas y comentarios pedagógicos en el código.