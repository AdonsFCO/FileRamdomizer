import os

working = True


# This method ask if the path exist or not.
def ask_for_directory():

    path = str(input('First of all select your path. Write down below your path:'))
    if not os.path.isdir(path):
        print('is not a path', os.path.isfile(path))
    else:
        print('Error 00. You have added an wrong syntax path. Please try again.')
        input("Press enter.")


while working:
    print('Welcome to file randomizer.')
    ask_for_directory()
