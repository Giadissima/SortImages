from typing import Union
from os.path import join
from src.config.config import Config

class DateManager():
  @staticmethod
  def get_date_path(date, output_folder)->Union[str,None]:
    """Check for items containing dates and concatenate the contents..
      Args:
        date (List[str]): a list of three elements containing: year, month, day
      Returns:
        str|None: The new file path"""
    dest_folder = output_folder
    if(Config.get_checkbox_choises("ScreenshotFolder")): 
      dest_folder = join(dest_folder, "Screenshot") # TODO spostarli se c'è screenshot nel nome
    if len(date) == 1 and date[0] != None:
      return join(dest_folder, date[0])
    elif len(date) == 2 and date[0] != None and date[1] != None: 
      if Config.get_sort_method("Year"):
        return join(dest_folder, date[0]) 
      return join(dest_folder, date[0], date[1])
    elif len(date) == 3 and date[0] != None and date[1] != None and date[2] != None: 
      if Config.get_sort_method("Year"):
        return join(dest_folder, date[0])
      elif Config.get_sort_method("YearMonth"):
        return join(dest_folder, date[0], date[1])
      return join(dest_folder, date[0], date[1], date[2])
    return None