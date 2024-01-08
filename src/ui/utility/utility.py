# This file contains useful functions that can be utilized by multiple UI components.
from tkinter.ttk import Frame
from typing import List


def configure_weight(frame:Frame, rows:List[int], columns:List[int]):
  """Automatically configures the weight of all rows and columns in a grid to 1.

  Args:
    frame (Frame): The window that contains the grid.
    rows (int): Number of rows in the grid.
    columns (int): Number of columns in the grid.
  """
  for row in rows:
    frame.rowconfigure(row, weight=1)
  for col in columns:
    frame.columnconfigure(col, weight=1)