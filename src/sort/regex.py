import re

from src.config.config import Config
class RegexMedia:
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
    
    self.date_img_patterns = [
      re.compile(r'{}({}){}'.format(self.complete_year, self.month_number_pattern, self.day_pattern)),
      re.compile(r'{}\D({})\D{}'.format(self.complete_year, self.month_number_pattern, self.day_pattern)),
      re.compile(r'{}({}){}'.format(self.abbreviate_year, self.month_number_pattern, self.day_pattern)),
      re.compile(r'{}\D({})\D{}'.format(self.abbreviate_year, self.month_number_pattern, self.day_pattern)),
    ]

  def extract_date_from_media(self, img_name: str, date):
    # Estrae la data dalla stringa img_name 
    for pattern in self.date_img_patterns:
      match = re.search(pattern, img_name)
      if match:
        year, month, day = match.group(1), match.group(2), match.group(3)
        return [self.get_year(year), month, day]
    return date

  def extract_date_from_folder(self, folder_name: str):
    if Config.get_checkbox_choises('IgnoreFolderSort'):
      return None
    for pattern in self.date_folder_patterns:
      match = re.search(pattern, folder_name)
      if match:
        groups = match.groups()
        if len(groups) == 3:
          return [self.get_year(groups[0]), self.get_month(groups[1]), groups[2]]
        elif len(groups) == 2:
          return [self.get_year(groups[0]), self.get_month(groups[1])]
        elif len(groups) == 1:
          return [self.get_year(groups[0])]
    return None
  
  def get_year(self, y):
    if int(y) < 100:
      y = '19' + y if int(y) > 70 else '20' + y
    return y
  
  def get_month(self, month:str) ->str:
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