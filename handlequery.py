#!/usr/bin/python3

import re
import search
import nav


def main():
    query = raw_input('Enter query: ')
    handle(query)
    
def handle(query):
    result = ''
    diff = re.search('[A-Z]*', query)
    if diff.group() == 'SEARCH':
        print('Search query')
        query = (re.sub('[A-Z]*\s','',query))
        print(query)
        result = search.Search(query)
        result = (re.sub('(\/.*\/)', '', result))
        result = (re.sub('\(.*\)', '', result))
        
        
    elif diff.group() == 'NAV':
        print('Nav query')
        diff = re.sub('[A-Z]*\s','',query)
        places = re.findall('#.*?#', diff)
        source, destination = places
        source = re.sub('#', '', source)
        destination = re.sub('#', '', destination)
        print(source)
        print(destination)
        result = nav.Nav(source, destination)
    
    print(result)        
    return result

if __name__ == "__main__":
    main()