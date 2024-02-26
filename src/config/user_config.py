from configparser import ConfigParser

class ConfigManager:
  """This class remember the preferences the user makes, and save them
  in a file called config.ini. It is a wrapper of the configparser library"""
  def __init__(self):
    self.config_parser = ConfigParser()
    self.read_config()

  def read_config(self):
    """It reads all the configurations present in the file and returns them"""
    self.config_parser.read('config.ini')
    if not self.config_parser.has_section('Preferences'):
      self.config_parser.add_section('Preferences')

  def save_config(self):
    """Save all preferences saved in RAM to the file"""
    with open('config.ini', "w") as configfile:
      self.config_parser.write(configfile)

  def set_preference(self, option, value):
    """it saves a new preference to the file.
    Args:
      option(string): the name of the preference saved
      value(string): the value of the preference
    """
    self.config_parser.set('Preferences', option, value)
    self.save_config()
      
  def has_preference(self, name):
    """it searches the configuration file to see if a certain preference has been saved"""
    return self.config_parser.has_option('Preferences', name)