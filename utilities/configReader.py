from configparser import ConfigParser

def readConfig(section, value):
    confReader=ConfigParser()
    confReader.read('..//configuration_data//conf.ini')
    return confReader.get(section, value)
