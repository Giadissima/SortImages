import re
from typing import Optional
from datetime import datetime
from src.sort.regex.patterns import italian_month_dict, italian_month_abbr_dict, english_month_dict, english_month_abbr_dict
class RegexManager:
  current_year = (datetime.now()).year
  minimum_year = 1990

  @staticmethod
  def get_year(y)->Optional[str]:
    """Converts the abbreviate year to a 4-digit year."""
    if int(y) < 100:
      y = '19' + y if int(y) > 90 else '20' + y
      
    if int(y) < RegexManager.minimum_year or int(y) > RegexManager.current_year:
      return None
    return y
  
  def get_month(self, month:str)->str:
    """Converts the months written in letters to numbers."""
    if(not month.isnumeric()):
      if(month in italian_month_dict.keys()):
        month = italian_month_dict[month]
      elif(month in italian_month_abbr_dict.keys()):
        month = italian_month_abbr_dict[month]
      elif(month in english_month_dict.keys()):
        month = english_month_dict[month]
      else:
        month = english_month_abbr_dict[month]
    return month
  
  @staticmethod
  def is_file_a_screenshot(file_name):
    """Find out if a file is a screenshot

    Args:
      file_name (str): the file name

    Returns:
      bool: True if file is a screenshot
    """
    pattern = re.compile(r'Screenshot', re.IGNORECASE)
    if pattern.search(file_name):
      return True
    return False
  
  def get_latest_date(self, dates):
    maxYear = 0
    maxDateObj = []
    
    for date in dates:
      year = int(date[0])
      if year > maxYear:
        maxYear = year
        maxDateObj = date

    return maxDateObj