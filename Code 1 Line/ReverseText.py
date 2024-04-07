# palindrome

text = input("Enter : ")

"""
def reverse_text(text):
    return "".join(reverse_text(text))
"""

def reverse_text(text):
    return text[:: -1]

print(reverse_text(text))

# madam , mom , radar , rotator , a santa at nasa , acrobats stab orca ,
# was it a car or a cat i saw , go hang a salami im a lasagna hog