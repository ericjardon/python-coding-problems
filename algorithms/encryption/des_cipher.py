"""DES [Data Encryption Standard]
    es un algoritmo de cifrado en bloques de de 8 bytes = 64 bits. 
    Recibce una llave de 8 bytes o 64 pero esta realmente se reduce a 56 bits.
    Al ser por bloques, el mensaje debe de ser un múltiplo
    del tamaño de la llave. De otra forma, se aplica un relleno que puede
    ser con ceros o con espacios.
    DES es un algoritmo muy conocido en emplear redes de Feistel."""

from base64 import b64decode, b64encode
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def encryptDES_CBC(key, plaintext, init_vector_8=None):
    # Recibe una llave, el texto claro, y vector de inicialización opcional
    if init_vector_8:
        cipher = DES.new(key, DES.MODE_CBC, iv=init_vector_8)
    else:
        cipher = DES.new(key, DES.MODE_CBC)

    # aplicar padding de acuerdo al tamaño del bloque
    data = pad(plaintext, DES.block_size)

    ciphertext_bytes = cipher.encrypt(data)

    return cipher.iv, ciphertext_bytes   # ambos en cadenas de bytes


def decryptDES_CBC(key, iv, ciphertext):
    # Recibe llave, vector de inicialización, y texto cifrado
    try:
        cipher = DES.new(key, DES.MODE_CBC, iv)
        data = cipher.decrypt(ciphertext)

        # Quitar el padding al texto desencriptado
        plaintext = unpad(data, DES.block_size)

        return plaintext

    except Exception as e:
        print("Fallo al desencriptar", e)
        return None


if __name__ == "__main__":
    # Generación de llave aleatoria
    key = get_random_bytes(8)
    plaintext = input("Escribe tu mensaje a encriptar (128 char MAX):\n")
    if len(plaintext) > 128:
        plaintext = plaintext[:128]
    plaintext = plaintext.encode('ascii')   # convertir de ASCII a bytes
    init_vector = b'12345678'

    # Encriptar
    iv, ciphertext = encryptDES_CBC(key, plaintext, init_vector)

    # Para mostrar en ASCII, codificamos a base64 y luego decodificamos en UTF-8
    ciphertext_print = b64encode(ciphertext).decode('ascii')

    print("Init vector", iv.decode("ascii"))
    print("\nCiphertext =>", ciphertext_print, "\n")

    print("Enviando mensaje encriptado...")
    print("Recibiendo mensaje encriptado...\n")

    # Desencriptar
    plaintext = decryptDES_CBC(key, iv, ciphertext)

    print("\nPlaintext =>", plaintext.decode("ascii"), "\n")


# https://pycryptodome.readthedocs.io/
