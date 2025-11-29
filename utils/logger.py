import logging
import os


# Directorio de logs (resuelto a ruta absoluta)
LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs'))
os.makedirs(LOG_DIR, exist_ok=True)

# Nombre de archivo fijo para los logs
log_file = os.path.join(LOG_DIR, 'test_log.log')


def get_logger(name: str) -> logging.Logger:
    """Devuelve un logger configurado.

    Asegura que exista un FileHandler apuntando a `logs/test_log.log` incluso
    si existen otros handlers en la jerarquía (por ejemplo, los que configura
    Pytest). Evita añadir handlers duplicados.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

    # Añadir FileHandler si no existe uno
    has_file = any(isinstance(h, logging.FileHandler) for h in logger.handlers)
    if not has_file:
        try:
            file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
            file_handler.setFormatter(formatter)
            file_handler.setLevel(logging.INFO)
            logger.addHandler(file_handler)
        except Exception:
            # No fallamos si por alguna razón no se puede crear el FileHandler
            pass

    # Añadir StreamHandler si no existe (útil para ver mensajes en consola)
    has_stream = any(isinstance(h, logging.StreamHandler) for h in logger.handlers)
    if not has_stream:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(logging.INFO)
        logger.addHandler(stream_handler)

    return logger
