from urllib.request import urlretrieve
import os
print(os.getcwd())

with open ('./tigres.txt', 'r') as f:
    urls = f.readlines()
    for i, j in enumerate(urls):
        if ('jpg' in j) and (i >600):
            try:
                urlretrieve(j, '{}.jpg'.format(i))
            except:
                pass
