# src/config/config_manager.py
from configparser import ConfigParser

class ConfigManager:
  def __init__(self):
    self.config_parser = ConfigParser()
    self.read_config()

  def read_config(self):
    self.config_parser.read('config.ini')
    if not self.config_parser.has_section('Preferences'):
      self.config_parser.add_section('Preferences')

  def save_config(self):
    with open('config.ini', "w") as configfile:
      self.config_parser.write(configfile)

  def set_preference(self, option, value):
    self.config_parser.set('Preferences', option, value)
    self.save_config()
      
  def has_preference(self, name):
    return self.config_parser.has_option('Preferences', name)