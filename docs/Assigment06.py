# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# dstrop,2.23.2020,Created starter script
# dstrop, 2.29.2020, Modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions
listofdata = None


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        row = {'Task': str(task).strip(), 'Priority': str(priority).strip()}
        list_of_rows.append(row)
        return list_of_rows, 'success'


    @staticmethod
    def remove_data_from_list(key_to_remove, list_of_rows):

        '''Desc - removed a dictionary row from a list of dictionary rows based on search key

        :param: key_'''

        item_removed = False #create a boolean flag for loop
        row_number = 0 # Create a counter to identify the current dictionary row in the loop
        # SEARCH through the table of rows for a match to the user's input
        while[row_number < len(list_of_rows)]:
            if(key_to_remove == str(list(dict(list_of_rows[row_number]).values())[0])):
                del list_of_rows[row_number]
                item_removed = True
            row_number += 1
        return item_removed, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        objFile = open(file_name, 'w')
        for dicRow in list_of_rows: # write each row of data to the file
            objFile.write(dicRow['Task'] + ',' + dicRow['Priority'] + '\n')
        objFile.close()
        return list_of_rows, 'Success'

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority(listofdata):
         strTask = input("Enter a task: ")
         strPriority = input("Enter a priority: ")
         dicRow = {"Task": strTask, "Priority": strPriority.strip()}
         lstTable.append(dicRow)
         for objRow in lstTable:
             print(objRow)
         return lstTable, 'success' #returns the list table and the message success

    @staticmethod
    def input_task_to_remove(key_to_remove, list_of_rows):
        #Get user input about which task to remove from list
        status = 'row not found'

        for objRow in lstTable:
            print(objRow)
            print()


        for objRow in lstTable:
            if objRow[0].lower() == strItem.lower():
                lstTable.remove(objRow)
                status = 'Row removed'

        pass
        # return task
        return lstTable

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    
    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        strTask, strPriority = IO.input_new_task_and_priority(listofdata)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        strKeyToRemove = input("Which Task would you like to remove? ")
        boolItemRemoved = False #create a boolean flag for loop
        intRowNumber = 0 # create a counter to identify current dictionary row in loop

        while(intRowNumber < len(lstTable)):
            if(strKeyToRemove == str(list(dict(lstTable[intRowNumber]).values())[0])):
                del lstTable[intRowNumber]
                boolItemRemoved = True
            intRowNumber += 1


    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.write_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            for row in lstTable:
                print(row["Task"] + " (" + row["Priority"] + ")")
            print("*******************************************")
            print()  # Add an extra line for looks
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  #  Exit Program
        print("Goodbye!")
        break   # and Exit
