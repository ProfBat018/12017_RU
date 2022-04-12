text = "Hello?????. My name is Elvin...... My!  surname is.     "
sentence = 0

if text != '':
    sentence = 1


chars = ['.', '!', '?']
state = False
i = 0
j = 0

text = text.lstrip()
text = text.rstrip()

while i < len(text) - 1:
    j = 0
    while j < len(chars):
        if text[i] == chars[j]:
            for k in range(i, len(text)):
                if text[k].isalnum():
                    state = True
                    break
                else:
                    state = False
            if state:
                sentence += 1
        j += 1
        while not text[i].isalnum():
            i += 1
            j = 0
    i += 1

sentence += 1
print(sentence)


