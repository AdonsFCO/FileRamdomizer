import os

working = True


def ask_for_directory(directory):

    if not os.path.isfile(directory):
        print('is not a path')
    else:
        print('is a path')


while working:
    print('Welcome to file randomizer.')
    path = input('First of all select your path. Write down below your path:')
    ask_for_directory(path)