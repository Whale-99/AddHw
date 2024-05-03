grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
lstudents = list(students)
slst = sorted(lstudents)
avgr = [sum(gr) / len(gr) for gr in grades]
favgr = [f"{avg:.2f}" for  avg in avgr]
pairs = [(x, y) for x, y in zip(slst, favgr)]
dic = dict(pairs)
print(dic)
