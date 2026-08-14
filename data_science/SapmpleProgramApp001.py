

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

