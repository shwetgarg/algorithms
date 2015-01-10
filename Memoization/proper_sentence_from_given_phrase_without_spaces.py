'''Given a dictionary of words. Given a phrase without spaces, add spaces to make it a proper sentence.'''

from memoize import memoized

class SentenceFromPhrase:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    @memoized
    def get_sentences(self, phrase):
        return_var = {}
        if len(phrase) == 0:
            return
                
        for i in range(1, len(phrase)+1):
            return_var2 = []
            if phrase[0:i] in self.dictionary and isinstance(self.get_sentences(phrase[i:]), dict):
                return_var2.append(self.get_sentences(phrase[i:]))
            if len(return_var2)> 0:
                return_var[i] = return_var2
        return return_var

def main():
    dictionary_words = ["mobile","samsung","sam","sung","man","mango","icecream","and","go","i","like","ice","cream"]
    dictionary = dict.fromkeys(dictionary_words)
    sentence_from_phrase = SentenceFromPhrase(dictionary)
    phrase = "ilikesamsung"
    print sentence_from_phrase.get_sentences(phrase)

if __name__ == "__main__":
    main()
    
