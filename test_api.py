# test_api.py
import requests

def test_get_posts():
    # URL для получения списка постов
    url = "https://jsonplaceholder.typicode.com/posts"

    # Выполняем GET-запрос
    response = requests.get(url)

    # Проверяем код ответа
    assert response.status_code == 200, f"Ожидается код ответа 200, 
получено {response.status_code}"

    # Проверяем, что в ответе есть данные
    assert len(response.json()) > 0, "Ответ не содержит данных"

