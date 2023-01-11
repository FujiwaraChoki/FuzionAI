import os
import downloader
from tokenizer import Tokenizer
from exceptions import NoCreatorsError


def main():
    # Create output directory
    os.makedirs('build', exist_ok=True)
    user_input = input('What video do you want to generate?\n')
    tokenizer = Tokenizer(user_input)
    creators = tokenizer.get_creators()

    if len(creators) == 0:
        raise NoCreatorsError('No creators found in the input.')
    else:
        print(creators)


if __name__ == '__main__':
    main()
