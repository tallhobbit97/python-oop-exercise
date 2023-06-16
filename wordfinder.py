"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, file_path):
        self.word_list = self.get_list(file_path)
        print(f"{len(self.word_list)} words read")
    
    def get_list(self, file_path):
        length = random.randint(3, 10)
        word_list = []
        file = open(file_path)
        words = file.read().split()

        i = 0
        while i < length:
            word_list.append(random.choice(words))
            i += 1
        file.close()
        return list(set(word_list))
    
    def random(self):
        return self.word_list[random.randint(0, len(self.word_list) - 1)]

wf = WordFinder('words.txt')

print(wf.random())
print(wf.random())
print(wf.random())

class RandomWordFinder(WordFinder):
    def __init__(self, file_path):
        self.word_list = self.get_list(file_path)
        print(f"{len(self.word_list)} words read")
    
    def get_list(self, file_path):
        words = list(set(super().get_list(file_path)))
        for word in words:
            if word == "" or word.startswith("#"):
                words.remove(word)
        return words
    
rwf = RandomWordFinder("more_words.txt")

print(rwf.random())
print(rwf.random())
print(rwf.random())