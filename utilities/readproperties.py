import configparser

config = configparser.RawConfigParser()
config.read("..\\configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def getUserPhone():
        username = config.get('common info', 'user_phone')
        return username

    @staticmethod
    def getEmail():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getEnv():
        env = config.get('common info', 'env')
        return env

    @staticmethod
    def add_min_sleep():
        password = config.get('common info', 'min_wait')
        return password

    @staticmethod
    def add_max_sleep():
        password = config.get('common info', 'max_wait')
        return password
