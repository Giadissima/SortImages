from meta.decorators import singleton


"""This class is used to save information about the media organization
process and then display a summary in the message box that notifies that
the sorting is completed. This information includes:

- the total media found
- duplicates found
- media moved
- media without date found
- media deleted
- folders deleted."""
@singleton
class MediaResultCalculator():
  def __init__(self):
    self.reset_total_results()
  
  def increment_total_media(self)->None: self.TOTAL_IMG = self.TOTAL_IMG + 1
  def increment_total_media_moved(self)->None: self.TOTAL_IMG_MOVED = self.TOTAL_IMG_MOVED + 1
  def increment_total_media_deleted(self)->None: self.TOTAL_IMG_DELETED = self.TOTAL_IMG_DELETED + 1
  def increment_total_unrecognized_media(self)->None: self.TOTAL_UNRECOGNIZED_IMG = self.TOTAL_UNRECOGNIZED_IMG + 1
  def increment_total_folder_deleted(self)->None: self.TOTAL_FOLDER_DELETED = self.TOTAL_FOLDER_DELETED + 1
  def increment_total_media_duplicates_found(self)->None: self.TOTAL_MEDIA_DUPLICATES_FOUND = self.TOTAL_MEDIA_DUPLICATES_FOUND + 1
  
  def reset_total_results(self)->None:
    self.TOTAL_IMG = 0
    self.TOTAL_IMG_MOVED = 0
    self.TOTAL_IMG_DELETED = 0
    self.TOTAL_UNRECOGNIZED_IMG = 0
    self.TOTAL_FOLDER_DELETED = 0
    self.TOTAL_MEDIA_DUPLICATES_FOUND = 0