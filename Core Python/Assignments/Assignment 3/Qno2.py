#Write a program to input any alphabet and check whether it is vowel or consonant.

alph = (input("Enter an alphabet:"))

if alph in ('a' , 'e' , 'i' , 'o' , 'u'):
    print(f"{alph} is a vowel")
else:
    print(f"{alph} is a consonant")