def palindrome_number():
    x = range(100, 1000)
    palindrome = 0
    for i in x:
        for j in x:
            prod = i * j
            if str(prod) == str(prod)[::-1]:
                if prod > palindrome:
                    palindrome = prod
    return palindrome

print(palindrome_number())
