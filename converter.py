ALPHA_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
               'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
               'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
               'Y': '-.--', 'Z': '--..'}

NUM_MORSE = {'0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
             '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

SYMBOL_MORSE = {'&': '.-...', "'": '.----.', "@": '.--.-.', ')': '-.--.-', '(': '-.--.', ':': '---...',
                ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '×': '-..-',
                '%': '----- -..-. -----', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'}


class TextToMorse:
    def __init__(self):
        self.alpha_morse = ALPHA_MORSE
        self.num_morse = NUM_MORSE
        self.symbol_morse = SYMBOL_MORSE

    def converter(self, text_input):
        morse_code_list = [self.alpha_morse, self.num_morse, self.symbol_morse]
        code_morse_converted = []
        for string in text_input.upper():
            for str_list in morse_code_list:
                if string in str_list.keys():
                    morse = str_list[string]
                    code_morse_converted.append(morse)

        output = ' '.join(code_morse_converted)
        return output
