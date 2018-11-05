takahashi_voice = input()
list = ['a','i','u','e','o']


translator=str.maketrans(dict.fromkeys(list, ''))


print(takahashi_voice.translate(translator))


