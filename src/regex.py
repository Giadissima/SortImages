import re

class RegexMedia:

	def check_regex(self, text: str):
		"""Controlla i vari formati della stringa text

		Args:
			text (str): il testo da matchare (il filename)

		Returns:
			None | [int, int, int]: Returns None if any formats match, otherwise 
			it returns the date extrapolated ([YYYY, MM, DD]).
		"""
		# Estrae la data tramite regex
		return self.extract_date(text)


	def extract_date(self, text: str):
		# Estrarre la data dalla stringa text
		match = re.search(r'.*?(\d{4}).*?(\d{2}).*?(\d{2}).*', text)
		if match:
			year, month, day = [group for group in match.groups()]
			return [year, month, day]
		
		match = re.search(r'.*?(\d{2}).*?(\d{2}).*?(\d{2}).*', text)
		# TODO controllare la data se è valida (2 cifra + 2 opzionali)
		if match:
			year, month, day = [group for group in match.groups()]
			year = '19' + year if int(year) > 70 else '20' + year
			return [year, month, day]
		# TODO togliere none e vedere come spostarle
		return None
