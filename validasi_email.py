import re

# Fungsi untuk validasi email
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Input email dari pengguna
email = input("Masukkan alamat email: ")

# Cek apakah email valid
if is_valid_email(email):
    print("Alamat email valid.")
else:
    print("Alamat email tidak valid.")