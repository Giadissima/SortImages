import re

class RegexMedia:
  def __init__(self):
    self.months_italian = r'(gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|settembre|ottobre|novembre|dicembre)'
    self.months_english = r'(January|February|March|April|May|June|July|August|September|October|November|December)'
    self.months_abbreviated = r'(gen|feb|mar|apr|mag|giu|lug|ago|set|ott|nov|dic|jan|jun|jul|aug|sep|oct|dec)'
    self.month_number_pattern = r'(1[0-2])|(0[1-9])|[1-9]'

    self.month_pattern = r'{}|{}|{}'.format(self.month_number_pattern, self.months_abbreviated, self.months_english, self.months_italian)
    self.year_pattern = r'(19\d{2}|20\d{2}|\d{2})'
    self.day_pattern = r'((0[1-9])|([12][0-9])|3[0-1])'

  def extract_date_from_img(self, img_name: str, date):
    # Estrarre la data dalla stringa img_name
    match = re.search(r'{}.?{}.?{}.*'.format(self.year_pattern, self.month_pattern, self.day_pattern), img_name, re.IGNORECASE)
    if match:
      print(len(match.group()))
      year, month, day = [group for group in match.groups()]
      if(int(year) < 100):
        year = '19' + year if int(year) > 70 else '20' + year
      return [year, month, day]
    return date

  def extract_date_from_folder(self, folder_name: str):
    # TODO farla funzionare anche in caso di "2023/mare/08"
    # ? Caso in cui trova sia anno che mese che giorno
    # TODO this
    match = re.search(r'/{}/.*?{}/.*?{}'.format(self.year_pattern, self.month_pattern, self.day_pattern), folder_name, re.IGNORECASE)
    if match:
      year, month, day = [group for group in match.groups()]
      if int(year) < 100:
          year = '19' + year if int(year) > 70 else '20' + year
      return [year, month, day]

    # ? Caso in cui trova sia anno che mese
    match = re.search(r'.*?/{}/.*?{}'.format(self.year_pattern, self.month_pattern), folder_name, re.IGNORECASE)
    if match:
      year, month= [group for group in match.groups()]
      return [year, month, None]
      
    # ? Caso in cui trova solo l'anno
    match = re.search(r'.*?/{}.*?'.format(self.year_pattern), folder_name)
    if match:
      year, month= [group for group in match.groups()]
      return [year, month, None]
    return None