# dice-roller-python

advanced dice roller in python

Commands:
    
    .__________________________________________________________________________________________________________________.
    |                                                                                                                  |
    |roll    || arguments: roll <amt> <type>   || Rolls dice based on the included arguments   || aliases:             |
    |end     || arguments: end                 || use: Ends the program                        || aliases:             |
    |help    || arguments: help                || prints out the command list                  || aliases: ?, commands |
    |read    || arguments: read                || use: prints the contents of the options file || aliases: print       |
    \__________________________________________________________________________________________________________________/

# Commands (in depth):
    
roll: 
        
    Used to roll the amount and type of custom dice that you want. How to use: roll <amt> <type> 
    Example: roll 3 d20, roll 5 d17
end: 
        
    Used to end the program instead of ^C. How to use: end
help: 
        
    Used to open the commands index so that you can view possible commands and args. How to use: help , ? , commands
read: 
        
    Used to print the contents of the options file (options.json). How to use: read , print 

#Uses:
    
    Used for rolling dice, essentially as a random unmber generator, but way cooler.

Options:
    
    debug: set this to true to view all debug info
    
    printitterations: prints each iteration from each roll.
