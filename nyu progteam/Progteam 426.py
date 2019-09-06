'''

A

integers = input()

r1 = int(integers[:integers.find(" ")])
s = int(integers[integers.find(" ")+1:])

r2 = 2*s - r1

print(r2)
'''

'''
B
'''
'''
num_students = int(input())

students_scores = []
for i in range(num_students):
    scores = input()
    score1 = int(scores[:scores.find(" ")])
    scores = scores[scores.find(" ")+1:]
    score2 = int(scores[:scores.find(" ")])
    scores = scores[scores.find(" ")+1:]
    score3 = int(scores[:scores.find(" ")])
    score4 = int(scores[scores.find(" ")+1:])
    sum_scores = score1 + score2 + score3 + score4
    students_scores += [sum_scores]

rank = 1
for j in students_scores:
    if j > students_scores[0]:
        rank += 1
    
print(rank)
'''
'''
C
'''
'''
num_chapters = int(input())

end_pages = []
for i in range(num_chapters):
    pages = input()
    end = int(pages[pages.find(" ")+1:])
    end_pages += [end]


index_page = int(input())

for j in range(len(end_pages)):
    if index_page <= end_pages[j]:
        read_chapter = j
        break

print(num_chapters - read_chapter)
'''
'''
D
'''
'''
p_integers = []
while True:
    N = input()
    if int(N) == 0:
        break
    sum_digits_N = 0
    for i in N:
        sum_digits_N += int(i)
    p = 11
    while True:
        Np = str(int(N) * p)
        sum_digits_Np = 0
        for j in Np:
            sum_digits_Np += int(j)
        if sum_digits_Np == sum_digits_N:
            break
        p += 1
    p_integers += [p]

for k in p_integers:
    print(k)
'''

'''
F
'''

setting = input()

n = int(setting[:setting.find(" ")])
k = int(setting[setting.find(" ")+1:])

tree = []
clutters = 0
for i in range(n-1):
    edges = input()
    start = int(edges[:edges.find(" ")])
    end = int(edges[edges.find(" ")+1:len(edges)-2])
    color = int(edges[len(edges)-1:])
    if color == 0:
        if start in tree:
            tree.insert(tree.index(start), end)
        elif end in tree:
            tree.insert(tree.index(end), start)
        else:
            tree += [start] + [end] + [" "]
            clutters += 1

not_good = 0
for j in range(clutters):
    n_vertices = len(tree[:tree.index(" ")])
    not_good += n_vertices ** k - n_vertices
    for i in tree[:tree.index(" ")]:
        tree.remove(i)
    tree.remove(" ")

good = n ** k - not_good - n

print(good)



