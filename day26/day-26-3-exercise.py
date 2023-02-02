with open("file1.txt") as file1:
    content1 = file1.readlines()
    content1 = [x.strip() for x in content1]

with open("file2.txt") as file2:
    content2 = file2.readlines()
    content2 = [x.strip() for x in content2]

# result = []
# for num1 in content1:
#     for num2 in content2:
#         if num1 == num2:
#             result.append(num1)

result = [num1 for num1 in content1 if num1 in content2]

print(result)