def student_report(**kwargs):
    total = 0
    for k,v in kwargs.items():
        print(k,v)
        total += v
    return len(kwargs), total/len(kwargs)

print(student_report(rohan=50,geeta=30,shruti=15))
print(student_report(harsh=100,himanshu=70,yash=75))