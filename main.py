import string
import random

# --- Defining Variables ---

password_list = []

LOWER_ALPHABET = list(string.ascii_lowercase)
DIGITS = list(string.digits)
UPPER_ALPHABET = list(string.ascii_uppercase)

SYMBOLS = list(string.punctuation)
SYMBOLS_EXCLUDE = ['"', "'", "(", ")", ",", ".", ":", ";", "[", "]", "|", "`", "{", "}"]
for x in SYMBOLS_EXCLUDE:
  SYMBOLS.remove(x)

CHAR_TYPES = [LOWER_ALPHABET, DIGITS] # Lower case letters and digits are used as default

# --- Program Intro ---

print("""    
#############################################################
#                  --- Password Generator ---               #
#############################################################
#                       Language: Python                    #
#############################################################
#                                                           #
#          This is my very first project with Python        #
#    Lowercase characteres and digits is used as default    #
#                                                           #
#############################################################
""")

# --- Password Length and Characteres Selection ---

# Length Question

while True:
  print("Password Length (Min: 8 / Max: 48):")
  pass_len = input()
  try:
    pass_len = int(pass_len)
    if pass_len >= 8 and pass_len <= 48:
        break
    else:
        print("\nYou should insert a number between 8 and 16.\n")
  except ValueError:
    # In case of the user insert a value that cannot be turned into a 'num' type
    
    print("\nYou should insert a NUMBER between 8 and 16.\n")

# Uppercase and Symbols Question Function

def question_checker(phrase, char_type):
    """Check if the user inserts a valid value on the upper case and symbols question.
        Then append the specific char type list if he answer is "Yes"
    """

    while True:
        print("")
        print(phrase)
        answer = input().strip().capitalize()
        if answer == "Yes" or answer == "No":
            break
        else:
            print("\nInvalid Value.\n")

    def char_assignment(char_check, char_type):
        if char_check == "Yes":
            return CHAR_TYPES.append(char_type)
        else:
            pass

    char_assignment(answer, char_type)


# Assigning Uppercase and/or Symbols characteres into the CHAR_TYPES list.

question_checker("Do you want uppercase letters? [Yes/No]", UPPER_ALPHABET)
question_checker("Do you want symbols? [Yes/No]", SYMBOLS)

# Make the Password

for x in range(len(CHAR_TYPES)):
    password_list.append(CHAR_TYPES[x][random.randrange(len(CHAR_TYPES[x]))]) # making at least one of all the char types appear in the password

for x in range(pass_len - len(CHAR_TYPES)):
    random_chartype = random.randrange(len(CHAR_TYPES))
    password_list.append(CHAR_TYPES[random_chartype][random.randrange(len(CHAR_TYPES[random_chartype]))]) # the spaces that remained will be filled with random characteres


random.shuffle(password_list)
password = "".join(password_list)

# Show Output

print("\n")
print(f"Password: {password} ")
print("\n")