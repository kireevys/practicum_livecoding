from bs4 import BeautifulSoup
import requests

# URL веб-страницы для парсинга
url = "https://example.com"

# Получаем HTML-код страницы
response = requests.get(url)
if not response.ok:
    print("Ошибка при получении HTML-кода страницы")
    exit()

soup = BeautifulSoup(response.content, "html.parser")

# Извлекаем данные
for link in soup.find_all("a", href=True):
    href = link["href"]
    text = link.string
    if text:
        print(f"Текст: {text}, Ссылка: {href}")
