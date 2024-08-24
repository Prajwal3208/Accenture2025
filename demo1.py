def word(s):
    string =""
    splited_string = s.split('0')
    for i in splited_string :
        if i:
            letter_posi = len(i)
            letter = chr(ord('A')+(letter_posi-1))
            string += letter
    return string
s = str(input("Enter the string :"))
print(word(s))

# s = "10010110111111000"
# seq = s.split('0')
# print(seq)
# # seq = 12
# for i in (seq):#range(seq): #seq:#(len(seq)):
#     if i:
#         letter = len(i)
    
#         print(letter)