
def main():

    while True:
        user_input = input("Please input a positive integer, a semicolon, and a word of your choosing. No spaces. ")

        if ';' not in user_input or '-' in user_input:
            break

        parts = user_input.split(";")
        num = int(parts[0])
        word = parts[1].lower()

        # ord() gives the ascii value of the character
        word_nums = [ord(x) - ord('a') for x in word]

        max_range = num + len(word)
        fibs = [fib(x) for x in range(num - 1, max_range - 1)]

        encrypted_nums = vector_add(word_nums, fibs)
        encrypted_letters = [chr(x + ord('a')) for x in encrypted_nums]

        print(''.join(encrypted_letters).upper())



"""
The fibonacci sequence
"""
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


"""
Vector addition and mod 26
"""
def vector_add(list_a, list_b):
    return [(a + b) % 26 for a, b in zip(list_a, list_b)]


main()