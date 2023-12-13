from typing import Union
from os.path import join

class DateManager():
  @staticmethod
  def get_date_path(date, output_folder)->Union[str,None]:
    """Check for items containing dates and concatenate the contents..
      Args:
        date (List[str]): a list of three elements containing: year, month, day
      Returns:
        str|None: The new file path"""
    if date[1] == None: 
      return join(output_folder, date[0])
    elif date[2] == None: 
      return join(output_folder, date[0], date[1])
    else: 
      return join(output_folder, date[0], date[1], date[2])