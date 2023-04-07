def main():
    val = int(input("Enter an integer: "))
    print(reverseDisplay(val))

def reverseDisplay(value):
    result = []
    reverseDisplayHelper(value, result)
    return int(''.join(result))

def reverseDisplayHelper(val, lst):
    if val < 10:
        lst.append(str(val))        
    else:
        lst.append(str(val%10))
        return reverseDisplayHelper(val//10, lst)
    

main()
