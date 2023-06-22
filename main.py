
def palindrome(s):
    return s[::-1] == s
while True:
    s = input("Введите палиндром: ")
    print(f"{s} True" if palindrome(s) else "False")