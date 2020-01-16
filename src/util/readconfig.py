from configparser import ConfigParser
import configparser
import os


# Read the properties for the application and environmental configuration.
configprops = {}
Config = ConfigParser()
Config.read(["../resources/environ.properties","../resources/application.properties"])
# a simple function to read an array of configuration files into a config object
def read_config(cfg_files):
    global config
    if(cfg_files != None):
        config = configparser.RawConfigParser()

        # merges all files into a single config
        for i, cfg_file in enumerate(cfg_files):
            if(os.path.exists(cfg_file)):
                config.read(cfg_file, encoding='utf-8')
                #config.read(cfg_file)

        return config

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


