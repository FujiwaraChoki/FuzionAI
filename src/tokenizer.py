import json


class Tokenizer:
    def __init__(self, text: str):
        self.__text = text
        self.__words = self.tokenize()

    @property
    def text(self):
        '''
        Get the text property.
        '''
        return self.__text

    @property
    def words(self):
        '''
        Get the words property
        '''
        return self.__words

    def tokenize(self):
        '''Tokenize a string of text into a list of words.

        Args:
            text: A string of text.

        Returns:
            A list of words.
        '''
        return self.text.split(' ')

    def get_creators(self) -> list:
        creators = json.load(open('assets/creators.json'))
        creator_names = []
        for creator in creators:
            if str(creator['name']).lower() in self.text.lower():
                creator_names.append(creator['name'])

        return creator_names

    def get_links(self, creator_names) -> list:
        creators = json.load(open('assets/creators.json'))
        links = []
        for creator in creators:
            if creator['name'] in creator_names:
                links.append(creator['channel_link'])
        return links
