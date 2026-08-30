# TEXT
# ======================================================================================================
print("==== MATH and TEXT =====")
text = "The oneperfectly divine thing, the oneglimpse of God's paradisegiven on earth. is to fight a losingbattle - and notlose it."

word_list = ['The', 'one', 'perfectly', 'divine']
word_list_copy = [word for word in word_list]

has_n = [word for word in word_list if 'n' in word]
print(has_n)

import re
locs = list(set([(m.start(), m.end()) for word in word_list for m in re.finditer(word, text)]))
# print(locs)

spacestarts = [m.start() for m in re.finditer(' ', text)]
spacestarts.append(-1)
spacestarts.append(len(text))
spacestarts.sort()

spacestarts_affine = [ss+1 for ss in spacestarts]
spacestarts_affine.sort()

between_spaces = [(spacestarts[k] + 1, spacestarts[k + 1]) for k in range(0, len(spacestarts) - 1)]
between_spaces_notvalid = [loc for loc in between_spaces if text[loc[0]:loc[1]] not in word_list]

print(between_spaces_notvalid)

print("==== NLTK =====")

import nltk
nltk.download('brown')
# корпус - набор действительных слов английского языка

from nltk.corpus import brown
wordlist = set(brown.words())
# [nltk_data] Error loading brown: <urlopen error [WinError 10060]
# [nltk_data]     Попытка установить соединение была безуспешной, т.к.
# [nltk_data]     от другого компьютера за требуемое время не получен
# [nltk_data]     нужный отклик, или было разорвано уже установленное
# [nltk_data]     соединение из-за неверного отклика уже подключенного
# [nltk_data]     компьютера>
# Traceback (most recent call last):

# Заблокированно

word_list = list(word_list)

word_list = [word.replace('*','') for word in word_list]
word_list = [word.replace('[','') for word in word_list]
word_list = [word.replace(']','') for word in word_list]
word_list = [word.replace('?','') for word in word_list]
word_list = [word.replace('.','') for word in word_list]
word_list = [word.replace('+','') for word in word_list]
word_list = [word.replace('/','') for word in word_list]
word_list = [word.replace(';','') for word in word_list]
word_list = [word.replace(':','') for word in word_list]
word_list = [word.replace(',','') for word in word_list]
word_list = [word.replace(')','') for word in word_list]
word_list = [word.replace('(','') for word in word_list]
word_list.remove('')

between_spaces_notvalid = [loc for loc in between_spaces if text[loc[0]:loc[1]] not in word_list]
print(between_spaces_notvalid)

partial_word = [loc for loc in locs if loc[0] in spacestarts_affine and loc[1] not in spacestarts]
print(partial_word)
partial_word_end = [loc for loc in locs if loc[0] not in spacestarts_affine and loc[1] in spacestarts]
print(partial_word_end)















