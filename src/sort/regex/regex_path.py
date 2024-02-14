from src.sort.regex.regex import RegexManager
from typing import List, Optional
from src.config.config import Config
from src.sort.regex.patterns import date_folder_patterns
import re

class RegexPath(RegexManager):
  def __init__(self):
    super().__init__()
    
  def extract_date_from_folder(self, folder_name: str)->Optional[List[str]]:
    """Check if there is a date in the folder name, and if so, return it

    Args:
      folder_name (str)

    Returns:
      Optional[List[str]]: folder's date if exists, otherwise None
    """
    if Config.get_checkbox_choises('IgnoreFolderSort'):
      return None
    for pattern in date_folder_patterns:
      match = re.search(pattern, folder_name)
      if match:
        groups = match.groups()
        if len(groups) == 3:
          return [RegexManager.get_year(groups[0]), self.get_month(groups[1]), groups[2]]
        elif len(groups) == 2:
          return [RegexManager.get_year(groups[0]), self.get_month(groups[1])]
        elif len(groups) == 1:
          return [RegexManager.get_year(groups[0])]
    return None
  
  def is_facebook_path(input_path:str)->bool:
    """Find out if a path contains 'Facebook' name

    Args:
      input_path (str): the path_to_check

    Returns:
      bool: True if path contains 'Facebook' name
    """
    pattern = re.compile(r'Facebook', re.IGNORECASE)
    if pattern.search(input_path):
      return True
    return False
  
  def is_whatsapp_path(input_path:str)->bool:
    """Find out if a path contains 'whatsapp' name

    Args:
      input_path (str): the path_to_check

    Returns:
      bool: True if path contains 'whatsapp' name
    """
    pattern = re.compile(r'whatsapp', re.IGNORECASE)
    if pattern.search(input_path):
      return True
    return False