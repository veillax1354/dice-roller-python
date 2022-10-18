import random
import json
import os

#Title

print("____________________________________________________________\n|      ___        _                        _           _   |\n|     / _ \      | |                      | |         | |  |\n|    / /_\ \_   _| |_ ___  _ __ ___   __ _| |_ ___  __| |  |\n|    |  _  | | | | __/ _ \| '_ ` _ \ / _` | __/ _ \/ _` |  |\n|    | | | | |_| | || (_) | | | | | | (_| | ||  __/ (_| |  |\n|    \_| |_/\__,_|\__\___/|_| |_| |_|\__,_|\__\___|\__,_|  |\n|                                                          |\n|                                                          |\n|    ______ _           ______      _ _                    |\n|    |  _  (_)          | ___ \    | | |                   |\n|    | | | |_  ___ ___  | |_/ /___ | | | ___ _ __          |\n|    | | | | |/ __/ _ \ |    // _ \| | |/ _ \ '__|         |\n|    | |/ /| | _|  __/  | |\ \ (_) | | |  __/ |            |\n|    |___/ |_|\___\___| \_| \_\___/|_|_|\___|_|            |\n|                                                          |\n|__________________________________________________________|\n                       ________     \n            ______    | .   . |\    \n           /     /\   |   .   |.\   \n          /  '  /  \  | .   . |.'|  \n         /_____/. . \ |_______|.'|  \n         \ . . \    /  \ ' .   \.|  \n          \ . . \  /    \____'__\|  \n           \_____\/               \n")
print(
    "Please enter the dice you want to roll in the following format: \n<Die Amount> <Die Type>.\n\nYou can roll the following dice:\nD4\nD6\nD8\nD10\nD12\nD20\nD100\n\nIf you would like to end the program, type 'end'. \nIf you would like to see the commands this program can run, type 'help', 'commands', or '?'.\n\nControls for custom rolls: custom <min> <max>\n\nThanks, and hope you enjoy!\n"
)

# Handles options
# Opening JSON file
f = open('options.json',)
  
# returns JSON object as a dictionary
data = json.load(f)

# Iterating through the json list
for i in data['options']:
    verify = str(i).split()  
debugverify1 = verify[1].strip(',')
if debugverify1 == 'True':
    print('Debug Enabled\n' + str(verify) + '\n')

printverify1 = verify[3].strip('}')
if printverify1 == 'True':
    print('Itteration Printing Enabled\n' + str(verify) + '\n')

commands = ['']
endcode = ''
cmd = ''
num = 0
roll = 0
i = 1

while True:
    cmd = input('Command: \n')
    commands = cmd.split()
    if debugverify1 == 'True':
        print(commands)

    #COMMANDS
    #Handles cmd listing
    if commands[0] == 'help' or commands[0] == 'commands' or commands[0] == '?':
        print('')
        print(
            '____________________________________________________________________________________________________________________'
        )
        print(
            '|                                                                                                                  |'
        )
        print(
            '|roll    || arguments: roll <amt> <type>   || Rolls dice based on the included arguments   || aliases:             |'
        )
        print(
            '|end     || arguments: end                 || use: Ends the program                        || aliases:             |'
        )
        print(
            '|restart || arguments: restart             || use: Restarts the program                    || aliases:             |'
        )
        print(
            '|help    || arguments: help                || prints out the command list                  || aliases: ?, commands |'
        )
        print(
            '|clear   || arguments: clear               || use: clears the options file                 || aliases: purge, wipe |'
        )
        print(
            '|read    || arguments: read                || use: prints the contents of the options file || aliases: print       |'
        )
        print(
            '|__________________________________________________________________________________________________________________|'
        )
        continue

        #Handles ending the program
    if commands[0] == 'end':
        confirm = input(
            "Are you sure you want to end the current session? Y/N ")
        if confirm == 'Y' or confirm == 'y':
            endcode = 'end'
            print(
                "CMD 'sessionend' called. Confirmation true. Terminating session."
            )
            break
        elif confirm == 'N' or confirm == 'n':
            print(
                "CMD 'sessionend' called. Confirmation false. Session termination cancled."
            )
            continue

    
    #Handles clearing of the options file
    if commands[0] == 'clear' or commands[0] == 'purge' or commands[
            0] == 'wipe':
        if os.path.exists("options.json"):
            confirm = input(
                "Are you sure you want to wipe the options file? Y/N ")
            if confirm == 'Y' or confirm == 'y':
                os.remove("options.json")
                options = open("options.json", "x")
                options = open("options.json", "a")
                print(
                    "CMD 'wipefile' called. Confirmation true. File wipe succesfull."
                )
            elif confirm == 'N' or confirm == 'n':
                print(
                    "CMD 'wipefile' called. Confirmation false. File wipe cancled."
                )
                continue
            else:
                print("\nThe file does not exist.\n\n")
                continue

    #Handles deletion of the options file
    if commands[0] == 'del' or commands[0] == 'delete':
        if os.path.exists("options.json"):
            confirm = input(
                "Are you sure you want to delete the options file? Y/N ")
            if confirm == 'Y' or confirm == 'y':
                os.remove("options.json")
                print(
                    "CMD 'delfile' called. Confirmation true. File deletion succesfull."
                )
                endcode = 'delfile'
            elif confirm == 'N' or confirm == 'n':
                print(
                    "CMD 'delfile' called. Confirmation false. File deletion cancled."
                )
            continue
        else:
            print("\nThe file does not exist.\n\n")
            continue
        #Reads the options file if one currently exist
        if commands[0] == 'read' or commands[0] == 'print':
            try:
                print(options.read())
                continue
            except:
                print("The file does not exist.")
                continue

    try:
        if commands[0] == 'roll':
            roll = int(commands[2][1:])
            if debugverify1 == 'True':
                print('roll')
                print(roll)
            if len(commands) == 3:
                if debugverify1 == 'True':
                    print(len(commands))
                i = 1
                while int(i) < (int(commands[1]) + 1):
                    mun = random.randint(1, roll)
                    num += mun
                    if debugverify1 == 'True':
                        print(str(i) + ': ' + str(mun))
                    if printverify1 == 'True':
                        print(str(i) + ': ' + str(mun))
                    i += 1
                print(num)
                num = 0
    except ValueError:
        print('Invalid value inputed. Please try again.')
        continue
