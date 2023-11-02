from src.file import File
from moviepy.editor import VideoFileClip
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

class VideoHelper(File):

  def isVideo(self, file_path):
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
      parser = createParser(vid)
      metadata = extractMetadata()
      if metadata.has("creation_date"):
        creation_date: str = metadata.get("creation_date").strftime("%Y %m %d")
        print("Data di creazione del video:", creation_date.split())
        return creation_date.split()
      else:
        print("Data di creazione non trovata nei metadati del video.")
    except Exception as e:
      return None
    finally:
      if video is not None:
        video.close()
      if parser is not None:
        parser.close()

