import os
import colorama as color
working = True


# This method ask if the     path exist or not.
def ask_for_directory():

    path = str(input('First of all select your path. Write down below your path:'))
    if not os.path.isdir(path):
        print(color.Fore.RED + 'Error 00. You have added an wrong syntax path. Please try again.', os.path.isfile(path))
    else:
        print('This is a path.')
        input("Press enter.")


while working:
    print('Welcome to file randomizer.')
    ask_for_directory()
