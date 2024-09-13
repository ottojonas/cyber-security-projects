import hashlib
from urllib.request import urlopen
from icecream import ic


# function to read word list stored in url and store as word_list_file
def read_word_list(url):
    try:
        word_list_file = urlopen(url).read()
    except Exception as error:
        ic(f"error while fetching wordlist, error: {error}")
        exit()
    return word_list_file


# hashes password inputted and in word_list_file to match hashes  
def hash(word_list_password):
    result = hashlib.sha1(word_list_password.encode())
    return result.hexdigest()


# interates through password list to find if inputted password matches an item in word_list_file
def bruteforce(guess_password_list, actual_password_hash):
    for guess_password in guess_password_list:
        if hash(guess_password) == actual_password_hash:
            ic(f"your password is: {guess_password} - it is a leaked or common password - please change it")
            exit()


# word_list_file
url = "https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt"

# user input password 
actual_password = input('input password here: ')

# hash password
actual_password_hash = hash(actual_password)

# read word list and store in guess_password_list to be read by bruteforce method
word_list = read_word_list(url).decode("UTF-8")
guess_password_list = word_list.split("\n")

bruteforce(guess_password_list, actual_password_hash)

print("password could not be found in wordlist")
