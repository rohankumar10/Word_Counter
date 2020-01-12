import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    for ptext in soup.find_all('a', {'class': 'search-result__result-link ember-view'}):
        content = ptext.text  # Remove HTML Crap
        words = content.lower().split()  # To Lowercase and split each line into singular words
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)


def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbol = "!@#$%^&*()_+/',{}:.?"
        for i in range(0, len(symbol)):
            word = word.replace(symbol[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_count = []
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count, key=operator.itemgetter(1)):
        print(key, value)


start("https://www.linkedin.com/search/results/people/?keywords=carbon%20offset&origin=SWITCH_SEARCH_VERTICAL&page=2")
