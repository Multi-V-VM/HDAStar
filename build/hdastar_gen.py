import random

with open("hdastar.txt", "w") as f:
    f.write("5 5\n")
    for i in range(5+1):
      for j in range(5+1):
        f.write("{}".format("#" if random.randint(0, 100) < 20 else "."))
      f.write("\n")
