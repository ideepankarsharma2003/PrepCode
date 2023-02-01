# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    d= dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score not in d:
            d[score]= [name]
        else:
            d[score].append(name)
    
    # print(f'd= {d}')
    
    l= list(d.keys())
    l.sort()
    
    ansKey= l[1]
    # print(f'ansKey= {ansKey}')
    
    ans= d[ansKey]
    ans.sort()
    # print(f'ans= {ans}')
    
    
    for i in ans:
        print(i)
    
    
        
    