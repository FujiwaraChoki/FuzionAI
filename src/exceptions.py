from termcolor import colored


class NoCreatorsError(Exception):
    '''
    Exception/Error Class when the user hasn't
    entered any creators / the entered creators weren't found in the list.
    '''

    def __init__(self, message: str):
        self.message = colored(message)
