import pprint

if __name__ == '__main__':
    file = open('lorem_ipsum.txt')
    word_count = dict()
    for line in file:
        for word in line.split():
            if word in word_count.keys():
                word_count[word] += 1
            else:
                word_count[word] = 1

    pprint.pprint(word_count)