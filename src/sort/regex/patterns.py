import re

"""
This file contains all the regex lists that can be used to exclude certain file types and to search
for dates within certain file types or paths. Also included are dictionaries useful for regexes, for
example, the dictionary that converts months written alphabetically into numbers
"""
months_italian = r'gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|settembre|ottobre|novembre|dicembre'
months_english = r'January|February|March|April|May|June|July|August|September|October|November|December'
months_abbreviated = r'gen|feb|mar|apr|mag|giu|lug|ago|set|ott|nov|dic|jan|jun|jul|aug|sep|oct|dec'
month_number_pattern = r'0[1-9]|1[0-2]'

month_pattern = r'({}|{}|{}|{})'.format(month_number_pattern, months_abbreviated, months_english, months_italian)
day_pattern = r'(0[1-9]|1[0-9]|2[0-9]|30|31)'
complete_year = r'(\d{4})'
abbreviate_year = r'(\d{2})'

italian_month_dict = {
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

english_month_dict = {
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

english_month_abbr_dict = {
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

italian_month_abbr_dict = {
  'gen':'01',
  'mag':'05',
  'giu':'06',
  'lug':'07',
  'ago': '08',
  'set':'09',
  'ott':'10',
  'dic':'12'
}

date_folder_patterns = [
  re.compile(r'/{}/{}/{}'.format(complete_year, month_pattern, day_pattern), flags=re.IGNORECASE),
  re.compile(r'/{}/.+/{}/{}'.format(complete_year, month_pattern, day_pattern), flags=re.IGNORECASE),
  re.compile(r'/{}/{}/.+/{}'.format(complete_year, month_pattern, day_pattern), flags=re.IGNORECASE),
  re.compile(r'/{}/.+/{}/.+/{}'.format(complete_year, month_pattern, day_pattern), flags=re.IGNORECASE),
  
  re.compile(r'/{}/{}/{}'.format(abbreviate_year, month_pattern, day_pattern), flags=re.IGNORECASE),
  re.compile(r'/{}/.+/{}/{}'.format(abbreviate_year, month_pattern, day_pattern), flags=re.IGNORECASE),
  re.compile(r'/{}/{}/.+/{}'.format(abbreviate_year, month_pattern, day_pattern), flags=re.IGNORECASE),
  re.compile(r'/{}/.+/{}/.+/{}'.format(abbreviate_year, month_pattern, day_pattern), flags=re.IGNORECASE),
  
  re.compile(r'/{}/{}'.format(complete_year, month_pattern), flags=re.IGNORECASE),
  re.compile(r'/{}/.+/{}'.format(complete_year, month_pattern), flags=re.IGNORECASE),
  re.compile(r'/{}/{}'.format(abbreviate_year, month_pattern), flags=re.IGNORECASE),
  re.compile(r'/{}/.+/{}'.format(abbreviate_year, month_pattern), flags=re.IGNORECASE),
  re.compile(r'/{}'.format(complete_year)),
]

specific_patterns = [
  # day-month-year order
  (re.compile(r'^photo_\d+@{}-({})-{}'.format(day_pattern, month_number_pattern, complete_year)), ('day', 'month', 'year')),
  (re.compile(r'^video_\d+@{}-({})-{}'.format(day_pattern, month_number_pattern, complete_year)), ('day', 'month', 'year')),
  (re.compile(r'^{}-({})-{}_\d\d\d\d\.jpg$'.format(day_pattern, month_number_pattern, complete_year)), ('day', 'month', 'year')),
  
  # year-month-day order (e.g. 20131128_150404.jpg, also matches suffixes
  # like 20131128_150404.0.jpg or 20131128_150404(1).jpg since we don't
  # anchor the ending anymore - only the leading date_time is checked)
  (re.compile(r'^{}({}){}_\d{{6}}'.format(complete_year, month_number_pattern, day_pattern)), ('year', 'month', 'day')),
  
  # day-month-abbreviate year order
  (re.compile(r'^Instasize_{}({}){}'.format(day_pattern, month_number_pattern, abbreviate_year)), ('day', 'month', 'year')),
  (re.compile(r'^P{}-({})-{}_.+'.format(day_pattern, month_number_pattern, abbreviate_year)), ('day', 'month', 'year')),
]

exclude_patterns = [
  re.compile(r'^PicsArt_.+'),
  re.compile(r'^FB_IMG_.+'),
  re.compile(r'^received_+'),
]

date_file_patterns = [
  # (pattern, group_order, has_separators, year_is_full) - has_separators marks patterns
  # where the day/month/year are delimited by non-digit characters, which are far less
  # likely to match a coincidental run of digits (like a time or serial number) than a
  # pattern that just concatenates digits with no delimiter. year_is_full marks patterns
  # with an explicit 4-digit year, which is far less ambiguous than a 2-digit one (e.g. an
  # abbreviated year can easily collide with an hour/minute/second from a timestamp).

  # day-month-year order
  (re.compile(r'{}-({})-{}'.format(day_pattern, month_number_pattern, complete_year)), ('day', 'month', 'year'), True, True),

  # year-month-day order
  (re.compile(r'{}({}){}'.format(complete_year, month_number_pattern, day_pattern)), ('year', 'month', 'day'), False, True),
  (re.compile(r'{}\D({})\D{}'.format(complete_year, month_number_pattern, day_pattern)), ('year', 'month', 'day'), True, True),
  (re.compile(r'{}({}){}'.format(abbreviate_year, month_number_pattern, day_pattern)), ('year', 'month', 'day'), False, False),
  (re.compile(r'{}\D({})\D{}'.format(abbreviate_year, month_number_pattern, day_pattern)), ('year', 'month', 'day'), True, False),
]