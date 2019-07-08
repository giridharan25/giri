user=input()
if(user=='A' or user=='a'):
    print('Vowel')
elif(user=='E' or user=='e'): 
    print('Vowel')
elif(user=='I' or user=='i'): 
    print('Vowel')
elif(user=='O' or user=='o'):
    print('Vowel')
elif(user=='U' or user=='u'):
    print('Vowel')
elif(user>='a' and user<='z') or (user>='A' and user<='Z'): 
    print('Consonant')
else: print('invalid')
