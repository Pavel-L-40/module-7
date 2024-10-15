#module 7.3

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        dict_ = {}
        exception =  [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']
        for file_name in self.file_names:
            list_for_dict = []
            with open(file_name, encoding = 'utf-8') as file:
                for line in file:
                    for char in exception:
                        line = line.replace(char, '')
                    line = line.split(' ')
                    list_for_dict += line
                dict_[file_name] = list_for_dict
        return dict_

    def find(self, word):
        word = word.lower()
        dict_all_words = self.get_all_words()
        for name in self.file_names:
            for num in range(len(dict_all_words[name])):
                if word == dict_all_words[name][num].lower():
                    dict_ = {}
                    dict_[name] = num + 1
                    return dict_

    def count(self, word):
        word = word.lower()
        dict_ = {}
        dict_all_words = self.get_all_words()
        for name in self.file_names:
            count = 0
            for piece in dict_all_words[name]:
                if word == piece.lower():
                    count += 1
            dict_[name] = count
        return dict_


# ========================= test case ================================



wf1 = WordsFinder('prototip.txt') # , 'prototip2.txt'

print(wf1.get_all_words())
print(wf1.find('но'))

print(wf1.count('уж'))
