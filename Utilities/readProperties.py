import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getURL():
        base_url = config.get('common info', 'url')
        return base_url