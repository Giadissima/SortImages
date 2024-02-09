"""This file contains the custom error classes that will be thrown in the project"""

class FileNotMovedError(IOError):
  def __init__(self):
    super().__init__()
    
class FileWithoutExtensionError(IOError):
  def __init__(self):
    super().__init__()