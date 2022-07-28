from string import punctuation

def remove_punc(text):

    for punc in punctuation:
        text = text.replace(punc,'')
    return text

def word_count(text):
    wordlist = text.split()
    wc = {}
    for word in wordlist:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1
    return wc

def sort(word_dict):
    ans = sorted(word_dict.items(), key = lambda val: val[1],reverse = True)
    return dict(ans)

if __name__ == '__main__':
    long_text = '''
    Hey one day we will meet in the forest and will enjoy the beauty of the nature. Having a cup of coffee and enjoying the nature.
    '''
    cl_text = remove_punc(long_text)
    counted_word = word_count(cl_text)
    sorted_words = sort(counted_word)
    print(counted_word)
    print(sorted_words)
