import configparser

config = configparser.RawConfigParser()
config.read("..\\configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common_info', 'base_url')
        return url

    @staticmethod
    def getUserPhone():
        username = config.get('common_info', 'user_phone')
        return username

    @staticmethod
    def getEmail():
        email = config.get('common_info', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('common_info', 'password')
        return password

    @staticmethod
    def getEnv():
        env = config.get('common_info', 'env')
        return env

    @staticmethod
    def add_min_sleep():
        password = config.get('common_info', 'min_wait')
        return password

    @staticmethod
    def add_max_sleep():
        password = config.get('common_info', 'max_wait')
        return password
