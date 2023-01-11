import requests
from tokenizer import Tokenizer


def main():
    creators = json.load(open('assets/creators.json'))
    creator_names = []
    creator_links = []
    for creator in creators:
        creator_names.append(creator['name'])
        creator_links.append(creator['channel_link'])

    user_input = input('What video do you want to generate?\n')
    tokenizer = Tokenizer(user_input)
    words = tokenizer.words
    creators = tokenizer.get_creators()
    
    if len(creators) == 0:
        


if __name__ == '__main__':
    main()
