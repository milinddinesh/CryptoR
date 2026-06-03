# ---- Begin Substituion ciphers ---- 

# ---- Begin Replacement Ciphers --- 

def replace_character(plaintext, key, replacement_character):
    #plaintext : the original string
    #key : the character to look for
    #replacement_character : the character used to replace the key character
    #both the key and replacement_character should be a single character
    #returns encoded string

    if len(key) != 1 or len(replacement_character) != 1:
        raise ValueError("Both key and replacement_character should be a single character")
    
    encoded_string = ""
    for character in plaintext:
        if character == key:
            encoded_string += replacement_character
        else:
            encoded_string += character
    return encoded_string

# Ceaser cipher , rot13 cipher
def rotate_character(plaintext, key):
    #plaintext : the original string
    #key : the number of positions to rotate each character
    #returns encoded string
    #uses the whole ascii table

    encoded_string = ""
    for character in plaintext:
        if character == " ":
            encoded_string += " "
        else:
            encoded_string += chr((ord(character) + key) % 256)
    return encoded_string

if __name__ == "__main__":
    plaintext = "hello world"
    key = 13
    print(rotate_character(plaintext, key))


# def replacement_cipher_encrypt(plaintext, key , replacment_text):
    # plaintext : the original string 
    # key : the substring to look for 
    # replacement_text : the substring used to replace the key string 
    # both the key and replacement_text can be of length between 1 and len(plaintex)
    # returns encoded string 

    #Theoretically, we can use this function to replace any substring with any other substring

    # left = 0 = len(replacment_text)
    # right = 0
    # while (left < len(replacment_text) and right < len(replacment_text)):
        
#Mono character replacement

#How does the function perfom when a large string is given as input ?
