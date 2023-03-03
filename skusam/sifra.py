

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
encrypted_message=""
def encrypt(message,shift):
    encypted_message=""
    for x in message:
        if x != " ":
            index= alphabet.index(x)
            new_index = index + shift
            encypted_message+= alphabet[new_index]
        else:
            encrypted_message+=x   
    print(f"Your encypted message is {encypted_message}")        

def decryption(message,shift):
    normal_text=""
    for x in message:
        if x != " ":
            
            index = alphabet.index(x)
            new_index= index - shift
            normal_text+=alphabet[new_index]
        else:
            normal_text+=x
         

   
    print(f"Your deencypted message is {normal_text}")   

def cipher(start_text,shift,choice):
    end_text=""
    if choice == "encode":
        shift = shift
    elif choice == "decode":
        shift= -shift
    for x in start_text:
        if x != " ":
            index = alphabet.index(x)
            new_index= index + shift
            end_text+=alphabet[new_index]
        else:
            end_text+=x
    print(f"{choice} of message is {end_text}")


run="yes"
while run == "yes":
    choice = input("Type 'encode' to encrypt, type 'decode to decrypt:\n")
    text= input("Type your message ").lower()
    shift = int(input("Type the shift number: "))  
    cipher(text,shift,choice)
    run=input("Do you wanna contiune? Yes or No ?")                