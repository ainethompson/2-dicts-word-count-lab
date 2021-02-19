# put your code here.

def count_words(filename):

    punctuation = ''',.?!()-[]{};:'"\<>/@#$&%^~_'''
    word_counts = {}

    for line in open(filename):
        words = line.rstrip().split(' ')

        for word in words:
            word = ''.join(char for char in word if char not in punctuation).lower()
            word_counts[word] = word_counts.get(word, 0) + 1

    for word, count in word_counts.items():
        print(word, count)

count_words("test.txt")