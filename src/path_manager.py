from typing import Union
from os.path import join
from src.config.config import Config
from src.sort.regex.regex_path import RegexPath
from src.sort.regex.regex_file import RegexMedia

class PathManager():
  def __init__(self):
    self.output_folder = Config.output_folder
    
  def get_date_path(self, date, output_folder)->Union[str,None]:
    """Check for items containing dates and concatenate the contents..
      Args:
        date (List[str]): a list of three elements containing: year, month, day
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
  
  def get_output_path(self, input_folder, file_name):
    self.output_folder = Config.output_folder
    if Config.get_checkbox_choises("ScreenshotFolder") and RegexMedia.is_file_a_screenshot(file_name): 
      self.output_folder = join(self.output_folder, "Screenshot")
    elif RegexMedia.is_file_from_facebook(file_name):
      self.output_folder = join(self.output_folder, "Facebook")
    elif RegexPath.is_facebook_path(input_folder):
      self.output_folder = join(self.output_folder, "Facebook")
    return self.output_folder