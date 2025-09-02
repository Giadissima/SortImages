from typing import List, Optional, Tuple
from src.sort.regex.regex import RegexManager
from src.files_manager.files import File
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

class VideoHelper(File):

  @staticmethod
  def isVideo(file_path:str)->bool:
    """Check if the file is a video.

    Args:
      file_path (str): Path of the file to check.

    Returns:
      bool: True if the file is a video, otherwise False.
    """
    video_extensions = {'avi', 'mkv', 'mp4', 'mov', 'flv', 'wmv', 'webm', '3gp'}
    file_extension = file_path.rsplit('.',1)[1].lower()
    return file_extension in video_extensions
  
  @staticmethod
  def get_date_from_metadata(vid:str)->Optional[Tuple[str, str, str]]:
    """Search for the date contained in the metadata

    Args:
      vid (str): path of the video to extract date

    Returns:
      Optional[Tuple[str, str, str]]: the date if video has metadata
    """
    parser = None
    try:
      parser = createParser(vid)
      metadata = extractMetadata(parser)
      if metadata.has("creation_date"):
        creation_date: str = (metadata.get("creation_date").strftime("%Y %m %d")).split()
        if(creation_date and creation_date[0]!= None):
          creation_date[0] = RegexManager.get_year(creation_date[0])
          if(not creation_date[0]): return None
          return creation_date
        return None
    except (FileNotFoundError, PermissionError) :
      return None
    finally:
      if parser:
        parser.close()