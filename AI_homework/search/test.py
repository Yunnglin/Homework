class student:
    age = 10

    def __init__(self, age):
        self.age = age


list1 = [student(5), student(6)]
student1 = list1[0]
student1 = student(10)
print(list1)
