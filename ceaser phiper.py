
def encrypt():
    alphabet = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z"
    ]
    message=input("Enter the message")
    shift=int(input("Enter the shift number"))
    message1=""
    for letter in message:
        if letter==" ":
            message1+=" "
        else:
            indexx=alphabet.index(letter)
            fin_index=indexx+shift
            fin_index=fin_index % 26
            message1+=alphabet[fin_index]
    print(f"Here is the encoded message {message1}")

    def decrypt():
        print("Decrypting...")
        message2 = " "
        for letter in message1:
            if letter == " ":
                message2 += " "
            else:
                indexx = alphabet.index(letter)
                fin_index = indexx - shift
                fin_index = fin_index % 26
                message2 += alphabet[fin_index]
        print(f"The decrypted data is {message2}")

    decision=input("Do you want to continue Y / N")
    if decision.upper()== "Y":
        decrypt()
encrypt()


