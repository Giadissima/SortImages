from src.file import File
from moviepy.editor import VideoFileClip

class VideoHelper(File):

  def isVideo(file_path):
    """Verifica se il file è un video.

    Args:
        file_path (str): Percorso del file da verificare.

    Returns:
        bool: True se il file è un video, altrimenti False.
    """
    video_extensions = {'avi', 'mkv', 'mp4', 'mov', 'flv', 'wmv', 'webm'}  # Aggiungi le estensioni video che desideri supportare

    # Estrai l'estensione del file
    file_extension = file_path.rsplit('.',1)[1].lower()

    # Verifica se l'estensione è nella lista delle estensioni video
    if file_extension in video_extensions:
        return True

    return False
  
  def get_date_from_metadata(self, vid):
    try:
      video = VideoFileClip(vid)
      creation_date = video.reader.infos.get('creation_time')
      video.close()
      print("data di crezione trovata nel video: ", creation_date)
      return creation_date
    except Exception as e:
      return None

