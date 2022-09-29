def reverse_words(text):
    strList = []
    for word in text.split(' '):
        strList.append(word[::-1])
    return ' '.join(strList)