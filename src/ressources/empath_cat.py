import os
from collections import defaultdict

# Function taking a string and returning every n_gram tokens
def n_tokenizer(string, n):
    tokens = string.split()
    for i in range(len(tokens)):
        for j in range(i+1, min(len(tokens)+1, i+1+n)):
            # replacing space with _ because that's how the words are stored in cat files
            yield '_'.join(tokens[i:j])

class Empath:
    def __init__(self, cat_folder_path):
        # cats loaded
        self.cats = defaultdict(list)
        # path to the base directory (containing the categories)
        self.path = cat_folder_path
        self.staging = {}
        # cache look up table from previous research
        self.inv_cache = {}
        # loading category in the base directory
        for f in os.listdir(cat_folder_path):
            if len(f.split(".")) > 1 and f.split(".")[1] == "empath":
                self.load(cat_folder_path + '/' + f)

    # open a tab separated file and load every word     
    def load(self,file):
        with open(file,"r") as f:
            for line in f:
                cols = line.strip().split("\t")
                name = cols[0]
                terms = cols[1:]
                for t in set(terms):
                    self.cats[name].append(t)
                    #self.invcats[t].append(name)

    # main function of class            
    def analyze(self, doc, categories = None, tokenizer = 1, normalize = False, verbose = False):
        # if the doc is a list, transform it to str
        if isinstance(doc,list):
            doc = "\n".join(doc)
        
        # if no category given, use default categories
        if not categories:
            categories = self.cats.keys()
        
        # if verbose = True, we save which words matche
        if verbose:
            match = []
        
        invcats = defaultdict(list)
        key = tuple(sorted(categories)) # key : catégorie(s)
        
        # initializing the reverse dictionary that map word to category
        if key in self.inv_cache:
            invcats = self.inv_cache[key]
        else:
            for k in categories:
                for t in self.cats[k]: invcats[t].append(k)
            self.inv_cache[key] = invcats
        
        # count dict will contains category: match items
        count = {}
        # count the total of tokens used (only usefull to normalize)
        tokens = 0.0
        # initilaizing count to 0
        for cat in categories: count[cat] = 0.0
        # iteraing through the n_gram tokens
        for tk in n_tokenizer(doc, n):
            tokens += 1.0
            # if the token is in the inversed dict, we add one to the count of every cat he's in
            if tk in invcats.keys():
                for cat in invcats[tk]:
                    # if we need to know which word matched, we add it to the match list
                    if verbose:
                        match.append(tk)
                    count[cat]+=1.0
        # normalizing values
        if normalize:
            for cat in count.keys():
                if tokens == 0:
                    return None
                else:
                    count[cat] = count[cat] / tokens
        # retunring the value, with or without match count 
        if verbose:
            return {'count': count, 'match': list(set(match))}
        else:
            return {'count': count}


    # create a category from a list of word
    def create_category(self, name, array):
        path = f"{self.path}/{name}.empath"
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
                                  tokenizer = 3, verbose = 1)
    print(empath_features)
    
    #print(list(bigram_tokenizer('Belle Bennett rat hftb')))
    #print(list(n_tokenizer('Belle Bennett rat hftb', n = 5)))

        