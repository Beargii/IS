import os

print(os.getcwd())

print(os.listdir("."))

os.makedirs('test_folder', exist_ok=True)

file_path = os.path.join('test_folder', 'example.txt')
print(file_path)

try:
    x = 10/0
except ZeroDivisionError:
    print("Cannot divide by Zero")