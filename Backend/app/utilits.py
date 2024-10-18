from fastapi import Request, Response
from typing import Any


def universal_key_builder(
    func: Any,
    namespace: str = "",
    request: Request = None,
    response: Response = None,
    *args,
    **kwargs
):
    # Собираем ключ из метода запроса, пути и параметров запроса (query и path params)
    query_params = repr(sorted(request.query_params.items())) if request.query_params else ""
    path_params = ":".join(str(value) for key, value in request.path_params.items())

    return ":".join(filter(None, [
        namespace,
        request.method.lower(),  # Метод запроса
        request.url.path,  # Путь запроса
        query_params,  # Параметры запроса
        path_params  # Параметры пути (например, идентификаторы)
    ]))