import csv

class Parser:
    """
    Класс Parser предназначен для парсинга данных, загруженных из Google таблицы.
    """

    def parse(self, data):
        """
        Метод парсит данные из строки CSV и возвращает список пар (почта, список слов).

        :param data: str, содержимое таблицы в формате CSV
        :return: list of tuples, где каждый элемент - это кортеж (почта, список слов)
        """
        parsed_data = []
        reader = csv.DictReader(data.splitlines())

        for row in reader:
            mail = row.get('mail')
            words = row.get('words')
            if words:
                words_list = [word.strip() for word in words.replace(';', ',').split(',')]
                parsed_data.append((mail, words_list))

        return parsed_data
