#Task 1

import re

with open('task1-ru.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words_dot = re.findall(r'\b[а-яА-ЯёЁa-zA-Z]+\b(?=\.)', text)

numbers = re.findall(r'\b\d+\,\d+\b', text)

print("Слова, после которых стоит точка:")
print(words_dot)

print("Дробные числа:")
print(numbers)

#Task 2

with open('task2.html', 'r', encoding='utf-8') as file:
    text = file.read()

pixel = re.findall(r'\b\d+px\b', text)

print("Значения в пикселях:")
print(pixel)

#Task 3

import csv


with open("task3.txt", "r", encoding="utf-8") as f:
    content = f.read()

ids = re.findall(r"\b\d+\b", content)
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)
dates = re.findall(r"\d{4}-\d{2}-\d{2}", content)
urls = re.findall(r"https?://[^\s]+", content)
names = re.findall(r"\b[A-Z][a-z]+(?: [A-Z][a-z]+)?\b", content)

table = list(zip(ids, names, emails, dates, urls))

table_sorted = sorted(table, key=lambda x: int(x[0]))

with open("Output3.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ID", "Фамилия", "Email", "Дата", "Сайт"])
    writer.writerows(table_sorted)

#Extra task

with open('task_add.txt', 'r', encoding='utf-8') as file:
    content = file.read()

dates = re.findall(r"\b(\d{2,4}[./-]\d{2,4}[./-]\d{2,4})", content)
emails = re.findall(r'\s([\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,})', content)
adresses = re.findall(r'\s(https?://[a-zA-Z0-9.-]+)', content)

if dates[:5]:
    print("Dates:")
    for date in dates:
        print(f'  {date}')

if emails[:5]:
    print("Emails:")
    for email in emails:
        print(f'  {email}')

if adresses[:5]:
    print("Webs:")
    for adress in adresses:
        print(f'  {adress}')