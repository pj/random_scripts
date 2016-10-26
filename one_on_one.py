from os import path
from random import randrange
import csv
from datetime import date

previous_pairs = set()

today = date.today()

if path.isfile("previous_pairs.csv"):
    with open("previous_pairs.csv", 'r') as f:
        pair_reader = csv.reader(f)
        for person_1, person_2, _ in pair_reader:
            previous_pairs.add((person_1, person_2))


people = open("people.txt", 'r').readlines()
people = map(lambda person: person.strip(), people)

new_pairs = set()

while people:
    if len(people) == 1:
        print("{0} has the day off.".format(people[0]))
        break
    person_1 = people.pop(randrange(0, len(people)))
    person_2 = people.pop(randrange(0, len(people)))
    new_pair = (person_1, person_2)

    if new_pair in previous_pairs:
        people.append(person_1)
        people.append(person_2)
    else:
        print("{0} {1}".format(person_1, person_2))
        new_pairs.add(new_pair)

with open("previous_pairs.csv", 'a') as f:
    pair_writer = csv.writer(f)
    for new_pair in new_pairs:
        pair_writer.writerow(new_pair + (today,))
