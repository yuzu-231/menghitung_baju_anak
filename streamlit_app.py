import streamlit as st
from PIL import Image
import json
import os

# Path file untuk menyimpan stok
STOK_FILE = "stok.json"

# Fungsi untuk membaca stok dari file
def baca_stok():
    if os.path.exists(STOK_FILE):
        with open(STOK_FILE, "r") as f:
            return json.load(f)
    else:
        # Jika file tidak ada, gunakan stok awal dan simpan ke file
        stok_awal = {
            "Baju Anak Motif Dinosaurus": 10,
            "Baju Anak Motif Bunga": 15,
            "Baju Anak Motif Mobil": 8,
            "Baju Anak Motif Hewan": 5,
            "Baju Anak Motif Buah": 12,
            "Baju Anak Motif Kartun": 7,
            "Baju Anak Motif Polkadot": 20,
            "Baju Anak Motif Pelangi": 18,
            "Baju Anak Motif Bintang": 12,
            "Baju Anak Motif Luar Angkasa": 10,
        }
        simpan_stok(stok_awal)
        return stok_awal

# Fungsi untuk menyimpan stok ke file
def simpan_stok(stok):
    with open(STOK_FILE, "w") as f:
        json.dump(stok, f)

# Inisialisasi session state
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []
if "page" not in st.session_state:
    st.session_state.page = "Login"  # Halaman default
if "total_harga" not in st.session_state:
    st.session_state.total_harga = 0
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "stok" not in st.session_state:
    st.session_state.stok = baca_stok()  # Baca stok dari file

# Data produk baju anak
baju_anak = [
    {"Nama": "Baju Anak Motif Dinosaurus", "Harga": 100000, "Gambar": "images/Dino.jpg"},
    {"Nama": "Baju Anak Motif Bunga", "Harga": 95000, "Gambar": "images/Bunga.jpg"},
    {"Nama": "Baju Anak Motif Mobil", "Harga": 105000, "Gambar": "images/Mobil.jpg"},
    {"Nama": "Baju Anak Motif Hewan", "Harga": 110000, "Gambar": "images/Hewan.jpg"},
    {"Nama": "Baju Anak Motif Buah", "Harga": 98000, "Gambar": "images/Buah.jpg"},
    {"Nama": "Baju Anak Motif Kartun", "Harga": 120000, "Gambar": "images/Kartun.jpg"},
    {"Nama": "Baju Anak Motif Polkadot", "Harga": 90000, "Gambar": "images/Polkadot.jpg"},
    {"Nama": "Baju Anak Motif Pelangi", "Harga": 115000, "Gambar": "images/Pelangi.jpg"},
    {"Nama": "Baju Anak Motif Bintang", "Harga": 100000, "Gambar": "images/Bintang.jpg"},
    {"Nama": "Baju Anak Motif Luar Angkasa", "Harga": 92000, "Gambar": "images/LuarAngkasa.jpg"},
]

# Fungsi untuk menambahkan produk ke keranjang
def tambah_ke_keranjang(nama, harga, jumlah, stok):
    if jumlah > 0 and jumlah <= stok:
        st.session_state.keranjang.append({"Nama": nama, "Harga": harga, "Jumlah": jumlah, "Subtotal": jumlah * harga})
        st.session_state.stok[nama] -= jumlah  # Kurangi stok
        simpan_stok(st.session_state.stok)  # Simpan perubahan stok ke file
        st.success(f"{nama} berhasil ditambahkan ke keranjang!")
    elif jumlah > stok:
        st.error(f"Jumlah melebihi stok tersedia ({stok}).")
    else:
        st.error("Jumlah harus lebih dari 0.")

# Fungsi untuk mengganti halaman
def ganti_halaman(page):
    st.session_state.page = page

# Halaman Login
if st.session_state.page == "Login":
    st.title("Login Pengguna")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    
    if st.button("Login"):
        if username == "admin" and password == "1234":  # Contoh login sederhana
            st.session_state.logged_in = True
            ganti_halaman("Katalog")
        else:
            st.error("Username atau password salah.")

# Halaman Katalog
elif st.session_state.page == "Katalog" and st.session_state.logged_in:
    st.title("Katalog Toko Baju Anak")
    
    for baju in baju_anak:
        col1, col2, col3 = st.columns([1, 3, 2])
        stok = st.session_state.stok[baju["Nama"]]  # Dapatkan stok terkini
        
        with col1:
            try:
                img = Image.open(baju["Gambar"])
                st.image(img, use_column_width=True)
            except:
                st.error(f"Gambar untuk {baju['Nama']} tidak ditemukan.")
        with col2:
            st.subheader(baju["Nama"])
            st.write(f"*Harga:* Rp {baju['Harga']:,}")
            st.write(f"*Stok:* {stok}")
        with col3:
            if stok > 0:
                jumlah = st.number_input(f"Jumlah untuk {baju['Nama']}", min_value=0, max_value=stok, step=1, key=baju["Nama"])
                if st.button(f"Tambah {baju['Nama']}", key=f"btn-{baju['Nama']}"):
                    tambah_ke_keranjang(baju["Nama"], baju["Harga"], jumlah, stok)
            else:
                st.error("Stok habis!")

    if st.button("Lihat Keranjang"):
        ganti_halaman("Keranjang")

# Halaman Keranjang
elif st.session_state.page == "Keranjang":
    st.title("Keranjang Belanja Anda")
    if st.session_state.keranjang:
        for item in st.session_state.keranjang:
            st.write(f"{item['Nama']} - Jumlah: {item['Jumlah']} - Subtotal: Rp {item['Subtotal']:,}")
        st.write(f"*Total Harga: Rp {sum([item['Subtotal'] for item in st.session_state.keranjang]):,}*")
        if st.button("Lanjutkan ke Pembayaran"):
            ganti_halaman("Pembayaran")
    else:
        st.warning("Keranjang Anda kosong.")
        if st.button("Kembali ke Katalog"):
            ganti_halaman("Katalog")

# Halaman Pembayaran
elif st.session_state.page == "Pembayaran":
    st.title("Konfirmasi Pembayaran")
    st.success("Pembayaran berhasil! Terima kasih atas pembelian Anda.")
    if st.button("Kembali ke Katalog"):
        ganti_halaman("Katalog")
