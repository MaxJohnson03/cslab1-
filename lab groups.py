total = input("What is the total number of students in the class?")
group = int(total) // 24
remainder = int(total) % 24
print("The total amount of full groups is", str(group))
print("The total amount of students left in the smaller group is", str(remainder))
