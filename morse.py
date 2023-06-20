def convertir_a_morse(palabra):
    morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
             'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
             'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
             'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
             '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

    codigo_morse = []
    for letra in palabra.upper():
        if letra in morse:
            codigo_morse.append(morse[letra])
        else:
            codigo_morse.append(' ')

    return ' '.join(codigo_morse)


# Ejemplo de uso
palabra = input("Ingresa una palabra: ")
codigo = convertir_a_morse(palabra)
print("Código Morse:", codigo)
