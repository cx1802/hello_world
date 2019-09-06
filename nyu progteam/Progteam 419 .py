'''
time1 = input()

h1 = int(time1[:2])
m1 = int(time1[time1.find(" ")+1:len(time1)])

if m1 >= 45 and m1 <= 60:
    time2 = str(h1) + " " + str(m1-45)
elif m1 >= 0 and m1 < 45:
    if h1 > 0 and h1 <= 23:
        time2 = str(h1-1) + " " + str(60+(m1-45))
    elif h1 == 0:
        time2 = str(23) + " " + str(60+(m1-45))

print(time2)
'''
'''
numbers = input()

number1 = numbers[:3]
number2 = numbers[4:]

new_number1 = int(number1[-1:-4:-1])
new_number2 = int(number2[-1:-4:-1])

if new_number1 < new_number2:
    print(new_number2)
else:
    print(new_number1)
'''

number_strings = int(input())
list_string = []
for i in range(number_strings):
    string = input()
    list_string += [string]


for string1 in list_string:
    repetition = 0
    for k in range(len(string1)):
        for l in range(k+1, len(string1)):
            if string1[k] == string1[l]:
                repetition += 1
    if repetition == 0:
        answer = "Yes"
        consecutive = 0
        for p in string1:
            for q in string1:
                if abs(ord(q) - ord(p)) >= len(string1):
                    consecutive -= 1
        if consecutive == 0:
            answer = "Yes"
        else:
            answer = "No"
    else:
        answer = "No"
    print(answer)
