import json

# Nama file untuk menyimpan data pengguna
file_name = "data_pengguna.json"

# Fungsi untuk membaca data dari file
def baca_data():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Jika file tidak ditemukan, kembalikan dictionary kosong

# Fungsi untuk menyimpan data ke file
def simpan_data(data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

# Fungsi untuk pendaftaran
def daftar():
    print("=== Formulir Pendaftaran ===")
    nama = input("Masukkan Nama: ")
    email = input("Masukkan Email: ")
    kata_sandi = input("Masukkan Kata Sandi: ")

    # Membaca data pengguna yang ada
    data_pengguna = baca_data()

    # Periksa apakah email sudah terdaftar
    if email in data_pengguna:
        print("Email sudah terdaftar! Silakan gunakan email lain.")
        return

    # Tambahkan pengguna baru ke data
    data_pengguna[email] = {
        "nama": nama,
        "kata_sandi": kata_sandi
    }

    # Simpan data ke file
    simpan_data(data_pengguna)
    print("Pendaftaran berhasil!")

# Program utama
if _name_ == "_main_":
    daftar()
