words = input()
c_word = ["c=","c-","dz=","d-","lj","nj","s=","z="]

c_word_count = 0
for word in c_word:
    if word in words:
        while word in words:
            words = words.replace(word," ",1)
            c_word_count+=1

total = len(words.replace(" ","")) + c_word_count

print(total)