

txt = ''' Eight dollars a week or a million a year - what is the difference? A mathematician or a wit
would give you the wrong answer. The magi brought valuable gifts, but that was not among them. - Gift of the Magi, O'Henry 
'''

world_lists = [[w.replace(',', '') for w in line.split() if w not in ['-']] for line in txt.replace('?', '.').split('.')]

print(len(world_lists))

print(world_lists)
for arr in world_lists:
    print(arr)

#--------------------------------------------------------------------------------------------------------------------------------------------------------

arr01 = [2, 4, 7]
arr02 = ['Bob', 'John', 'Will']

regions = ['Asia', 'America', 'Europe']
# regions = []
test_list = []
test_list.append('Pay bills')
test_list.append('Tidy up')
test_list.append('Walk the dog')
test_list.append('Cook dinner')

print(test_list)
index = test_list.index('Walk the dog')
print(index)

test_list.insert(index, 'Go to the pharmacy')
test_list.insert(index, 'Tidy up')
print(test_list)
print(test_list.count('Tidy up'))

#SLice
print(test_list[0: 3])
print(test_list[3: ])

test_list[len(test_list):] = ['Mow the lawn', 'Water plants']
print(test_list)

#=======================================================================================================================================================
print("====== QUEUE =======")
print(test_list)

from collections import deque
queue = deque(test_list)
queue.append("Wash the car")
print(queue)
print(queue.popleft(), ' - Done!')
my_test_list = list(queue)
print(my_test_list)

#=======================================================================================================================================================
print("======= STACK ======")
my_list = ['Pay bills', 'Tidy up', 'Walk the dog', 'Cook dinner']

stack = []
for task in my_list:
    stack.append(task)

while stack:
    print(stack.pop(), ' - Done!')
print('\nThe stack is empty')

#=======================================================================================================================================================
print("======= NATURAL LANGUAGE ======")
# pip install -U spacy
# python -m spacy download en_core_web_sm

import spacy
txt = 'List is a ubiquitous data structure in the Python programming language.'

nlp = spacy.load('en_core_web_sm')
doc = nlp(txt)
stk = []

for w in doc:
    if w.pos_ == 'NOUN' or w.pos_ == 'PROPN':
        stk.append(w.text)
    elif (w.head.pos_ == 'NOUN' or w.head.pos_ == 'PROPN') and (w in w.head.lefts):
        stk.append(w.text)
    elif stk:
        chunk = ''
        while stk:
            chunk = stk.pop() + ' ' + chunk
        print(chunk.strip())

#=======================================================================================================================================================
# python -m spacy download en
print("======= NATURAL LANGUAGE 2 ======")
import spacy
txt = 'List is a ubiquitous data structure in the Python programming language.'
nlp = spacy.load('en_core_web_sm')
doc = nlp(txt)
for t in doc:
    print(t.text, t.head.text)

#=======================================================================================================================================================
# python -m spacy download en
print("======= NATURAL LANGUAGE 3 ======")
import spacy
txt = 'List is a ubiquitous data structure in the Python programming language.'
nlp = spacy.load("en")
doc = nlp(txt)
for t in doc:
    print(t.text, t.head.text)
















































































