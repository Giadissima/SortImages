def singleton(cls):
  """define a decorator capable of generating a single instance of the specified class at a time
  Args:
  cls: The class to which the decorator is applied."""
  instances = {}

  def get_instance(*args, **kwargs):
    if cls not in instances:
      instances[cls] = cls(*args, **kwargs)
    return instances[cls]

  return get_instance
