import requests

class Loader:
    """
    Класс Loader предназначен для загрузки данных из Google таблицы.
    """

    def load(self, link):
        """
        Метод загружает данные из Google таблицы по указанной ссылке.

        :param link: str, ссылка на Google таблицу
        :return: str, содержимое таблицы в формате CSV
        """
        response = requests.get(link)
        if response.status_code == 200:
            return response.text
        else:
            response.raise_for_status()
