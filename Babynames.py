import urllib.request

def main():
    year = input("Enter the year:")
    gender = input("Enter the gender, F or M: ")
    name = input("Enter the name: ")
    
    print(retrieveFromNameList(year, gender, name))
    
def retrieveFromNameList(year, gender, name):
    url = f'https://liveexample.pearsoncmg.com/data/babynameranking{year}.txt'
    input = urllib.request.urlopen(url)
    text = input.read().decode().split('\n')
    nameList = []
    for i in text:
        nameList.append([item.strip() for item in i.split("\t")])
    g = 1 if gender == "M" else 3
    for line in nameList:
        if name in line: 
            return f'{"Girl" if g == 3 else "Boy"} name {name} is ranked #{line[0]} in year {year}'
    return f'The name {name} was not among the top 1000 in the year {year}'
        
        
main()