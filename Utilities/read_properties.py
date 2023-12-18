import configparser

# This is used for reading data from ini file
config = configparser.RawConfigParser()

# giving location of config.ini
config.read('.\\Configurations\\config.ini')

class ReadConfig:
    # Now to read from config.ini we need to create method for each variable in config.ini
    # Also create static method if you want to access it directly using class name
    @staticmethod
    def getApplicationurl():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def getUserEmail():
        user_name = config.get('common info', 'username')
        return user_name

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password