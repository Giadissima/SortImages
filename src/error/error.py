class FileNotMovedError(IOError):
  def __init__(self):
    super().__init__()
    
class FileWithoutExtensionError(IOError):
  def __init__(self):
    super().__init__()