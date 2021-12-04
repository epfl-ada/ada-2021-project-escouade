import os
from collections import defaultdict
import json


def default_tokenizer(doc, n = None):
    return doc.split()


def bigram_tokenizer(doc, n = None):
    tokens = doc.split()
    for t1,t2 in zip(tokens,tokens[1:]):
        yield t1
        yield t1+"_"+t2
    yield tokens[-1]

def n_tokenizer(doc, n):
    tokens = doc.split()
    for i in range(len(tokens)):
        for j in range(i+1, min(len(tokens)+1, i+1+n)):
            yield '_'.join(tokens[i:j])

class Empath:
    def __init__(self, cat_folder_path):
        self.cats = defaultdict(list)
        self.staging = {}
        self.inv_cache = {}
        for f in os.listdir(cat_folder_path):
            if len(f.split(".")) > 1 and f.split(".")[1] == "empath":
                self.load(cat_folder_path + '/' + f)

                
    def load(self,file):
        with open(file,"r") as f:
            for line in f:
                cols = line.strip().split("\t")
                name = cols[0]
                terms = cols[1:]
                for t in set(terms):
                    self.cats[name].append(t)
                    #self.invcats[t].append(name)

                    
    def analyze(self,doc,categories=None,tokenizer="default",normalize=False):
        if isinstance(doc,list):
            doc = "\n".join(doc)
        if tokenizer == "default":
            tokenizer = default_tokenizer
        elif tokenizer == "bigrams":
            tokenizer = bigram_tokenizer
        elif isinstance(tokenizer, int):
            n = tokenizer
            tokenizer = n_tokenizer
        if not hasattr(tokenizer,"__call__"):
            raise Exception("invalid tokenizer")
        if not categories:
            categories = self.cats.keys()
        invcats = defaultdict(list)
        key = tuple(sorted(categories)) # key : catégorie(s)
        if key in self.inv_cache:
            invcats = self.inv_cache[key]
        else:
            for k in categories:
                for t in self.cats[k]: invcats[t].append(k)
            self.inv_cache[key] = invcats
        count = {}
        tokens = 0.0
        for cat in categories: count[cat] = 0.0
        print(list(tokenizer(doc, n)))
        print(invcats)
        for tk in tokenizer(doc, n):
            tokens += 1.0
            for cat in invcats[tk]:
                count[cat]+=1.0
        if normalize:
            for cat in count.keys():
                if tokens == 0:
                    return None
                else:
                    count[cat] = count[cat] / tokens
        return count

    
    def create_category(self, name, array, path):
        array = list(set(array))
        result = array
        result = list(map(lambda x : x.replace(" ", "_"), array))
        with open(path,"w", encoding = 'utf-8') as f:
            f.write("\t".join([name] + result))
        if name not in self.cats: 
            self.load(path)
        
        
if __name__ == '__main__':
    lexicon = Empath('empath_cat')
    film_name_test = ['Bohemios', 'De Garraf a Barcelona','Belle Bennett', 'titanic']
    person_name_test = ['Tarantino', 'Wes Anderson']
    lexicon.create_category("ADA_cinema_test3", film_name_test + person_name_test, path = 'empath_cat/test3.empath')
    empath_features = lexicon.analyze('Belle Bennett', 
                                  categories = ['ADA_cinema_test3'], 
                                  tokenizer = 3)
    print(empath_features)
    
    #print(list(bigram_tokenizer('Belle Bennett rat hftb')))
    #print(list(n_tokenizer('Belle Bennett rat hftb', n = 5)))

        