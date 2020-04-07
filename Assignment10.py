# Temur Khabibullaev 4/2/2020
import re


def remover(sentence):
    sentence = str(sentence)
    sentence = re.sub(r'[^\w\s]', '', sentence)
    sentence = sentence.strip()
    sentence = sentence.lower()
    return sentence


def palindrome_check(string):
    string = remover(string)
    if len(string) <= 1:
        return 'yes'
    if string[0] != string[-1]:
        return 'no'
    else:
        return palindrome_check(string[1: -1])


while True:
    string = input('Enter the string, and I\'ll check if it is a palindrome:\n>>>')
    print(palindrome_check(string))
