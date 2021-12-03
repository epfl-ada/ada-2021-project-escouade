def create_category(name, array, path, write=True):
    array = list(set(array))
    result = list(map(lambda x : x.replace(" ", "_"), array))
    if write:
        with open(path,"w", encoding = 'utf-8') as f:
            f.write("\t".join([name] + result))