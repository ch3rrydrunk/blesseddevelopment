import configparser


class ConfigurationParser:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('cfg/config.ini')
        telegram_data = config['TelegramData']
        self.token = telegram_data['token']
        self.username = telegram_data['username']
