from typing import List, Union
from os.path import join
from src.config.config import Config
from src.sort.regex.regex_path import RegexPath
from src.sort.regex.regex_media import RegexMedia

class PathManager():
  def __init__(self):
    self.output_folder = Config.output_folder
    
  def get_date_path(self, date:List[str], output_folder:str)->Union[str,None]:
    """This function returns the new destination folder containing the possible path of the previously found date.
      Args:
        date (List[str]): a list of three elements containing: year, month, day
        output_folder: it is the initial destination folder for the images
      Returns:
        str: The new file path"""
    if date == None: return output_folder
    if len(date) == 1 and date[0] != None:
      return join(output_folder, date[0])
    elif len(date) == 2 and date[0] != None and date[1] != None:
      if Config.get_sort_method("Year"):
        return join(output_folder, date[0])
      return join(output_folder, date[0], date[1])
    elif len(date) == 3 and date[0] != None and date[1] != None and date[2] != None:
      if Config.get_sort_method("Year"):
        return join(output_folder, date[0])
      elif Config.get_sort_method("YearMonth"):
        return join(output_folder, date[0], date[1])
      return join(output_folder, date[0], date[1], date[2])
    return output_folder
  
  def get_output_path(self, input_folder:str, file_name:str)->str:
    """It performs checks on the path and file name to determine whether
    folder concatenation is required, such as WhatsApp, Facebook, and Screenshot.
    Returns:
      str: The new file path"""
    self.output_folder = Config.output_folder
    if Config.get_checkbox_choises("ScreenshotFolder") and RegexMedia.is_file_a_screenshot(file_name):
      self.output_folder = join(self.output_folder, "Screenshot")
    elif RegexMedia.is_file_from_facebook(file_name):
      self.output_folder = join(self.output_folder, "Facebook")
    elif RegexPath.is_facebook_path(input_folder):
      self.output_folder = join(self.output_folder, "Facebook")
    elif not Config.get_checkbox_choises("WhatsappFolder") and RegexMedia.is_file_from_whatsapp(file_name):
      self.output_folder = join(self.output_folder, "Whatsapp")
    elif not Config.get_checkbox_choises("WhatsappFolder") and RegexPath.is_whatsapp_path(input_folder):
      self.output_folder = join(self.output_folder, "Whatsapp")
    return self.output_folder