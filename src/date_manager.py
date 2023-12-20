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
    print(date)
    if len(date) == 1 and date[0] != None: 
      return join(output_folder, date[0])
    elif len(date) == 2 and date[0] != None and date[1] != None: 
      return join(output_folder, date[0], date[1])
    elif len(date) == 3 and date[0] != None and date[1] != None and date[2] != None: 
      return join(output_folder, date[0], date[1], date[2])
    return None