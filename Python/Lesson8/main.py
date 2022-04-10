# Пользователь вводит текст. Затем пользователь вводит слова,
# если в тексте есть эти слова, то сделать их большими

text = "hello my dear @$friends.)"

words = input("Enter words: ")  # string

words = words.split()   # list
tmp = ''



# for i in range(len(list_from_text)):
#     for j in range(len(words)):
#         if list_from_text[i].count(words[j]) > 0:
#             for item in list_from_text[i]:
#                 for word in words[j]:
#                     if item != word:
#                         if item.isalpha():
#                             tmp += item.upper()
#                             break
#                         tmp += item
#                         break
#                     else:
#                         tmp += word.upper()
#                         break
#             list_from_text[i] = tmp


# for i in range(len(list_from_text)):
#     for j in range(len(words)):
#         if list_from_text[i].count(words[j]) > 0:
#             list_from_text[i] = list_from_text[i].upper()




