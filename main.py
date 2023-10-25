def count_vowels(input_string):
    vowels = "AEIOUaeiou"
    return sum(input_string.count(vowel) for vowel in vowels)