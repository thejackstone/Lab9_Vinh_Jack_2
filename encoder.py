class Encoder:
    def encode(data):
        output = ""
        for letter in data:
            output += chr(ord(letter) + 3)
        return output