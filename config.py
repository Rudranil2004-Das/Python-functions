def even_odd(n: int):

    if n % 2 == 0:

        print("Even")

    else:

        print("Odd")


'''
This function checks whether a number is even or odd.

'''


def check_number(n1: int):

    if n1 > 0:

        print("Positive")

    elif n1 < 0:

        print("Negative")

    else:

        print("Zero")


'''
This function checks whether the number is Positive,
Negative or Zero.

'''


def find_largest(a, b):

    if a > b:

        return a

    else:

        return b


'''
This function finds the largest of two numbers.

'''


def find_largest_three(a, b, c):

    if a >= b and a >= c:

        return a

    elif b >= a and b >= c:

        return b

    else:

        return c


'''
This function finds the largest of three numbers.
max() is not used.

'''


def sum_natural(n):

    total = 0

    for i in range(1, n + 1):

        total = total + i

    return total


'''
This function calculates the sum from 1 to n.

'''


def multiplication_table(n):

    for i in range(1, 11):

        print(n, "x", i, "=", n * i)


'''
This function prints the multiplication table from 1 to 10.

'''


def factorial(n):

    result = 1

    for i in range(1, n + 1):

        result = result * i

    return result


'''
This function calculates factorial using a loop.
Recursion is not used.

'''


def count_digits(n):

    if n == 0:

        return 1

    if n < 0:

        n = -n

    count = 0

    while n > 0:

        n = n // 10

        count = count + 1

    return count


'''
This function counts the number of digits using while loop.

'''


def reverse_number(n):

    reverse = 0

    while n > 0:

        digit = n % 10

        reverse = reverse * 10 + digit

        n = n // 10

    return reverse


'''
This function reverses a number using while, % and //.

'''


def check_prime(n):

    if n <= 1:

        return False

    for i in range(2, n):

        if n % i == 0:

            return False

    return True


'''
This function checks whether a number is prime.

'''


def count_characters(text):

    count = 0

    for ch in text:

        count = count + 1

    return count


'''
This function counts the number of characters using a loop.
len() is not used.

'''


def count_vowels(text):

    count = 0

    for ch in text:

        if ch.lower() in "aeiou":

            count = count + 1

    return count


'''
This function counts vowels using a loop and lower().

'''


def count_consonants(text):

    count = 0

    for ch in text:

        if ch.isalpha():

            if ch.lower() not in "aeiou":

                count = count + 1

    return count


'''
This function counts consonants using a loop and isalpha().

'''


def count_vowels_consonants(text):

    vowels = 0

    consonants = 0

    for ch in text:

        if ch.isalpha():

            if ch.lower() in "aeiou":

                vowels = vowels + 1

            else:

                consonants = consonants + 1

    print("Vowels :", vowels)

    print("Consonants :", consonants)


'''
This function separately counts vowels and consonants.

'''


def reverse_string(text):

    reverse = text[::-1]

    print("Reverse :", reverse)


'''
This function reverses a string using slicing.

'''


def check_palindrome(text):

    reverse = text[::-1]

    if text == reverse:

        print("Palindrome")

    else:

        print("Not Palindrome")


'''
This function checks whether a string is palindrome
using slicing.

'''


def count_words(text):

    count = 0

    inside_word = False

    for ch in text:

        if ch != " " and inside_word == False:

            count = count + 1

            inside_word = True

        elif ch == " ":

            inside_word = False

    return count


'''
This function counts words using a loop.
split() is not used.

'''


def character_frequency(text, ch):

    frequency = 0

    for character in text:

        if character == ch:

            frequency = frequency + 1

    return frequency


'''
This function counts the frequency of a character using a loop.
count() is not used.

'''


def remove_spaces(text):

    result = ""

    for ch in text:

        if ch != " ":

            result = result + ch

    return result


'''
This function removes spaces using a loop.

'''


def convert_uppercase(text):

    result = text.upper()

    print("Uppercase :", result)


'''
This function converts a string to uppercase using upper().

'''


def count_case(text):

    uppercase = 0

    lowercase = 0

    digits = 0

    spaces = 0

    for ch in text:

        if ch.isupper():

            uppercase = uppercase + 1

        elif ch.islower():

            lowercase = lowercase + 1

        elif ch.isdigit():

            digits = digits + 1

        elif ch == " ":

            spaces = spaces + 1

    print("Uppercase :", uppercase)

    print("Lowercase :", lowercase)

    print("Digits :", digits)

    print("Spaces :", spaces)


'''
This function counts uppercase, lowercase, digits and spaces
using string methods.

'''


def first_character(text):

    for ch in text:

        print("First character :", ch)

        break


'''
This function finds the first character using a loop.
text[0] is not used.

'''


def last_character(text):

    print("Using text[-1] :", text[-1])

    last = ""

    for ch in text:

        last = ch

    print("Using loop :", last)


'''
This function finds the last character using indexing
and a loop.

'''


def display_characters(text):

    for ch in text:

        print(ch)


'''
This function prints every character on a separate line.

'''


def display_position(text):

    for i in range(len(text)):

        print("Position", i, ":", text[i])


'''
This function displays every character with its position
using indexing and range().

'''


def remove_vowels(text):

    result = ""

    for ch in text:

        if ch.lower() not in "aeiou":

            result = result + ch

    return result


'''
This function removes vowels using a loop.
replace() is not used.

'''


def find_longest_word(text):

    longest_word = ""

    current_word = ""

    for ch in text:

        if ch != " ":

            current_word = current_word + ch

        else:

            if len(current_word) > len(longest_word):

                longest_word = current_word

            current_word = ""

    if len(current_word) > len(longest_word):

        longest_word = current_word

    return longest_word


'''
This function finds the longest word using a loop.
max(), dictionaries and advanced collections are not used.

'''


def count_each_vowel(text):

    a_count = 0

    e_count = 0

    i_count = 0

    o_count = 0

    u_count = 0

    for ch in text.lower():

        if ch == "a":

            a_count = a_count + 1

        elif ch == "e":

            e_count = e_count + 1

        elif ch == "i":

            i_count = i_count + 1

        elif ch == "o":

            o_count = o_count + 1

        elif ch == "u":

            u_count = u_count + 1

    print("a =", a_count)

    print("e =", e_count)

    print("i =", i_count)

    print("o =", o_count)

    print("u =", u_count)


'''
This function counts each vowel separately using a loop.

'''


def star_pattern(n):

    for i in range(1, n + 1):

        for j in range(i):

            print("*", end="")

        print()


'''
This function creates a star pattern using nested loops.

'''


def number_pattern(n):

    for i in range(1, n + 1):

        for j in range(1, i + 1):

            print(j, end="")

        print()


'''
This function creates a number pattern using nested loops.

'''