import requests
from tokenizer import Tokenizer
from exceptions import NoCreatorsError


def main():
    user_input = input('What video do you want to generate?\n')
    tokenizer = Tokenizer(user_input)
    words = tokenizer.words
    creators = tokenizer.get_creators()

    if len(creators) == 0:
        raise NoCreatorsError('No creators found in the input.')
    else:
        print(creators)


if __name__ == '__main__':
    main()
