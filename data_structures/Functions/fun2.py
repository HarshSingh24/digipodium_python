def vowel(sentence):
    result = {}
    for i in 'aeiou':
        result[i] = sentence.lower().count(i)
    return result

if __name__ == "__main__":
    msg = "This is a test"
    print(vowel(msg))