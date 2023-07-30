
a=input("Enter the String :").lower()
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_list_reverse = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
lst=list(a)
# print(lst)
# for i in range (len(a)):
#     if a[i] in alphabet_list:
encrypt=[]
for i in range (len(lst)):
    # print(lst[i])
    if lst[i] in alphabet_list:
        # inx=alphabet_list[i].index(i)
        letter = i
        index_position = alphabet_list.index(lst[i])
        # print(alphabet_list_reverse[index_position])

        encrypt.append(alphabet_list_reverse[index_position])
    else:
        encrypt.append(" ")

l="".join(encrypt)
print(*encrypt)
print(l)



