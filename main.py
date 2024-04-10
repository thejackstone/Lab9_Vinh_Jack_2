from encoder import Encoder
from decoder import Decoder
def main():
    encoded_password = None
    while True:
        print("""
Menu
-------------
1. Encode
2. Decode
3. Quit
""")    
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = Encoder.encode(password)
            print("Your password has been encoded and stored!")
        elif choice == "2":
            encoded_password, decoded_password = Decoder.decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        elif choice == "3":
            break

if __name__ == "__main__":
    main() 