names=["moez","omar","ahmed"]
marks=[]
course_work=[]

import random
for  i in names:
    x=random.randint(0,60)
    y=random.randint(0,30)
    course_work.append(y)
    marks.append(x)
for i in range(3):
    print(f"{names[i]} get {marks[i]} his course work is {course_work[i]}")