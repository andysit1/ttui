"""
  add more util functions to help parse data
"""

from ast import literal_eval
from filehandler_component import FileHandleComponent

class Parser(FileHandleComponent):
  def __init__(self) -> None:
    self.file_path : str = None

  def setup(self):
    if not self.path_exists(self.file_path):
      return False


class DictParse(Parser):
  def parse(self):
    if not self.setup:
      raise FileExistsError("File not found")



