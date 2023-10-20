# Encode the password
def encoder(message):
    result = ''
    for digit in message:
        new_digit = str((int(digit) + 3) % 10)
        result += new_digit
    return result


# Decode the password
def decoder(message):
    result = ''
    for digit in message:
        digit = int(digit) - 3
        if digit < 0:
            digit += 10
        new_digit = str(digit)
        result += new_digit
    return result


# Main loop which shows Menu
def main():
    encode_value = 0
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Enter your option: ")
        if choice == "1":
            value = input("Please enter your password to encode: ")
            encode_value = encoder(value)
            print("Your password has been encoded and stored!")
        elif choice == "2":
            decode_value = decoder(encode_value)
            print(f"The encoded password is {encode_value}, and the original password is {decode_value}.")
        elif choice == "3":
            break
        print()


if __name__ == "__main__":
    main()
