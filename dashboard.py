from config import(
    even_odd,
    check_number,
    find_largest,
    find_largest_three,
    sum_natural,
    multiplication_table,
    factorial,
    count_digits,
    reverse_number,
    check_prime,
    count_characters,
    count_vowels,
    count_consonants,
    count_vowels_consonants,
    reverse_string,
    check_palindrome,
    count_words,
    character_frequency,
    remove_spaces,
    convert_uppercase,
    count_case,
    first_character,
    last_character,
    display_characters,
    display_position,
    remove_vowels,
    find_longest_word,
    count_each_vowel,
    star_pattern,
    number_pattern
)


def dashboard():

    while True:

        print()
        print("=" * 55)
        print("             PYTHON QUESTION PRACTICE")
        print("=" * 55)

        print("1.  Even or Odd")
        print("2.  Positive, Negative or Zero")
        print("3.  Find Largest of Two Numbers")
        print("4.  Find Largest of Three Numbers")
        print("5.  Sum of Natural Numbers")
        print("6.  Multiplication Table")
        print("7.  Factorial")
        print("8.  Count Digits")
        print("9.  Reverse a Number")
        print("10. Prime Number")
        print("11. Count Characters")
        print("12. Count Vowels")
        print("13. Count Consonants")
        print("14. Count Vowels and Consonants")
        print("15. Reverse a String")
        print("16. Check Palindrome String")
        print("17. Count Words")
        print("18. Character Frequency")
        print("19. Remove Spaces")
        print("20. Convert Lowercase to Uppercase")
        print("21. Count Uppercase, Lowercase, Digits and Spaces")
        print("22. Find First Character")
        print("23. Find Last Character")
        print("24. Print Each Character")
        print("25. Print Characters with Position")
        print("26. Remove Vowels")
        print("27. Find Longest Word")
        print("28. Count Occurrence of Each Vowel")
        print("29. Star Pattern")
        print("30. Number Pattern")
        print("0.  Exit")

        print("=" * 55)

        choice = int(input("Enter your choice: "))

        match choice:

            case 0:

                print()
                print("Thank you for using Python Question Practice.")
                break

            case 1:

                n = int(input("Enter a number: "))
                even_odd(n)

            case 2:

                n1 = int(input("Enter a number: "))
                check_number(n1)

            case 3:

                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))

                result = find_largest(a, b)

                print("Largest =", result)

            case 4:

                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                c = int(input("Enter third number: "))

                result = find_largest_three(a, b, c)

                print("Largest =", result)

            case 5:

                n = int(input("Enter n: "))

                result = sum_natural(n)

                print("Sum =", result)

            case 6:

                n = int(input("Enter a number: "))

                multiplication_table(n)

            case 7:

                n = int(input("Enter a number: "))

                result = factorial(n)

                print("Factorial =", result)

            case 8:

                n = int(input("Enter a number: "))

                result = count_digits(n)

                print("Number of digits =", result)

            case 9:

                n = int(input("Enter a number: "))

                result = reverse_number(n)

                print("Reversed number =", result)

            case 10:

                n = int(input("Enter a number: "))

                if check_prime(n):

                    print("Prime number")

                else:

                    print("Not a prime number")

            case 11:

                text = input("Enter a string: ")

                result = count_characters(text)

                print("Number of characters =", result)

            case 12:

                text = input("Enter a string: ")

                result = count_vowels(text)

                print("Number of vowels =", result)

            case 13:

                text = input("Enter a string: ")

                result = count_consonants(text)

                print("Number of consonants =", result)

            case 14:

                text = input("Enter a string: ")

                count_vowels_consonants(text)

            case 15:

                text = input("Enter a string: ")

                reverse_string(text)

            case 16:

                text = input("Enter a string: ")

                check_palindrome(text)

            case 17:

                text = input("Enter a sentence: ")

                result = count_words(text)

                print("Number of words =", result)

            case 18:

                text = input("Enter text: ")
                ch = input("Enter character: ")

                result = character_frequency(text, ch)

                print("Frequency =", result)

            case 19:

                text = input("Enter a string: ")

                result = remove_spaces(text)

                print("Without spaces =", result)

            case 20:

                text = input("Enter a string: ")

                convert_uppercase(text)

            case 21:

                text = input("Enter a string: ")

                count_case(text)

            case 22:

                text = input("Enter a string: ")

                first_character(text)

            case 23:

                text = input("Enter a string: ")

                last_character(text)

            case 24:

                text = input("Enter a string: ")

                display_characters(text)

            case 25:

                text = input("Enter a string: ")

                display_position(text)

            case 26:

                text = input("Enter a string: ")

                result = remove_vowels(text)

                print("Without vowels =", result)

            case 27:

                text = input("Enter a sentence: ")

                result = find_longest_word(text)

                print("Longest word =", result)

            case 28:

                text = input("Enter a string: ")

                count_each_vowel(text)

            case 29:

                n = int(input("Enter n: "))

                star_pattern(n)

            case 30:

                n = int(input("Enter n: "))

                number_pattern(n)

            case _:

                print("Invalid choice. Please enter a number from 0 to 30.")

        input("\nPress Enter to return to dashboard...")


'''
This function displays the Python question dashboard
and runs the selected question using match case.
'''