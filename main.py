def is_pangram(input_string):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return set(input_string.lower()) >= alphabet