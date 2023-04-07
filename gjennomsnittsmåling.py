from datetime import datetime
FILENAME1 = "box_a.txt"
FILENAME2 = "box_b.txt"
def fileToDictionary(filename):
    lst= []
    with open(filename, 'r') as file:
        for line in file:
            lst.append(line.split(','))
    lst2 = []
    for i in range(len(lst)):
        lst2.append([j.strip() for j in lst[i]])
    
    dictfile = dict(lst2)
    return dictfile

def listSpeeders(filename_a, filename_b, speed_limit, distance):
    dict1 = fileToDictionary(filename_a)
    dict2 = fileToDictionary(filename_b)
    allowedSpeed = speed_limit * 1.05
    speederList = dict()
    for licence, time in dict1.items():
        try:
            passFirst = datetime.strptime(dict1[licence], '%Y-%m-%d %H:%M:%S')
            passSecond = datetime.strptime(dict2[licence], '%Y-%m-%d %H:%M:%S')
            tid = passSecond - passFirst
            seconds = tid.total_seconds()
            speed = ((distance * 1000) / seconds) * 3.6
            if speed > allowedSpeed:
                speederList[licence] = (round(speed, 3), time, speed_limit)
        except KeyError: #Ikke alle som kjører forbi boks 1 som kjører forbi boks 2.
            continue
            
    return speederList
