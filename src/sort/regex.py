import re
from typing import List, Optional
from datetime import datetime
from src.config.config import Config
class RegexMedia:
  current_year = (datetime.now()).year
  minimum_year = 1990
  def __init__(self):
    self.months_italian = r'gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|settembre|ottobre|novembre|dicembre'
    self.months_english = r'January|February|March|April|May|June|July|August|September|October|November|December'
    self.months_abbreviated = r'gen|feb|mar|apr|mag|giu|lug|ago|set|ott|nov|dic|jan|jun|jul|aug|sep|oct|dec'
    self.month_number_pattern = r'0[1-9]|1[0-2]'

    self.month_pattern = r'({}|{}|{}|{})'.format(self.month_number_pattern, self.months_abbreviated, self.months_english, self.months_italian)
    self.day_pattern = r'(0[1-9]|1[0-9]|2[0-9]|30|31)'
    self.complete_year = r'(\d{4})'
    self.abbreviate_year = r'(\d{2})'
    
    self.italian_month_dict = {
      'gennaio':'01',
      'febbraio':'02',
      'marzo':'03',
      'aprile':'04',
      'maggio':'05',
      'giugno':'06',
      'luglio':'07',
      'agosto': '08',
      'settembre':'09',
      'ottobre':'10',
      'novembre':'11',
      'dicembre':'12'
    }
    
    self.english_month_dict = {
      'january':'01',
      'february':'02',
      'march':'03',
      'april':'04',
      'may':'05',
      'june':'06',
      'july':'07',
      'august': '08',
      'september':'09',
      'october':'10',
      'november':'11',
      'december':'12'
    }
    
    self.english_month_abbr_dict = {
      'jan':'01',
      'feb':'02',
      'mar':'03',
      'apr':'04',
      'may':'05',
      'jun':'06',
      'jul':'07',
      'aug': '08',
      'sep':'09',
      'oct':'10',
      'nov':'11',
      'dec':'12'
    }
    
    self.italian_month_abbr_dict = {
      'gen':'01',
      'mag':'05',
      'giu':'06',
      'lug':'07',
      'ago': '08',
      'set':'09',
      'ott':'10',
      'dic':'12'
    }
    
    self.date_folder_patterns = [
      re.compile(r'/{}/{}/{}'.format(self.complete_year, self.month_pattern, self.day_pattern), flags=re.IGNORECASE),
      re.compile(r'/{}/.+/{}/{}'.format(self.complete_year, self.month_pattern, self.day_pattern), flags=re.IGNORECASE),
      re.compile(r'/{}/{}/.+/{}'.format(self.complete_year, self.month_pattern, self.day_pattern), flags=re.IGNORECASE),
      re.compile(r'/{}/.+/{}/.+/{}'.format(self.complete_year, self.month_pattern, self.day_pattern), flags=re.IGNORECASE),
      
      re.compile(r'/{}/{}/{}'.format(self.abbreviate_year, self.month_pattern, self.day_pattern), flags=re.IGNORECASE),
      re.compile(r'/{}/.+/{}/{}'.format(self.abbreviate_year, self.month_pattern, self.day_pattern), flags=re.IGNORECASE),
      re.compile(r'/{}/{}/.+/{}'.format(self.abbreviate_year, self.month_pattern, self.day_pattern), flags=re.IGNORECASE),
      re.compile(r'/{}/.+/{}/.+/{}'.format(self.abbreviate_year, self.month_pattern, self.day_pattern), flags=re.IGNORECASE),
      
      re.compile(r'/{}/{}'.format(self.complete_year, self.month_pattern), flags=re.IGNORECASE),
      re.compile(r'/{}/.+/{}'.format(self.complete_year, self.month_pattern), flags=re.IGNORECASE),
      re.compile(r'/{}/{}'.format(self.abbreviate_year, self.month_pattern), flags=re.IGNORECASE),
      re.compile(r'/{}/.+/{}'.format(self.abbreviate_year, self.month_pattern), flags=re.IGNORECASE),
      re.compile(r'/{}'.format(self.complete_year)),
    ]
    
    self.specific_patterns = {
      "PHOTO": re.compile(r'^photo_\d+@({})-({})-({})'.format(self.day_pattern, self.month_number_pattern, self.complete_year)),
    }
    
    self.exclude_patterns = [
      re.compile(r'^PicsArt_.+'.format())
    ]
    self.date_file_patterns = [
      re.compile(r'{}({}){}'.format(self.complete_year, self.month_number_pattern, self.day_pattern)),
      re.compile(r'{}\D({})\D{}'.format(self.complete_year, self.month_number_pattern, self.day_pattern)),
      re.compile(r'{}({}){}'.format(self.abbreviate_year, self.month_number_pattern, self.day_pattern)),
      re.compile(r'{}\D({})\D{}'.format(self.abbreviate_year, self.month_number_pattern, self.day_pattern)),
    ]

  def extract_date_from_media(self, file_name: str, date: Optional[List[str]])->Optional[List[str]]:
    """Check if there is a date in the file name, and if so, return it.

    Args:
      file_name (str)
      date (Optional[List[str]]): The date of the previously extracted folder, which may also be None.

    Returns:
      Optional[List[str]]: file's date if exists, otherwise None
    """
    specific_date = self.search_specific_patten(file_name) 
    if specific_date != None and specific_date[0] != None: 
      return specific_date
    
    if self.search_exclude_patterns(file_name):
      return None
    
    return self.search_common_patterns(file_name)

  def extract_date_from_folder(self, folder_name: str)->Optional[List[str]]:
    """Check if there is a date in the folder name, and if so, return it

    Args:
      folder_name (str)

    Returns:
      Optional[List[str]]: folder's date if exists, otherwise None
    """
    if Config.get_checkbox_choises('IgnoreFolderSort'):
      return None
    for pattern in self.date_folder_patterns:
      match = re.search(pattern, folder_name)
      if match:
        groups = match.groups()
        if len(groups) == 3:
          return [RegexMedia.get_year(groups[0]), self.get_month(groups[1]), groups[2]]
        elif len(groups) == 2:
          return [RegexMedia.get_year(groups[0]), self.get_month(groups[1])]
        elif len(groups) == 1:
          return [RegexMedia.get_year(groups[0])]
    return None
  
  @staticmethod
  def get_year(y)->Optional[str]:
    """Converts the abbreviate year to a 4-digit year."""
    if int(y) < 100:
      y = '19' + y if int(y) > 90 else '20' + y
      
    if int(y) < RegexMedia.minimum_year or int(y) > RegexMedia.current_year:
      return None
    return y
  
  def get_month(self, month:str)->str:
    """Converts the months written in letters to numbers."""
    if(not month.isnumeric()):
      if(month in self.italian_month_dict.keys()):
        month = self.italian_month_dict[month]
      elif(month in self.italian_month_abbr_dict.keys()):
        month = self.italian_month_abbr_dict[month]
      elif(month in self.english_month_dict.keys()):
        month = self.english_month_dict[month]
      else:
        month = self.english_month_abbr_dict[month]
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
  
  def search_specific_patten(self, file_name):
    """To make the program more robust to any files that do not follow the conventional 
    rules of the date format, this function will check if we have encountered one of 
    these cases and resolve it
    Returns:
      None|List[str]
    """
    match = re.search(self.specific_patterns["PHOTO"], file_name)
    if match:
      day, month, year = match.group(1), match.group(2), match.group(3)
      return [RegexMedia.get_year(year), month, day]
    return None
  
  def search_exclude_patterns(self, file_name):
    for pattern in self.exclude_patterns:
      match = re.search(pattern, file_name)
      if match:
        return True
    return False
  
  def search_common_patterns(self, file_name):
    index = 0
    dates = []
    for pattern in self.date_file_patterns:
      if index == 2 and len(dates) > 0:
        return self.get_latest_date(dates)
      matches = re.findall(pattern, file_name)
      for match in matches:
        year, month, day = match
        date = [RegexMedia.get_year(year), month, day]
        if date[0] != None:
          if index >= 2:
            return date
          dates.append(date)
      index+=1
    return date