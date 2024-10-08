# EDIT THE FILE WITH YOUR SOLUTION
import sys
import re
from os.path import exists
from itertools import product

file_name = input('Which text file do you want to use for the puzzle? ').removesuffix('\n')
if not exists(file_name):
    print('Incorrect input, giving up.')
    sys.exit()
f = open(file_name, 'r')
text = f.read()
people = []
words = []
j1 = 'am a Knave'
j2 = 'am a Knight'
j3 = 'is a Knight'
j4 = 'is a Knave'
j5 = 'll of us are Knights'
j6 = 'll of us are Knaves'
flagt=0
fakenames=['Knight','Knave','Sir','Sirs','Knights','Knaves']
pattern=re.compile('Though|Also|However|Furthermore|Moreover|Besides|Indeed|Again|Naturally|Namely|First|Second|Third|Next|Eventually,Afterward|Meanwhile|Therefore|Immediately|Finally')
namelist = []
newtext = re.sub(r"\n", " ", text)
newtext = re.sub(r'\?"', ".", newtext)
newtext = re.sub(r'\."', ".", newtext)
newtext = re.sub(r'\!"', ".", newtext)
newtext = re.sub(pattern, "", newtext)
sentences = re.split(r'\.|\!|\?', newtext)
for line in sentences:
    s = re.finditer(
        r'Sir ([A-Z][a-z]+)|Sirs ([A-Z][a-z]+) and ([A-Z][a-z]+)| ([A-Z][a-z]+), ([A-Z][a-z]+)|and Sir (['
        r'A-Z][a-z]+)|Sirs ([A-Z][a-z]+), ([A-Z][a-z]+)|Sirs ([A-Z][a-z]+)|([A-Z][a-z]+), ([A-Z][a-z]+) and ([A-Z][a-z]+)', line)
    for names in s:
        names = re.split(r'and |Sirs |Sir |, ', names.group())
        for name in names:
            if len(name.strip()) and name.strip() not in namelist and name.strip() not in fakenames :
                namelist.append(name.strip())
                namelist = sorted(namelist, key=str.lower)

    states = re.findall(r'"(.+)', line)
    states2 = re.findall(r'"(.+)"', line)
    if len(states) or len(states2):
        s = re.finditer(
            r'Sir ([A-Z][a-z]+)|Sirs ([A-Z][a-z]+) and ([A-Z][a-z]+)| ([A-Z][a-z]+), ([A-Z][a-z]+)|and Sir (['
        r'A-Z][a-z]+)|Sirs ([A-Z][a-z]+), ([A-Z][a-z]+)|Sirs ([A-Z][a-z]+)|([A-Z][a-z]+), ([A-Z][a-z]+) and ([A-Z][a-z]+)',
            line)
        for names in s:
            names = re.split(r'and |Sirs |Sir |, | ', names.group())
            for name in names:
                if len(name):
                    for n in states2:
                        if name not in n and name not in fakenames:
                            flagt=1
                            people.append(name)
                            words.append(n)
                    if flagt==1:
                        flagt=0
                        break
                    for n in states:
                        if name not in n and name not in fakenames:
                            people.append(name)
                            words.append(n)
    states = []
    states2 = []


def judges(resultlist, word, people, namelist):
    word = re.sub(' I ', ' Sir ' + people+' ', word)
    word = re.sub('I,', 'Sir ' + people+',', word)
    if resultlist:
        if j1 in word:
            resultlist = []
            return resultlist
        if re.findall(r'(.*) or (.*) is a Knave', word):
            setr1 = set()
            index1 = namelist.index(people)
            index2 = []
            s = re.finditer(
                r'Sir ([A-Z][a-z]+)| Sir ([A-Z][a-z]+) and ([A-Z][a-z]+)|Sir ([A-Z][a-z]+), Sir ([A-Z][a-z]+)|and Sir ([A-Z][a-z]+)',
                word)
            for names in s:
                names = re.split(r'and |Sirs |Sir |, ', names.group())
                for name in names:
                    if name != '' and name != ' ':
                        index2.append(namelist.index(name))
            if index1 in index2:
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for j in range(0, len(list_r1)):
                    listr1 = list(list_r1[j])
                    listr1[index1] = 0
                    setr1.add(tuple(listr1))
                resultlist = list(set(resultlist) - setr1)
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for j in range(0, len(list_r1)):
                    listr1 = list(list_r1[j])
                    listr1[index1] = 1
                    for p in range(0, len(index2)):
                        listr1[index2[p]] = 1
                    setr1.add(tuple(listr1))
                resultlist = list(set(resultlist) - setr1)
                return resultlist
            else:
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 1
                    for j in range(0, len(index2)):
                        listr1[index2[j]] = 1
                    setr1.add(tuple(listr1))
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 0
                    flag=0
                    for j in range(0, len(index2)):
                        if listr1[index2[j]] == 0:
                            flag+=1
                    if flag!=0:
                        setr1.add(tuple(listr1))
                resultlist = list(set(resultlist) - setr1)
                return resultlist

        if re.findall(r'(.*) or (.*) is a Knight', word):
            setr1 = set()
            setr2 = set()
            index1 = namelist.index(people)
            index2 = []
            s = re.finditer(
                r'Sir ([A-Z][a-z]+)| Sirs ([A-Z][a-z]+) and ([A-Z][a-z]+)|Sir ([A-Z][a-z]+), Sir ([A-Z][a-z]+)|and Sir ([A-Z][a-z]+)',
                word)
            for names in s:
                names = re.split(r'and |Sirs |Sir |, ', names.group())
                for name in names:
                    if name != '' and name != ' ':
                        index2.append(namelist.index(name))
            if index1 in index2:
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for j in range(0, len(list_r1)):
                    listr1 = list(list_r1[j])
                    listr1[index1] = 0
                    for i in range(0, len(index2)):
                        if listr1[index2[i]] == 0:
                            setr1.add(tuple(listr1))
                            break
                resultlist = list(set(resultlist) - setr1)
                return resultlist
            else:
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 0
                    for q in range(0, len(index2)):
                        if listr1[index2[q]] == 1:
                            setr1.add(tuple(listr1))
                            break
                resultlist = list(set(resultlist) - setr1)
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 1
                    for j in range(0, len(index2)):
                        listr1[index2[j]] = 0
                    setr2.add(tuple(listr1))
                resultlist = list(set(resultlist) - setr2)
                return resultlist
        if j2 in word:
            return resultlist

        if re.findall(r'Sir (.*) and (.*) are Knights', word):
            setr1 = set()
            setr2 = set()
            index1 = namelist.index(people)
            index2 = []
            s =re.finditer(r'Sir ([A-Z][a-z]+)| Sirs ([A-Z][a-z]+) and ([A-Z][a-z]+)|Sir ([A-Z][a-z]+), Sir ([A-Z][a-z]+)|and Sir ([A-Z][a-z]+)',word)
            for names in s:
                names = re.split(r'and |Sirs |Sir |, ', names.group())
                for name in names:
                    if name != '' and name != ' ':
                        index2.append(namelist.index(name))
            if index1 in index2:
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for j in range(0, len(list_r1)):
                    listr1 = list(list_r1[j])
                    listr1[index1] = 1
                    for i in range(0, len(index2)):
                        if listr1[index2[i]] == 0:
                            setr1.add(tuple(listr1))
                            break
                resultlist = list(set(resultlist) - setr1)
                return resultlist
            else:
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 0
                    flag = 0
                    for q in range(0, len(index2)):
                        if listr1[index2[q]] == 1:
                            flag += 1
                        if flag == len(index2):
                            setr1.add(tuple(listr1))
                            break
                resultlist = list(set(resultlist) - setr1)
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 1
                    for j in range(0, len(index2)):
                        if listr1[index2[j]] == 0:
                            setr2.add(tuple(listr1))
                            break
                resultlist = list(set(resultlist) - setr2)
                return resultlist
        if re.findall(r'Sir (.*) and (.*) are Knaves', word):
            setr1 = set()
            setr2 = set()
            index1 = namelist.index(people)
            index2 = []
            s = re.finditer(
                r'Sir ([A-Z][a-z]+)| Sirs ([A-Z][a-z]+) and ([A-Z][a-z]+)|Sir ([A-Z][a-z]+), Sir ([A-Z][a-z]+)|and Sir ([A-Z][a-z]+)',
                word)
            for names in s:
                names = re.split(r'and |Sirs |Sir |, ', names.group())
                for name in names:
                    if name != '' and name != ' ':
                        index2.append(namelist.index(name))
            if index1 in index2:
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 1
                    setr1.add(tuple(listr1))
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 0
                    for q in range(0, len(index2)):
                        listr1[index2[q]] = 0
                    setr1.add(tuple(listr1))
                resultlist = list(set(resultlist) - setr1)
                return resultlist
            else:
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 1
                    for q in range(0, len(index2)):
                        if listr1[index2[q]] == 1:
                            setr1.add(tuple(listr1))
                            break
                resultlist = list(set(resultlist) - setr1)
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 0
                    flag = 0
                    for j in range(0, len(index2)):
                        if listr1[index2[j]] == 0:
                            flag += 1
                        if flag == len(index2):
                            setr2.add(tuple(listr1))
                            break
                resultlist = list(set(resultlist) - setr2)
                return resultlist
        if j5 in word:
            setr1 = set()
            index1 = namelist.index(people)
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for j in range(0, len(list_r1)):
                listr1 = list(list_r1[j])
                listr1[index1] = 1
                for i in range(0, len(namelist)):
                    if listr1[i] == 0:
                        setr1.add(tuple(listr1))
                        break
            resultlist = list(set(resultlist) - setr1)
            return resultlist
        if j6 in word:
            setr1 = set()
            index1 = namelist.index(people)
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for j in range(0, len(list_r1)):
                listr1 = list(list_r1[j])
                listr1[index1] = 1
                setr1.add(tuple(listr1))
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for j in range(0, len(list_r1)):
                listr1 = list(list_r1[j])
                listr1[index1] = 0
                for i in range(0, len(namelist)):
                    listr1[i]=0
                setr1.add(tuple(listr1))
            resultlist = list(set(resultlist)- setr1)
            return resultlist

        if re.findall(r't most one of us is a Knight', word):
            setr1 = set()
            setr2 = set()
            index1 = namelist.index(people)
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for j in range(0, len(list_r1)):
                flag = 0
                listr1 = list(list_r1[j])
                listr1[index1] = 1
                for i in range(0, len(namelist)):
                    if listr1[i] != 0:
                        flag += 1
                if flag > 1:
                    setr1.add(tuple(listr1))
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for j in range(0, len(list_r1)):
                listr1 = list(list_r1[j])
                listr1[index1] = 0
                flag = 0
                for i in range(0, len(namelist)):
                    if listr1[i] == 1:
                        flag += 1
                if flag <= 1:
                    setr2.add(tuple(listr1))
            resultlist = list(set(resultlist) - setr2 - setr1)
            return resultlist

        if re.findall(r't most one of us is a Knave', word):
            setr1 = set()
            setr2 = set()
            index1 = namelist.index(people)
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for j in range(0, len(list_r1)):
                flag = 0
                listr1 = list(list_r1[j])
                listr1[index1] = 1
                for i in range(0, len(namelist)):
                    if listr1[i] == 0:
                        flag += 1
                if flag > 1:
                    setr1.add(tuple(listr1))
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for j in range(0, len(list_r1)):
                flag = 0
                listr1 = list(list_r1[j])
                listr1[index1] = 0
                for i in range(0, len(namelist)):
                    if listr1[i] == 0:
                        flag += 1
                if flag <= 1:
                    setr2.add(tuple(listr1))
            resultlist = list(set(resultlist) - setr1 - setr2)
            return resultlist
        if re.findall(r't most one of Sir (.*) is a Knave', word):
            setr1 = set()
            setr2 = set()
            index1 = namelist.index(people)
            index2 = []
            s = re.finditer(
                r'Sir ([A-Z][a-z]+)| Sirs ([A-Z][a-z]+) and ([A-Z][a-z]+)|Sir ([A-Z][a-z]+), Sir ([A-Z][a-z]+)|and Sir ([A-Z][a-z]+)',
                word)
            for names in s:
                names = re.split(r'and |Sirs |Sir |, ', names.group())
                for name in names:
                    if name != '' and name != ' ':
                        index2.append(namelist.index(name))
            if index1 in index2:
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 1
                    flag = 0
                    for q in range(0, len(index2)):
                        if listr1[index2[q]] == 0:
                            flag += 1
                        if flag > 1:
                            setr1.add(tuple(listr1))
                            break
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 0
                    flag = 0
                    for q in range(0, len(index2)):
                        if listr1[index2[q]] == 0:
                            flag += 1
                        if flag <= 1:
                            setr1.add(tuple(listr1))
                            break
                resultlist = list(set(resultlist) - setr1)
                return resultlist
            else:
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 1
                    flag = 0
                    for q in range(0, len(index2)):
                        if listr1[index2[q]] == 0:
                            flag += 1
                        if flag > 1:
                            setr1.add(tuple(listr1))
                            break
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 0
                    flag = 0
                    for j in range(0, len(index2)):
                        if listr1[index2[j]] == 0:
                            flag += 1
                        if flag <= 1:
                            setr1.add(tuple(listr1))
                            break
                resultlist = list(set(resultlist) - setr1)
                return resultlist
        if re.findall(r't most one of Sir (.*) is a Knight', word):
            setr1 = set()
            index1 = namelist.index(people)
            index2 = []
            s = re.finditer(
                r'Sir ([A-Z][a-z]+)| Sirs ([A-Z][a-z]+) and ([A-Z][a-z]+)|Sir ([A-Z][a-z]+), Sir ([A-Z][a-z]+)|and Sir ([A-Z][a-z]+)',
                word)
            for names in s:
                names = re.split(r'and |Sirs |Sir |, ', names.group())
                for name in names:
                    if name != '' and name != ' ':
                        index2.append(namelist.index(name))
            if index1 in index2:
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 1
                    flag = 0
                    for q in range(0, len(index2)):
                        if listr1[index2[q]] == 1:
                            flag+=1
                    if flag>1:
                        setr1.add(tuple(listr1))
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 0
                    flag = 0
                    for q in range(0, len(index2)):
                        if listr1[index2[q]] == 1:
                            flag += 1
                    if flag <= 1:
                        setr1.add(tuple(listr1))
                resultlist = list(set(resultlist) - setr1)
                return resultlist
            else:
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 1
                    flag = 0
                    for q in range(0, len(index2)):
                        if listr1[index2[q]] == 1:
                            flag += 1
                    if flag > 1:
                        setr1.add(tuple(listr1))
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 0
                    flag = 0
                    for j in range(0, len(index2)):
                        if listr1[index2[j]] == 1:
                            flag += 1
                    if flag <= 1:
                        setr1.add(tuple(listr1))
                resultlist = list(set(resultlist) - setr1)
                return resultlist
        if re.findall(r't least one of us is a Knight', word):
            setr1 = set()
            index1 = namelist.index(people)
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for j in range(0, len(list_r1)):
                flag = 0
                listr1 = list(list_r1[j])
                listr1[index1] = 0
                for i in range(0, len(namelist)):
                    if listr1[i] == 1:
                        flag += 1
                if flag >= 1:
                    setr1.add(tuple(listr1))
            resultlist = list(set(resultlist) - setr1)
            return resultlist
        if re.findall(r't least one of us is a Knave', word):
            setr1 = set()
            setr2 = set()
            index1 = namelist.index(people)
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for j in range(0, len(list_r1)):
                flag = 0
                listr1 = list(list_r1[j])
                listr1[index1] = 1
                for i in range(0, len(namelist)):
                    if listr1[i] == 0:
                        flag += 1
                if flag < 1:
                    setr1.add(tuple(listr1))
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for j in range(0, len(list_r1)):
                flag = 0
                listr1 = list(list_r1[j])
                listr1[index1] = 0
                for i in range(0, len(namelist)):
                    if listr1[i] == 0:
                        flag += 1
                if flag >= 1:
                    setr2.add(tuple(listr1))
            resultlist = list(set(resultlist) - setr1 - setr2)
            return resultlist

        if re.findall(r't least one of Sir (.*) is a Knave', word):
            setr1 = set()
            index1 = namelist.index(people)
            index2 = []
            s = re.finditer(
                r'Sir ([A-Z][a-z]+)| Sirs ([A-Z][a-z]+) and ([A-Z][a-z]+)|Sir ([A-Z][a-z]+), Sir ([A-Z][a-z]+)|and Sir ([A-Z][a-z]+)',
                word)
            for names in s:
                names = re.split(r'and |Sirs |Sir |, ', names.group())
                for name in names:
                    if name != '' and name != ' ':
                        index2.append(namelist.index(name))
            if index1 in index2:
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 1
                    flag = 0
                    for q in range(0, len(index2)):
                        if listr1[index2[q]] == 0:
                            flag += 1
                    if flag < 1:
                        setr1.add(tuple(listr1))
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 0
                    setr1.add(tuple(listr1))
                resultlist = list(set(resultlist) - setr1)
                return resultlist
            else:
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 1
                    flag = 0
                    for q in range(0, len(index2)):
                        if listr1[index2[q]] == 0:
                            flag += 1
                    if flag < 1:
                        setr1.add(tuple(listr1))
                list_r1 = list(product([0, 1], repeat=len(namelist)))
                for i in range(0, len(list_r1)):
                    listr1 = list(list_r1[i])
                    listr1[index1] = 0
                    flag = 0
                    for q in range(0, len(index2)):
                        if listr1[index2[q]] == 0:
                            flag += 1
                    if flag >= 1:
                        setr1.add(tuple(listr1))
                resultlist = list(set(resultlist) - setr1)
                return resultlist
        if re.findall(r't least one of Sir (.*) is a Knight', word):
            setr1 = set()
            index1 = namelist.index(people)
            index2 = []
            s = re.finditer(
                r'Sir ([A-Z][a-z]+)| Sirs ([A-Z][a-z]+) and ([A-Z][a-z]+)|Sir ([A-Z][a-z]+), Sir ([A-Z][a-z]+)|and Sir ([A-Z][a-z]+)',
                word)
            for names in s:
                names = re.split(r'and |Sirs |Sir |, ', names.group())
                for name in names:
                    if name != '' and name != ' ':
                        index2.append(namelist.index(name))
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for i in range(0, len(list_r1)):
                listr1 = list(list_r1[i])
                listr1[index1] = 1
                flag = 0
                for q in range(0, len(index2)):
                    if listr1[index2[q]] == 1:
                        flag += 1
                if flag < 1:
                    setr1.add(tuple(listr1))
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for i in range(0, len(list_r1)):
                listr1 = list(list_r1[i])
                listr1[index1] = 0
                flag = 0
                for q in range(0, len(index2)):
                    if listr1[index2[q]] == 1:
                        flag += 1
                if flag >= 1:
                    setr1.add(tuple(listr1))
            resultlist = list(set(resultlist) - setr1)
            return resultlist

        if re.findall(r'xactly one of Sir (.*) is a Knight', word):
            setr1 = set()
            index1 = namelist.index(people)
            index2 = []
            s = re.finditer(
                r'Sir ([A-Z][a-z]+)| Sirs ([A-Z][a-z]+) and ([A-Z][a-z]+)|Sir ([A-Z][a-z]+), Sir ([A-Z][a-z]+)|and Sir ([A-Z][a-z]+)',
                word)
            for names in s:
                names = re.split(r'and |Sirs |Sir |, ', names.group())
                for name in names:
                    if name != '' and name != ' ':
                        index2.append(namelist.index(name))
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for i in range(0, len(list_r1)):
                listr1 = list(list_r1[i])
                listr1[index1] = 1
                flag = 0
                for q in range(0, len(index2)):
                    if listr1[index2[q]] == 1:
                        flag += 1
                if flag != 1:
                    setr1.add(tuple(listr1))
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for i in range(0, len(list_r1)):
                listr1 = list(list_r1[i])
                listr1[index1] = 0
                flag = 0
                for q in range(0, len(index2)):
                    if listr1[index2[q]] == 1:
                        flag += 1
                if flag == 1:
                    setr1.add(tuple(listr1))
            resultlist = list(set(resultlist) - setr1)
            return resultlist

        if re.findall(r'xactly one of us is a Knight', word):
            setr1 = set()
            setr2 = set()
            index1 = namelist.index(people)
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for j in range(0, len(list_r1)):
                flag = 0
                listr1 = list(list_r1[j])
                listr1[index1] = 1
                for i in range(0, len(namelist)):
                    if listr1[i] == 1:
                        flag += 1
                if flag != 1:
                    setr1.add(tuple(listr1))
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for j in range(0, len(list_r1)):
                flag = 0
                listr1 = list(list_r1[j])
                listr1[index1] = 0
                for i in range(0, len(namelist)):
                    if listr1[i] == 1:
                        flag += 1
                if flag == 1:
                    setr2.add(tuple(listr1))
            resultlist = list(set(resultlist) - setr1 - setr2)
            return resultlist

        if re.findall(r'xactly one of us is a Knave', word):
            setr1 = set()
            setr2 = set()
            index1 = namelist.index(people)
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for j in range(0, len(list_r1)):
                flag = 0
                listr1 = list(list_r1[j])
                listr1[index1] = 1
                for i in range(0, len(namelist)):
                    if listr1[i] == 0:
                        flag += 1
                if flag != 1:
                    setr1.add(tuple(listr1))
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for j in range(0, len(list_r1)):
                flag = 0
                listr1 = list(list_r1[j])
                listr1[index1] = 0
                for i in range(0, len(namelist)):
                    if listr1[i] == 0:
                        flag += 1
                if flag == 1:
                    setr2.add(tuple(listr1))
            resultlist = list(set(resultlist) - setr1 - setr2)
            return resultlist

        if re.findall(r'xactly one of Sir (.*) is a Knave', word):
            setr1 = set()
            setr2 = set()
            index1 = namelist.index(people)
            index2 = []
            s = re.finditer(
                r'Sir ([A-Z][a-z]+)| Sirs ([A-Z][a-z]+) and ([A-Z][a-z]+)|Sir ([A-Z][a-z]+), Sir ([A-Z][a-z]+)|and Sir ([A-Z][a-z]+)',
                word)
            for names in s:
                names = re.split(r'and |Sirs |Sir |, ', names.group())
                for name in names:
                    if name != '' and name != ' ':
                        index2.append(namelist.index(name))
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for i in range(0, len(list_r1)):
                listr1 = list(list_r1[i])
                listr1[index1] = 1
                flag = 0
                for q in range(0, len(index2)):
                    if listr1[index2[q]] == 0:
                        flag += 1
                if flag != 1:
                    setr1.add(tuple(listr1))
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for i in range(0, len(list_r1)):
                listr1 = list(list_r1[i])
                listr1[index1] = 0
                flag = 0
                for q in range(0, len(index2)):
                    if listr1[index2[q]] == 0:
                        flag += 1
                if flag == 1:
                    setr1.add(tuple(listr1))
            resultlist = list(set(resultlist) - setr1)
            return resultlist
        if j3 in word:
            setr1 = set()
            setr2 = set()
            index1 = namelist.index(people)
            s = re.finditer(
                r'Sir ([A-Z][a-z]+)| Sirs ([A-Z][a-z]+) and ([A-Z][a-z]+)|Sir ([A-Z][a-z]+), Sir ([A-Z][a-z]+)|and Sir ([A-Z][a-z]+)',
                word)
            for names in s:
                names = re.split(r'and |Sirs |Sir |, ', names.group())
                for name in names:
                    if name != '' and name != ' ':
                        index2 = namelist.index(name)
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for j in range(0, len(list_r1)):
                listr1 = list(list_r1[j])
                listr1[index1] = 1
                listr1[index2] = 0
                setr1.add(tuple(listr1))
            list_r2 = list(product([0, 1], repeat=len(namelist)))
            for j in range(0, len(list_r2)):
                listr2 = list(list_r2[j])
                listr2[index1] = 0
                listr2[index2] = 1
                setr2.add(tuple(listr2))
            resultlist = list(set(resultlist) - setr2 - setr1)
            return resultlist
        if j4 in word:
            setr1 = set()
            setr2 = set()
            index1 = namelist.index(people)
            s = re.finditer(r'Sir ([A-Z][a-z]+)| Sirs ([A-Z][a-z]+) and ([A-Z][a-z]+)|Sir ([A-Z][a-z]+), Sir ([A-Z][a-z]+)|and Sir ([A-Z][a-z]+)',word)
            for names in s:
                names = re.split(r'and |Sirs |Sir |, ', names.group())
                for name in names:
                    if name != '' and name != ' ':
                        index2 = namelist.index(name)
            list_r1 = list(product([0, 1], repeat=len(namelist)))
            for j in range(0, len(list_r1)):
                listr1 = list(list_r1[j])
                listr1[index1] = 1
                listr1[index2] = 1
                setr1.add(tuple(listr1))
            list_r2 = list(product([0, 1], repeat=len(namelist)))
            for j in range(0, len(list_r2)):
                listr2 = list(list_r2[j])
                listr2[index1] = 0
                listr2[index2] = 0
                setr2.add(tuple(listr2))
            resultlist = list(set(resultlist) - setr2 - setr1)
            return resultlist

    else:
        return resultlist


resultlist = list(product([0, 1], repeat=len(namelist)))
for i in range(0, len(words)):
    resultlist = judges(resultlist, words[i], people[i], namelist)

print('The Sirs are:', end='')
for i in range(0, len(namelist)):
    if namelist[i] != '' and namelist[i] != ' ':
        print(' ' + namelist[i], end='')

if resultlist:
    if len(resultlist) > 1:
        print('\nThere are ' + str(len(resultlist)) + ' solutions.')
    else:
        print('\nThere is a unique solution:')
        for i in range(0, len(resultlist)):
            for j in range(0, len(namelist)):
                if resultlist[i][j] == 1:
                    print('Sir ' + namelist[j] + ' is a Knight.')
                if resultlist[i][j] == 0:
                    print('Sir ' + namelist[j] + ' is a Knave.')
else:
    print('\nThere is no solution.')
