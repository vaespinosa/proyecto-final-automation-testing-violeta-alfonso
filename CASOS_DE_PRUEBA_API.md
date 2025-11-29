
# Casos de Prueba API (JSONPlaceholder)

Todos los casos se implementan en `tests/test_api_jsonplaceholder.py` usando la API pública JSONPlaceholder.

1. **GET /posts**
	- Validar que la respuesta sea 200 OK.
	- Verificar que la estructura sea una lista de posts.
	- Comprobar que cada post tiene los campos 'id' y 'title'.

2. **GET /users/1**
	- Validar que la respuesta sea 200 OK.
	- Verificar que el usuario con id=1 existe.
	- Comprobar que tiene los campos 'username' y 'email'.

3. **POST /posts**
	- Crear un nuevo post con datos de prueba.
	- Validar que la respuesta sea 201 Created.
	- Comprobar que los datos enviados coinciden con los recibidos.

4. **DELETE /posts/1**
	- Eliminar el post con id=1.
	- Validar que la respuesta sea 200 OK o 204 No Content.

5. **Flujo encadenado: Crear y eliminar un post**
	- Crear un post y obtener su id.
	- Eliminar el post recién creado.
	- Validar ambos pasos y las respuestas correspondientes.

Todos los casos incluyen validaciones robustas y comentarios pedagógicos en el código.