class Decoder:
    def decode(data):
        output = ""
        for letter in data:
            output += chr(ord(letter) - 3)
        return data,output
