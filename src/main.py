import json
from utils.loader import Loader
from utils.parser import Parser
from settings import Settings

def main():
    # Загрузка конфигурации
    with open('config.json', 'r') as f:
        config = json.load(f)

    # Инициализация настроек
    settings = Settings(config)

    # Загрузка данных
    loader = Loader()
    csv_data = loader.load(settings.google_sheet_link)

    # Парсинг данных
    parser = Parser()
    parsed_data = parser.parse(csv_data)

    # Вывод результатов
    for email, words in parsed_data:
        print(f"Email: {email}, Words: {words}")

if __name__ == "__main__":
    main()
