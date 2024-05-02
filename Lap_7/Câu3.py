text = '''My younger brother, Golu is very naughty. He is only four years old and study in nursery class.  He is the star of everyone’s eyes in our house. 
        He engages everyone with his naughty activities and funny talks. He imitates his grandfather and all break into laughter. 
        He is good at studies also. His class teacher is all praise for him. I love him very much.'''
text = text.lower()
print(text)
word_list = text.split()
word_count = {}
for i in range (len(word_list)):
    count = 0
    for j in range(len(word_list)):
        if word_list[i] == word_list[j]:
            count += 1
    word_count[word_list[i]]= count
tần_số_max = max(word_count , key =word_count.get )
tần_số_min = min(word_count , key = word_count.get)
print("Tần số xuất hiện nhiều nhất là :", tần_số_max)
print("Số lần từ xuất hiện là :", word_count[tần_số_max])
print("Tần Số xuất hiện ít nhất là :",tần_số_min)
print("Số lần từ xuất hiện là :", word_count[tần_số_min])


