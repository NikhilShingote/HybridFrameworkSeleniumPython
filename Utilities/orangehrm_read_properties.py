import configparser

config = configparser.RawConfigParser()

config.read('.\\Configurations\\confighrm.ini')


class ReadConfigHRM:

    @staticmethod
    def read_orangehrm_url():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def getUsername():
        Username = config.get('common info', 'username')
        return Username

    @staticmethod
    def getPassword():
        passwrd = config.get('common info', 'password')
        return passwrd
