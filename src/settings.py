class Settings:
    """
    Класс Settings загружает настройки из конфигурационного файла.
    """

    def __init__(self, config):
        self.google_sheet_link = config.get('google_sheet_link')

    def __repr__(self):
        return f"Settings(google_sheet_link={self.google_sheet_link})"
