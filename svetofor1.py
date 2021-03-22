"""Введи цвет светофора говорит, и программа скажет что тебе делать."""
print ('Svetofor')
comand = str(input ('Tell me the color\n'))
if comand.lower() == "red":
  print ('Stay')
elif comand.lower() == "yellow":
  print('Stay and wait or go quickly')
elif comand.lower() == "green":
  print('Go')
else:
  print('Color not found')
