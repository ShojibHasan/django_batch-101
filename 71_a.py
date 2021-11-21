# 4
# word [0]
# localization [1]
# internationalization [2]
# pneumonoultramicroscopicsilicovolcanoconiosis [3]
# word =['word','localization','internationalization','pneumonoultramicroscopicsilicovolcanoconiosis']





def wayTooLongWords(words):
    for i in range(len(words)):  # 4 // 0 -> 3
        len_of_words = len(words[i])
        if(len_of_words <= 10):
            print(words[i])
        else:
            for j in range(len_of_words):  # 12
                abb1 = words[i][j] # 2D List/ Array
                abb2 = words[i][j-1] # 
                word_count = len_of_words-2
                final_abb = abb1+ str(word_count)+abb2
                print(final_abb)
                break

count = int(input())
word = []
for i in range(count): 
    w = input()
    word.append(w)
wayTooLongWords(word)



# words[1] = 'Helllo'

# a= word[1][0]
# a2 = word[1][-2]
# print(a[-1])

# aList =[]
# count = int(input())
# for i in range(count):
#     a = input()
#     aList.append(a)

# a = 1.5


# aList2 = [1254,523,'aText']
# a = list(aList2[0])
# aa = list(aList2[1])

# a2 = a[3]
# a3 = aa[1]

# result = int(a2)+int(a3)



a = [1,2,3][2,3,4]