import random

def eq2text(eq):
    lst = []
    for i in range(len(eq)):
        if eq[i] == 1:
            lst.append(f'x' if i == 0 or i == 2 else f'{eq[i]}')
        elif eq[i] == -1:
            lst.append(f'-x' if i == 0 or i == 2 else f'{eq[i]}')
        else:
            lst.append(f'{eq[i]}x' if i == 0 or i == 2 else f'{eq[i]}')
            
    return \
        f'{lst[0]} {"-" if lst[1][0:1] == "-" else "+"} {lst[1][1:] if lst[1][0:1] == "-" else lst[1]} = {lst[2]} {"-" if lst[3][0:1] == "-" else "+"} {lst[3][1:] if lst[3][0:1] == "-" else lst[3]}'

def OK(L):
    if L[0] == L[2]:
        return False
    if L[1] == L[3]:
        return False
    for i in L:
        if i == 0:
            return False
    return True


def make_eq():
    valid = False
    while valid == False:
        eq = []
        for i in range(4):
            eq.append(random.randint(-9, 9))
        if OK(eq):
            valid = True
    return eq

def make_n_eqs(n):
    eqs = []
    for i in range(n):
        eq = make_eq()
        if eq not in eqs and eq[2:] + eq[0:2] not in eqs:
            eqs.append(eq)
    return eqs

def make_test(students, n):
    dict = {}
    for i in students:
        dict[i] = make_n_eqs(n)
    return dict

d = make_test(['Ada','Bob'], 4)

def answer_questions(D):
    resultlst = []
    name = ""
    while name not in D.keys():
        name = input("Enter your name: ")
    count = 0
    print("Please solve these equations: ")
    for i in D[name]:
        letter = chr(ord("a") + count)
        lst = i
        print(f'{letter}) {eq2text(lst)}')
        answer = float(input("x = "))
        lst.append(answer)
        resultlst.append(lst)
        count += 1
    D[name] = resultlst

def main():



    tests = make_test(['Ola', 'Kari', 'Fredrik'], 5)

    answer_questions(tests)

    print(tests)
    
main()