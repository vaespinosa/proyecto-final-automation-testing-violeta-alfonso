"""
Archivo: tests/test_api_jsonplaceholder.py
Framework: Pytest + Requests
API: JSONPlaceholder (https://jsonplaceholder.typicode.com)
Consigna: 5 tests defendibles, cubriendo GET, POST, DELETE y flujo encadenado, con comentarios pedagógicos.
"""

import pytest
import requests
from utils.logger import get_logger

BASE_URL = "https://jsonplaceholder.typicode.com"
logger = get_logger(__name__)

# Test 1: GET /posts - Validar respuesta y estructura
def test_get_posts():
    logger.info("[API] Iniciando test: GET /posts")
    response = requests.get(f"{BASE_URL}/posts")
    logger.info(f"[API] Status code recibido: {response.status_code}")
    assert response.status_code == 200, "El endpoint /posts debe responder 200 OK"
    posts = response.json()
    logger.info(f"[API] Total de posts recibidos: {len(posts)}")
    assert isinstance(posts, list), "La respuesta debe ser una lista de posts"
    assert len(posts) > 0, "Debe haber al menos un post disponible"
    assert all("id" in post and "title" in post for post in posts), "Cada post debe tener 'id' y 'title'"

# Test 2: GET /users/1 - Validar datos de usuario
def test_get_user_by_id():
    logger.info("[API] Iniciando test: GET /users/1")
    response = requests.get(f"{BASE_URL}/users/1")
    logger.info(f"[API] Status code recibido: {response.status_code}")
    assert response.status_code == 200, "El endpoint /users/1 debe responder 200 OK"
    user = response.json()
    logger.info(f"[API] Usuario recibido: {user}")
    assert user["id"] == 1, "El id del usuario debe ser 1"
    assert "username" in user and "email" in user, "El usuario debe tener 'username' y 'email'"

# Test 3: POST /posts - Crear un nuevo post
def test_create_post():
    logger.info("[API] Iniciando test: POST /posts")
    payload = {"title": "Test Post", "body": "Contenido de prueba", "userId": 1}
    logger.info(f"[API] Payload enviado: {payload}")
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    logger.info(f"[API] Status code recibido: {response.status_code}")
    assert response.status_code == 201, "El endpoint /posts debe responder 201 Created"
    post = response.json()
    logger.info(f"[API] Post creado: {post}")
    assert post["title"] == payload["title"], "El título debe coincidir"
    assert post["body"] == payload["body"], "El cuerpo debe coincidir"
    assert post["userId"] == payload["userId"], "El userId debe coincidir"

# Test 4: DELETE /posts/1 - Eliminar un post
def test_delete_post():
    logger.info("[API] Iniciando test: DELETE /posts/1")
    response = requests.delete(f"{BASE_URL}/posts/1")
    logger.info(f"[API] Status code recibido: {response.status_code}")
    assert response.status_code in [200, 204], "El endpoint /posts/1 debe responder 200 OK o 204 No Content"

# Test 5: Flujo encadenado - Crear y luego eliminar un post
def test_create_and_delete_post():
    logger.info("[API] Iniciando test: Flujo POST y DELETE")
    payload = {"title": "Post para eliminar", "body": "Contenido temporal", "userId": 1}
    logger.info(f"[API] Payload enviado: {payload}")
    create_resp = requests.post(f"{BASE_URL}/posts", json=payload)
    logger.info(f"[API] Status code creación: {create_resp.status_code}")
    assert create_resp.status_code == 201, "Creación debe responder 201 Created"
    post_id = create_resp.json().get("id")
    logger.info(f"[API] ID del post creado: {post_id}")
    assert post_id is not None, "La respuesta debe contener el id del nuevo post"
    delete_resp = requests.delete(f"{BASE_URL}/posts/{post_id}")
    logger.info(f"[API] Status code borrado: {delete_resp.status_code}")
    assert delete_resp.status_code in [200, 204], "El borrado debe responder 200 OK o 204 No Content"
