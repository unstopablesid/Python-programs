class person:
  def __init__(self, name, occ):  # Add arguments to __init__
      self.name = name
      self.occ = occ
      print("hey i am a constructor")

  def info(self):  # Add self as the first argument
    print(f"{self.name} is a {self.occ}")


a = person("harry", "Developer")
b = person("Divya", "HR")
a.info()
b.info()