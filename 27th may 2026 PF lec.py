marks=[]

count=1

while count <= 10:
    m=int(input("Enter Marks: "))
    marks.append(m)

    count = count + 1

print(marks)

#finding the maximum
#assume first data in the list is the starting maximum

max = marks[0]

i = 1

while i < 10:
    if marks [i] > max:
        max = marks [i]

    i = i + 1

print("Maximum mark is: ", max)
