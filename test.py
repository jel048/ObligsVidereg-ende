import urllib.request

url = f'https://liveexample.pearsoncmg.com/data/babynameranking2008.txt'
input = urllib.request.urlopen(url)
text = input.read().decode('utf-8').split('\n')
lst = []

for i in text:
    lst.append([item.strip() for item in i.split("\t")])
    
print(lst[5])

    
