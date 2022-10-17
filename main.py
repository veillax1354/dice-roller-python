import random
import os

#Title

print("____________________________________________________________")
print("|      ___        _                        _           _   |")
print("|     / _ \      | |                      | |         | |  |")
print("|    / /_\ \_   _| |_ ___  _ __ ___   __ _| |_ ___  __| |  |")
print("|    |  _  | | | | __/ _ \| '_ ` _ \ / _` | __/ _ \/ _` |  |")
print("|    | | | | |_| | || (_) | | | | | | (_| | ||  __/ (_| |  |")
print("|    \_| |_/\__,_|\__\___/|_| |_| |_|\__,_|\__\___|\__,_|  |")
print("|                                                          |")
print("|                                                          |")
print("|    ______ _           ______      _ _                    |")
print("|    |  _  (_)          | ___ \    | | |                   |")
print("|    | | | |_  ___ ___  | |_/ /___ | | | ___ _ __          |")
print("|    | | | | |/ __/ _ \ |    // _ \| | |/ _ \ '__|         |")
print("|    | |/ /| | (_|  __/ | |\ \ (_) | | |  __/ |            |")
print("|    |___/ |_|\___\___| \_| \_\___/|_|_|\___|_|            |")
print("|                                                          |")
print("|__________________________________________________________|")

print("                       ________     ")
print("            ______    | .   . |\    ")
print("           /     /\   |   .   |.\   ")
print("          /  '  /  \  | .   . |.'|  ")
print("         /_____/. . \ |_______|.'|  ")
print("         \ . . \    /  \ ' .   \.|  ")
print("          \ . . \  /    \____'__\|  ")
print("           \_____\/                 \n")

#Restart loop
while True:
    #Instructions 
    print("Please enter the dice you want to roll in the following format: \n<Die Amount> <Die Type>.\n\nYou can roll the following dice:\nD4\nD6\nD8\nD10\nD12\nD20\nD100\n\nIf you would like to end the program, type 'end'. \nIf you would like to see the commands this program can run, type 'help', 'commands', or '?'.\n\nControls for custom rolls: custom <min> <max>\n\nThanks, and hope you enjoy!")

    #Varible decleration
    endcode = ''
    Iteration = ''
    finalroll = ''
    dietype = ''
    rollamt = 0
    tmproll = 0
    roll = 0
    i = 0

    #Tries to crate a new output file, if one already exists, it will start to append to the new file.
    try:
        filewriteto = open("output.txt", "x")
        print("Output file created!")
    except:
        print("File already exists! Attempting to append to an existing file.")
        filewriteto = open("output.txt", "a")
    finally:
        filewriteto.write("\n\nProgram Start: \n\n")
    
    #Starts the main loop that runs the program
    while True:
        #Input & Parce
        diei = input("Roll: ").split()
        
        #COMMANDS
    
        #Handles ending the program
        if diei[0] == 'end':
            endcode = 'end'
            break
            
        #Handles restarting the program
        if diei[0] == 'restart':
            endcode = 'restart'
            break
        
        #Handles clearing of the output file
        if diei[0] == 'clear' or diei[0] == 'purge' or diei[0] == 'wipe':
            if os.path.exists("output.txt"):
                confirm = input("Are you sure you want to wipe the output file? Y/N ")
                if confirm == 'Y' or confirm == 'y':
                    os.remove("output.txt")
                    filewriteto = open("output.txt", "x")
                    filewriteto = open("output.txt", "a")
                    print("CMD 'wipefile' called. Confirmation true. File wipe succesfull.")
                elif confirm == 'N' or confirm == 'n':
                    print("CMD 'wipefile' called. Confirmation false. File wipe cancled.")
                continue
            else:
                print("\nThe file does not exist.\n\n")
                continue
       
        #Handles deletion of the output file
        if diei[0] == 'del' or diei[0] == 'delete':
            if os.path.exists("output.txt"):
                confirm = input("Are you sure you want to delete the output file? Y/N ")
                if confirm == 'Y' or confirm == 'y':
                    os.remove("output.txt")
                    print("CMD 'delfile' called. Confirmation true. File deletion succesfull.")
                    endcode = 'delfile'
                elif confirm == 'N' or confirm == 'n':
                    print("CMD 'delfile' called. Confirmation false. File deletion cancled.")
                break
            else:
                print("\nThe file does not exist.\n\n")
                continue
        
        #Reads the output file if one currently exist
        if diei[0] == 'read' or diei[0] == 'print':
            try:
                filewriteto = open("output.txt", "r")
                print(filewriteto.read())
                filewriteto = open("output.txt", "a")
                continue
            except:
                print("File already exists! Attempting to append to an existing file.")
                continue
        
        #Handles custom rolls
        if diei[0] == 'custom':
            try:
                min = int(diei[1]) 
                max = int(diei[2]) + 1
                tmproll = random.randrange(min,max)
                roll += tmproll
                finalroll = "Custom roll is: " + str(roll) + "\n\n"
                print(finalroll)
                filewriteto.write("\n['custom', '" + str(min) + "', '" + str(max - 1) + "']\n" + finalroll)
                tmproll = 0
                min = 0
                max = 0
                continue
            except IndexError:
                print("IndexError: list index out of range \nIt appears that you tried to run a command without including the propper arguments. Please try again")
                continue
            except ValueError:
                print("ValueError: invalid literal for int() with base 10: '" + diei[1] + "'\nIt appears that you have entered a value that cannot be procceced and translated into an integet using the base 10 system, please try again using the following format: <Dice amount> <Die type>")
                continue
    
        #Handles cmd listing
        if diei[0] == 'help' or diei[0] == 'commands' or diei[0] == '?':
            print('')
            print('__________________________________________________________________________________________________________________')
            print('|                                                                                                                |')
            print('|roll    || arguments: <amt> <type>        || Rolls dice based on the included arguments || aliases:             |')
            print('|custom  || arguments: custom <min> <max>  || use: allows for rolling with custom limits || aliases:             |')
            print('|end     || arguments: none                || use: Ends the program                      || aliases:             |')
            print('|restart || arguments: none                || use: Restarts the program                  || aliases:             |')
            print('|help    || arguments: none                || prints out the command list                || aliases: ?, commands |')
            print('|clear   || arguments: none                || use: clears the output file                || aliases: purge, wipe |')
            print('|read    || arguments: none                || use: prints the contents of the outpt file || aliases: print       |')
            print('|delete  || arguments: none                || use: deletes the output file               || aliases: del         |')
            print('|________________________________________________________________________________________________________________|')
            continue
            
       
            
        #Checks to see if the input roll amount is an integer or not
        try:
            rollamt = int(diei[0])
        except ValueError:
            print("ValueError: invalid literal for int() with base 10: '" + diei[0] + "'\nIt appears that you have entered a value that cannot be procceced and translated into an integet using the base 10 system, please try again using the following format: <Dice amount> <Die type>")
            continue
        try:
            dietype = str(diei[1])
        except IndexError:
            print("IndexError: list index out of range \nIt appears that you tried to run a command without including the propper arguments. Please try again")
            
        #Prints the output of a propper roll input    
        if os.path.exists("output.txt"):
            filewriteto.write(str(diei) + '\n')
            
        #Starts the main die roll sequence
        while i < rollamt:
            
            #Roll a D4
            if dietype == 'd4' or dietype == 'D4':
                tmproll = random.randrange(1,5)
                roll += tmproll
                Iteration = 'Iteration ' + str(i + 1) + ': ' + str(tmproll)
                print(Iteration)
                tmproll = 0
                
            #Roll a D6
            if dietype == 'd6' or dietype == 'D6':
                tmproll = random.randrange(1,7)
                roll += tmproll
                Iteration = 'Iteration ' + str(i + 1) + ': ' + str(tmproll)
                print(Iteration)
                tmproll = 0
        
            #Roll a D8
            if dietype == 'd8' or dietype == 'D8':
                tmproll = random.randrange(1,9)
                roll += tmproll
                Iteration = 'Iteration ' + str(i + 1) + ': ' + str(tmproll)
                print(Iteration)
                tmproll = 0
            
            
            #Roll a D10
            if dietype == 'd10' or dietype == 'D10':
                tmproll = random.randrange(1,11)
                roll += tmproll
                Iteration = 'Iteration ' + str(i + 1) + ': ' + str(tmproll)
                print(Iteration)
                tmproll = 0
            
            #Roll a D12
            if dietype == 'd12' or dietype == 'D12':
                tmproll = random.randrange(1,13)
                roll += tmproll
                Iteration = 'Iteration ' + str(i + 1) + ': ' + str(tmproll)
                print(Iteration)
                tmproll = 0
            
            #Roll a D20    
            if dietype == 'd20' or dietype == 'D20':
                tmproll = random.randrange(1,21)
                roll += tmproll
                Iteration = 'Iteration ' + str(i + 1) + ': ' + str(tmproll)
                print(Iteration)
                tmproll = 0
                
            #Roll a D100
            if dietype == 'd100' or dietype == 'D100':
                tmproll = random.randrange(1,101)
                roll += tmproll
                Iteration = 'Iteration ' + str(i + 1) + ': ' + str(tmproll) 
                print(Iteration)
                tmproll = 0
            
            #Appends each iteration from the roll to the output file
            filewriteto.write(Iteration + '\n')
            
            i += 1
            
            finalroll = '\nFinal roll is: ' + str(roll) + '\n\n'
        
        print(finalroll)
        #Appends the final roll to the output file
        filewriteto.write(finalroll)
        
            
        print("All outputs have been saved. To view them, please view 'output.txt'\n")
    
        
    if endcode == 'delfile':
        print("Hey! This has stopped running due to a request for file deletion. To stop the recreation of the file or any errors due to the file being missing. Please start it again if you want to continue using the program, just make sure to be done first.")
        break
    elif endcode == 'end':
        print("Thanks for using this dice roller. I hope you liked it!.")
        break
    elif endcode == 'restart':
        continue
