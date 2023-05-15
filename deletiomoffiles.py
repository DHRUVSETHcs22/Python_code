#deletion of file and dir
import os

if os.path.exists("myfile2.txt"):
    os.remove("myfile2.txt")
else:
  print("The file does not exist")

