import re
from src.data.images_patterns import IMAGE_FORMATS
from src.data.video_patterns import VIDEO_FORMATS
import re

class RegexMedia:
	def __init__(self):
		self.image_formats = IMAGE_FORMATS

		self.video_formats = VIDEO_FORMATS

	def check_regex(self, text: str):
		"""Controlla i vari formati della stringa text

		Args:
			text (str): il testo da matchare (il filename)

		Returns:
			None | [int, int, int]: Returns None if any formats match, otherwise 
			it returns the date extrapolated ([YYYY, MM, DD]).
		"""
		for key, pattern in self.image_formats.items():
			if re.search(pattern, text):
				# Estrai la data da un formato di immagine
				return self.extract_date(text)

		for key, pattern in self.video_formats.items():
			if re.search(pattern, text):
				# Estrai la data da un formato di video
				return self.extract_date(text)

		return None

	def extract_date(self, text: str):
		# Estrarre la data dalla stringa text
		# Esempio: text = "IMG_20231209_150738.jpg"
		match = re.search(r'(\d{4})-(\d{2})-(\d{2})_(\d{2})(\d{2})(\d{2})', text)
		if match:
			year, month, day, hour, minute, second = map(int, match.groups())
			return [year, month, day, hour, minute, second]
		return None
