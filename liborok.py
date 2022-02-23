from colorama import Fore
def setcolor(color):
  if (color == "blue"):
    return Fore.BLUE
  elif (color == "red"):
    return Fore.RED
  elif (color == "green"):
    return Fore.GREEN
  elif (color == ""):
    return Fore.RESET
  elif (color == "yellow"):
    return Fore.YELLOW
  elif (color == "pink"):
    return Fore.LIGHTMAGNETTA_EX
  elif (color == "resetthis"):
    return Fore.RESET, "Hello World!"
  





def logger(log):
  print(log)
  
