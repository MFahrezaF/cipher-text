def vigenere_encrypt(plain_text, key):
    encrypted_text = ''
    key = key.upper()
    key_repeated = (key * (len(plain_text) // len(key) + 1))[:len(plain_text)]

    for p, k in zip(plain_text, key_repeated):
        if p.isalpha():
            # Mengonversi huruf ke angka (A=0, B=1, ..., Z=25)
            p_num = ord(p.upper()) - ord('A')
            k_num = ord(k.upper()) - ord('A')

            # Enkripsi dengan Vigenere Cipher
            encrypted_num = (p_num + k_num) % 26

            # Mengonversi angka kembali ke huruf
            encrypted_char = chr(encrypted_num + ord('A'))
            encrypted_text += encrypted_char
        else:
            # Menambahkan karakter non-alphabet tanpa enkripsi
            encrypted_text += p

    return encrypted_text


def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ''
    key = key.upper()
    key_repeated = (key * (len(encrypted_text) // len(key) + 1))[:len(encrypted_text)]

    for c, k in zip(encrypted_text, key_repeated):
        if c.isalpha():
            # Mengonversi huruf ke angka (A=0, B=1, ..., Z=25)
            c_num = ord(c.upper()) - ord('A')
            k_num = ord(k.upper()) - ord('A')

            # Dekripsi dengan Vigenere Cipher
            decrypted_num = (c_num - k_num) % 26

            # Mengonversi angka kembali ke huruf
            decrypted_char = chr(decrypted_num + ord('A'))
            decrypted_text += decrypted_char
        else:
            # Menambahkan karakter non-alphabet tanpa dekripsi
            decrypted_text += c

    return decrypted_text


def main():
    print("Program Vigenere Cipher")
    choice = int(input("Pilih 1 untuk Enkripsi, 2 untuk Dekripsi: "))

    if choice == 1:
        plain_text = input("Masukkan Plain Text: ").upper()
        key = input("Masukkan Kunci: ").upper()
        encrypted_result = vigenere_encrypt(plain_text, key)
        print("Hasil Enkripsi: ", encrypted_result)
    elif choice == 2:
        encrypted_text = input("Masukkan Plain Text Terenkripsi: ").upper()
        key = input("Masukkan Kunci: ").upper()
        decrypted_result = vigenere_decrypt(encrypted_text, key)
        print("Hasil Dekripsi: ", decrypted_result)
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
