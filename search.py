#!/usr/bin/python3
import wikipedia
import time
def main():
    term = raw_input('What do you want to search for? ')
    print(Search(term))
    
def Search(term):
    result = ''
    while len(result) < 5:
        result = wikipedia.summary(term, sentences = 2)
    return result

if __name__ == '__main__':
    main()


# import wikipedia
# print wikipedia.summary("Wikipedia")
# Wikipedia...
#
# wikipedia.search("Barack")
# [u'Barak (given name)', u'Barack Obama', u'Barack (brandy)', u'Presidency of Barack Obama', u'Family of Barack Obama', u'First inauguration of Barack Obama', u'Barack Obama presidential campaign, 2008', u'Barack Obama, Sr.', u'Barack Obama citizenship conspiracy theories', u'Presidential transition of Barack Obama']
#
# ny = wikipedia.page("New York")
# ny.title
# u'New York'
# ny.url
# u'http://en.wikipedia.org/wiki/New_York'
# ny.content
# u'New York is a state in the Northeastern region of the United States. New York is the 27th-most exten'...
# ny.links[0]
# u'1790 United States Census'
#
# wikipedia.set_lang("fr")
# wikipedia.summary("Facebook", sentences=1)
# Facebook ...