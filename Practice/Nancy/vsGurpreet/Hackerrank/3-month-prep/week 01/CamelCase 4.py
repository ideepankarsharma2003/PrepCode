# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
str = sys.stdin.readlines()
inp = []
# print(str)
for line in str:
    line = line.rstrip('\r\n')
    # print(line)
    sc = line[0]
    mvc = line[2]
    line = line[4:]
    if sc == 'S':
        if mvc == 'M':
            x = line[:-2]  # remove the ()
            line = ''
            for i in x:
                if i.isupper():
                    line += ' '
                    i = i.lower()
                line += i

        elif mvc == 'V':
            x = line
            line = ''
            for i in x:
                if i.isupper():
                    line += ' '
                    i = i.lower()
                line += i
        elif mvc == 'C':
            x = line[1:]  # not first letter, because it is always capital
            line = '' + line[0].lower()
            for i in x:
                if i.isupper():
                    line += ' '
                    i = i.lower()
                line += i
    else:
        wordList = line.split(' ')
        if mvc == 'V':
            line = ''
            line += wordList[0]
            for i in wordList[1:]:
                line += i.capitalize()
        elif mvc == 'M':
            line = ''
            line += wordList[0]
            for i in wordList[1:]:
                line += i.capitalize()
            line += '()'
        elif mvc == 'C':
            line = ''
            for i in wordList:
                line += i.capitalize()

    inp.append(line)

for i in inp:
    print(i)
