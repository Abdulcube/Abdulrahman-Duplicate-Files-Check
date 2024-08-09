from functions import get_user_input, traverse_directory
import time
# Entry Point
def main(): 
    print('Welcome to the program Jedi!\n')
    while True:
        
        user_input = get_user_input()

        # Traverse file system
        print('Traversing...\n')                    
        resulting_groups = traverse_directory(user_input)
        print ('Complete!\n')
        time.sleep(.5)


        # Resulting value on successful traverse
        if len(resulting_groups) == 0:
            print('There are no duplicated files within the sent directory!')
        else: 
            print('The following groups are the duplicate files from the entered directory:')
            for group in resulting_groups:
                print(group)
        print()
        
        # User input for restarting/termination of program
        cancel = False
        while True:
            user_status = input('Would you like to continue the program? (Yes/No): ')
            if user_status.lower() == 'no':
                cancel = True
                break
            if user_status.lower() != 'yes':
                print('\nPlease try again with correct input.')
            else:
                break
        if(cancel):
            print()
            break
                
    print('\nThank you... Terminating Program.\n')

if __name__ == '__main__':
    main()






