from src.sort.regex.regex import RegexManager
from typing import List, Optional
from src.sort.regex.patterns import specific_patterns, date_file_patterns, exclude_patterns
import re

class RegexMedia(RegexManager):
  def __init__(self):
    super().__init__()
    
  def extract_date_from_media(self, file_name: str, date: Optional[List[str]])->Optional[List[str]]:
    """Checks among the various patterns if it finds a date contained within the images,
    otherwise, it returns the content of the date parameter

    Args:
      file_name (str)
      date (Optional[List[str]]): The date of the previously extracted folder, which may also be None.

    Returns:
      Optional[List[str]]: file's date if exists, otherwise folder's date, otherwise None
    """
    specific_date = self.search_specific_patten(file_name)
    if specific_date != None and specific_date[0] != None:
      return specific_date
    
    if self.exclude_specific_patterns(file_name): return None
    
    return self.search_common_pattern(file_name, date)
  
  def search_specific_patten(self, file_name:str)->Optional[List[str]]:
    """To make the program more robust to any files that do not follow the conventional
    rules of the date format, this function will check if we have encountered one of
    these cases and resolve it
    Returns:
      None|List[str]
    """
    for pattern in specific_patterns:
      match = re.search(pattern, file_name)
      if match:
        day, month, year = match.group(1), match.group(2), match.group(3)
        print(day, month, year)
        return [RegexManager.get_year(year), month, day]
    return None
  
  def exclude_specific_patterns(self, file_name:str)->bool:
    """This function will check whether we have encountered a pattern to exclude.
    A file should be excluded if it doesn't contain the date in the name,
    but the program might erroneously indicate otherwise.
    Returns:
      bool: True if the file is to be excluded from the regex's searches
    """
    for pattern in exclude_patterns:
      match = re.search(pattern, file_name)
      if match:
        return True
    return False
  
  def search_common_pattern(self, file_name:str, date:str|None)->Optional[List[str]]:
    """search for a generalized pattern in which a format of the type YYYY-MM-DD is searched for
    Args:
      file_name (str): the name of the file
      date (str | None): folder's date previously founded
    Returns:
      Optional[List[str]]: if the date is found, it returns it as a list of strings
    """
    index = 0
    dates = []
    for pattern in date_file_patterns:
      if index == 2 and len(dates) > 0:
        return self.get_latest_date(dates)
      matches = re.findall(pattern, file_name)
      for match in matches:
        year, month, day = match
        date = [RegexManager.get_year(year), month, day]
        if date[0] != None:
          if index >= 2:
            return date
          dates.append(date)
      index+=1
    return date
  
  def is_file_from_facebook(file_name:str)->bool:
    """Find out if a file is from Facebook

    Args:
      file_name (str): the file name

    Returns:
      bool: True if file is from Facebook
    """
    pattern = re.compile(r'^FB_IMG_.+')
    if pattern.search(file_name):
      return True
    return False
  
  def is_file_from_whatsapp(file_name:str)->bool:
    """Find out if a file is from Whatsapp

    Args:
      file_name (str): the file name

    Returns:
      bool: True if file is from Whatsapp
    """
    pattern = re.compile(r'^IMG-\d{8}-WA.+')
    if pattern.search(file_name):
      return True
    return False
  
  @staticmethod
  def is_file_a_screenshot(file_name:str)->bool:
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