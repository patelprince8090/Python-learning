def percent(marks):
    p=((marks[0]+marks[1]+marks[2])/100)*50
    return p

marks1 = [10,20,50,40]
percentage1 = percent(marks1)

marks2 = [15,22,25,45]
percentage2 = percent(marks2)
print(percentage1, percentage2)