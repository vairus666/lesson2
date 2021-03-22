"""
Введи цвет светофора говорит, и программа скажет что тебе делать.

exit -- завершает программу
"""
print ('Svetofor')
comand = str(input ('Tell me the color\n'))
while comand.lower() != 'exit':
    if comand.lower() == "red":
        print ('Stay')
        comand = str(input ('Tell me the color\n'))
    elif comand.lower() == "yellow":
        print('Stay and wait or go quickly')
        comand = str(input ('Tell me the color\n'))
    elif comand.lower() == "green":
        print('Go')
        comand = str(input ('Tell me the color\n'))
    else:
        print('Color not found')
        comand = str(input ('Tell me the color\n'))
