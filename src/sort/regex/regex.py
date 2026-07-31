from typing import List, Optional, Tuple
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
  def is_valid_calendar_date(year:str, month:str, day:str)->bool:
    """Check that the extracted numbers actually form a real calendar date
    (e.g. rejects things like day 30 of February)."""
    try:
      datetime(int(year), int(month), int(day))
      return True
    except (ValueError, TypeError):
      return False

  def choose_best_date(self, candidates:List[Tuple[List[str], bool, bool]])-> List[str]:
    """Among the various matches that a file name may have generated, picks
    the most trustworthy one instead of just the one with the largest year:
    a bare run of digits (e.g. a time or serial number) can coincidentally
    look like a valid, even more recent, date - so those are only used as a
    last resort, after calendar-invalid matches are discarded. Preference
    order: matches with explicit separators (e.g. 2013-11-28) over ones
    without, then matches with a full 4-digit year over an abbreviated
    2-digit one (an abbreviated year can easily collide with an hour,
    minute or second from a timestamp elsewhere in the name), and only
    then the largest year as a last-resort tie-break.

    Args:
      candidates (List[Tuple[List[str], bool, bool]]): list of
        (date, has_separators, year_is_full) triples

    Returns:
      List[str]: the chosen [year, month, day], or an empty list if none are valid"""
    valid = [(date, has_separators, year_is_full) for date, has_separators, year_is_full in candidates
             if RegexManager.is_valid_calendar_date(date[0], date[1], date[2])]
    if not valid:
      return []

    separated = [(date, year_is_full) for date, has_separators, year_is_full in valid if has_separators]
    pool = separated if separated else [(date, year_is_full) for date, _, year_is_full in valid]

    full_year = [date for date, year_is_full in pool if year_is_full]
    pool = full_year if full_year else [date for date, _ in pool]

    return max(pool, key=lambda date: int(date[0]))