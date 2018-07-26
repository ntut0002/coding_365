#input
name = input()
id = input()
chinese = input()
computer_science = input()
computer_programming = input()

#transform
chinese_score = int(chinese)
computer_science_score = int(computer_science)
computer_programming_score = int(computer_programming)

#math
Total = chinese_score + computer_science_score + computer_programming_score
Average = Total//3

#transform
str_Total = str(Total)
str_Average = str(Average)

print("Name:" + name)
print("Id:" + id)
print("Total:" + str_Total)
print("Average:" + str_Average)