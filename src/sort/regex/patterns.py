import re

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
  re.compile(r'^photo_\d+@{}-({})-{}'.format(day_pattern, month_number_pattern, complete_year)),
  re.compile(r'^video_\d+@{}-({})-{}'.format(day_pattern, month_number_pattern, complete_year)),
  re.compile(r'^Instasize_{}({}){}'.format(day_pattern, month_number_pattern, abbreviate_year)),
]

exclude_patterns = [
  re.compile(r'^PicsArt_.+'.format()),
  re.compile(r'^FB_IMG_.+'.format())
]
date_file_patterns = [
  re.compile(r'{}({}){}'.format(complete_year, month_number_pattern, day_pattern)),
  re.compile(r'{}\D({})\D{}'.format(complete_year, month_number_pattern, day_pattern)),
  re.compile(r'{}({}){}'.format(abbreviate_year, month_number_pattern, day_pattern)),
  re.compile(r'{}\D({})\D{}'.format(abbreviate_year, month_number_pattern, day_pattern)),
]