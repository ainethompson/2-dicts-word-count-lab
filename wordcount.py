# put your code here.


def count_words(filename):

    chars_to_replace = ["/n",]
    word_counts = {}

    with open(filename) as f:

        lines = f.readlines()
    for line in lines:
        words = line.rstrip().split(' ')

        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

    for word, count in word_counts.items():
        print(word, count)

count_words("test.txt")