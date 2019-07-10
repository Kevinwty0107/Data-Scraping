import csv
import re

def avsplit2(s, n):
    fn = len(s)//n
    rn = len(s)%n
    sr = []
    ix = 0
    for i in range(n):
        if i<rn:
            sr.append(s[ix:ix+fn+1])
            ix += fn+1
        else:
            sr.append(s[ix:ix+fn])
            ix += fn
    return sr


with open('/Users/wangtaiyi/Desktop/SummerInternship/CD2.csv','rt',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    column = [row[0] for row in reader]
    print (column)
    column2 = column[1:]
    print (column2)
    while '' in column2:
        column2.remove('')
    i=0
    newcolumn = list(range(3830))
    for c in column2:
        #print (c[2:10])
        newcolumn[i]=c[2:10]
        i=i+1
    print (newcolumn)
    print (len(newcolumn))
    for a in newcolumn:
        if isinstance(a,int):
            break
        #除定义分割函数外用,另一种方法去分割
        #b = re.findall(r'.{4}', a)
        #c = ','.join(b)
        #c = c.split(',')
        c = avsplit2(a, 2)
        print(c)
