


transactions = [
    ['curd', 'sour cream'], ['curd', 'orange', 'sour cream'], ['bread', 'cheese', 'butter'], ['bread', 'butter'], ['bread', 'milk'],
    ['apple', 'orange', 'pear'], ['bread', 'milk', 'eggs'], ['tea', 'lemon'], ['curd', 'sour cream', 'apple'], ['eggs', 'wheat flour', 'milk'],
    ['pasta','cheese'], ['bread', 'cheese'],
    ['pasta', 'olive oil', 'cheese'], ['curd', 'jam'], ['bread', 'cheese', 'butter'], ['bread', 'sour cream', 'butter'],
    ['strawberry', 'sour cream'], ['curd', 'sour cream'], ['bread', 'coffee'], ['onion', 'garlic']
]

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

encoder = TransactionEncoder()
encoded_array = encoder.fit(transactions).transform(transactions)

df_itemsets = pd.DataFrame(encoded_array, columns=encoder.columns_)

print(df_itemsets)

print("====================")

print('Number of transaction: ', len(transactions))
print('Number of unique items: ', len(set(sum(transactions, []))))

print("========== Определение часто встречающихся наборов =========")

from mlxtend.frequent_patterns import apriori
frequent_itemsets = apriori(df_itemsets, min_support=0.1, use_colnames=True)
print(frequent_itemsets)
print("====================")

frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda itemset: len(itemset))

print(frequent_itemsets[frequent_itemsets['length'] >= 2])

print("====================")

print("========== Генеррирование ассоциативных правил =========")
print()
from mlxtend.frequent_patterns import association_rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

print(rules.iloc[:, 0:7])

print("====================")
print("========== Визуализация ассоциативных правил =========")
print()

rules_plot = pd.DataFrame()
rules_plot['antecedents'] = rules['antecedents'].apply(lambda x: ','.join(list(x)))
rules_plot['consequents'] = rules['consequents'].apply(lambda x: ','.join(list(x)))

rules_plot['lift'] = rules['lift'].apply(lambda x: round(x, 2))

pivot = rules_plot.pivot(index = 'antecedents', columns = 'consequents', values= 'lift')
print(pivot)

antecedents = list(pivot.index.values)
consequents = list(pivot.columns)

import numpy as np
pivot = pivot.to_numpy()

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

im = ax.imshow(pivot, cmap = 'Reds')

ax.set_xticks(np.arange(len(consequents)))
ax.set_yticks(np.arange(len(antecedents)))

ax.set_xticklabels(consequents)
ax.set_yticklabels(antecedents)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

for i in range(len(antecedents)):
    for j in range(len(consequents)):
        if not np.isnan(pivot[i, j]):
            text = ax.text(j, i, pivot[i, j], ha="center", va="center")

ax.set_title("Lift metric for frequent itemsets")
fig.tight_layout()
#plt.show()


print("====================")
print("========== Получение полезных инсайтов из ассоциативных правил =========")

butter_antecedent = rules[rules['antecedents'] == {'butter'}][['consequents', 'confidence']].sort_values('confidence', ascending = False)

butter_consequents = [list(item) for item in butter_antecedent.iloc[0:3:,]['consequents']]
item = 'butter'
print('Item frequently bought together with', item, 'are:', butter_consequents)

print("====================")
print("========== Плаирование скидок на основе ассоциативных правил =========")
print()
from functools import reduce
rules['itemsets'] = rules[['antecedents', 'consequents']].apply(lambda x: reduce(frozenset.union, x), axis=1)

print(rules[['antecedents', 'consequents', 'itemsets']])
print("====================")
rules.drop_duplicates(subset=['itemsets'], keep='first', inplace=True)
print(rules['itemsets'])
print("====================")

discounted = []
others = []
for itemset in rules['itemsets']:
    for i, item in enumerate(itemset):
        if item not in others:
            discounted.append(item)
            itemset = set(itemset)
            itemset.discard(item)
            others.extend(itemset)
            break
        if i == len(itemset)-1:
            discounted.append(item)
            itemset = set(itemset)
            itemset.discard(item)
        others.extend(itemset)
print(discounted)
print("-----------------------------------")
print(list(set(discounted)))












