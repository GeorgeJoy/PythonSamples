from urllib.request import urlopen

def fetch():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words

def print_words(word_list):
    for word in word_list:
        print(word)

print(__name__)
if __name__ == "__main__":
    print_words(fetch())