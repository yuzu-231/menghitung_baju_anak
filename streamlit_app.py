import streamlit as st
from PIL import Image
import os

# Inisialisasi session state
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []
if "page" not in st.session_state:
    st.session_state.page = "Katalog"  # Halaman default

# Fungsi untuk menambahkan produk ke keranjang
def tambah_ke_keranjang(nama, harga, jumlah):
    if jumlah > 0:
        st.session_state.keranjang.append({"Nama": nama, "Harga": harga, "Jumlah": jumlah})
        st.success(f"{nama} berhasil ditambahkan ke keranjang!")

# Fungsi untuk menavigasi antar halaman
def ganti_halaman(page):
    st.session_state.page = page

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
    {"Nama": "Baju Anak Motif Luar Angkasa", "Harga": 92000, "Gambar": "images/Luar angkasa.jpg"},
]

# Halaman Katalog
if st.session_state.page == "Katalog":
    st.title("Katalog Toko Baju Anak Andalan")

    st.markdown("## Pilih Produk")
    for baju in baju_anak:
        col1, col2, col3 = st.columns([1, 3, 2])
        with col1:
            try:
                img = Image.open(baju["Gambar"])
                st.image(img, use_column_width=True)
            except:
                st.error(f"Gambar untuk {baju['Nama']} tidak ditemukan.")
        with col2:
            st.subheader(baju["Nama"])
            st.write(f"*Harga:* Rp {baju['Harga']:,}")
        with col3:
            jumlah = st.number_input(f"Jumlah untuk {baju['Nama']}", min_value=0, max_value=10, step=1, key=baju["Nama"])
            if st.button(f"Tambah {baju['Nama']}", key=f"btn-{baju['Nama']}"):
                tambah_ke_keranjang(baju["Nama"], baju["Harga"], jumlah)

    # Tombol menuju halaman checkout
    if st.button("Lihat Keranjang"):
        ganti_halaman("Checkout")

# Halaman Checkout
elif st.session_state.page == "Checkout":
    st.title("Checkout Pesanan Anda")

    if st.session_state.keranjang:
        total_harga = 0
        for idx, item in enumerate(st.session_state.keranjang):
            st.write(f"{idx+1}. *{item['Nama']}* - {item['Jumlah']} x Rp {item['Harga']:,} = Rp {item['Jumlah'] * item['Harga']:,}")
            total_harga += item["Jumlah"] * item["Harga"]

        st.markdown("### Total Harga")
        st.write(f"*Rp {total_harga:,}*")

        # Tombol konfirmasi
        if st.button("Konfirmasi Pesanan"): import streamlit as st
from PIL import Image
import os

# Inisialisasi session state
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []
if "page" not in st.session_state:
    st.session_state.page = "Katalog"  # Halaman default

# Fungsi untuk menambahkan produk ke keranjang
def tambah_ke_keranjang(nama, harga, jumlah):
    if jumlah > 0:
        st.session_state.keranjang.append({"Nama": nama, "Harga": harga, "Jumlah": jumlah})
        st.success(f"{nama} berhasil ditambahkan ke keranjang!")

# Fungsi untuk menavigasi antar halaman
def ganti_halaman(page):
    st.session_state.page = page

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
    {"Nama": "Baju Anak Motif Luar Angkasa", "Harga": 92000, "Gambar": "images/Luar angkasa.jpg"},
]

# Halaman Katalog
if st.session_state.page == "Katalog":
    st.title("Katalog Toko Baju Anak Andalan")

    st.markdown("## Pilih Produk")
    for baju in baju_anak:
        col1, col2, col3 = st.columns([1, 3, 2])
        with col1:
            try:
                img = Image.open(baju["Gambar"])
                st.image(img, use_column_width=True)
            except:
                st.error(f"Gambar untuk {baju['Nama']} tidak ditemukan.")
        with col2:
            st.subheader(baju["Nama"])
            st.write(f"*Harga:* Rp {baju['Harga']:,}")
        with col3:
            jumlah = st.number_input(f"Jumlah untuk {baju['Nama']}", min_value=0, max_value=10, step=1, key=baju["Nama"])
            if st.button(f"Tambah {baju['Nama']}", key=f"btn-{baju['Nama']}"):
                tambah_ke_keranjang(baju["Nama"], baju["Harga"], jumlah)

    # Tombol menuju halaman checkout
    if st.button("Lihat Keranjang"):
        ganti_halaman("Checkout")

# Halaman Checkout
elif st.session_state.page == "Checkout":
    st.title("Checkout Pesanan Anda")

    if st.session_state.keranjang:
        total_harga = 0
        for idx, item in enumerate(st.session_state.keranjang):
            st.write(f"{idx+1}. *{item['Nama']}* - {item['Jumlah']} x Rp {item['Harga']:,} = Rp {item['Jumlah'] * item['Harga']:,}")
            total_harga += item["Jumlah"] * item["Harga"]

        st.markdown("### Total Harga")
        st.write(f"*Rp {total_harga:,}*")

        # Tombol konfirmasi
        if st.button("Konfirmasi Pesanan"):import streamlit as st
from PIL import Image
import os

# Inisialisasi session state
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []
if "page" not in st.session_state:
    st.session_state.page = "Katalog"  # Halaman default

# Fungsi untuk menambahkan produk ke keranjang
def tambah_ke_keranjang(nama, harga, jumlah):
    if jumlah > 0:
        st.session_state.keranjang.append({"Nama": nama, "Harga": harga, "Jumlah": jumlah})
        st.success(f"{nama} berhasil ditambahkan ke keranjang!")

# Fungsi untuk menavigasi antar halaman
def ganti_halaman(page):
    st.session_state.page = page

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
    {"Nama": "Baju Anak Motif Luar Angkasa", "Harga": 92000, "Gambar": "images/Luar angkasa.jpg"},
]

# Halaman Katalog
if st.session_state.page == "Katalog":
    st.title("Katalog Toko Baju Anak Andalan")

    st.markdown("## Pilih Produk")
    for baju in baju_anak:
        col1, col2, col3 = st.columns([1, 3, 2])
        with col1:
            try:
                img = Image.open(baju["Gambar"])
                st.image(img, use_column_width=True)
            except:
                st.error(f"Gambar untuk {baju['Nama']} tidak ditemukan.")
        with col2:
            st.subheader(baju["Nama"])
            st.write(f"*Harga:* Rp {baju['Harga']:,}")
        with col3:
            jumlah = st.number_input(f"Jumlah untuk {baju['Nama']}", min_value=0, max_value=10, step=1, key=baju["Nama"])
            if st.button(f"Tambah {baju['Nama']}", key=f"btn-{baju['Nama']}"):
                tambah_ke_keranjang(baju["Nama"], baju["Harga"], jumlah)

    # Tombol menuju halaman checkout
    if st.button("Lihat Keranjang"):
        ganti_halaman("Checkout")

# Halaman Checkout
elif st.session_state.page == "Checkout":
    st.title("Checkout Pesanan Anda")

    if st.session_state.keranjang:
        total_harga = 0
        for idx, item in enumerate(st.session_state.keranjang):
            st.write(f"{idx+1}. *{item['Nama']}* - {item['Jumlah']} x Rp {item['Harga']:,} = Rp {item['Jumlah'] * item['Harga']:,}")
            total_harga += item["Jumlah"] * item["Harga"]

        st.markdown("### Total Harga")
        st.write(f"*Rp {total_harga:,}*")

        # Tombol konfirmasi
        if st.button("Konfirmasi Pesanan"): st.button("Kembali ke katalog")
            st.success("Pesanan Anda telah berhasil diproses. Terima kasih!")
            st.session_state.keranjang = []  # Reset keranjang setelah checkout
            ganti_halaman("Katalog")  # Kembali ke halaman katalog
   
    
    else:
        st.info("Keranjang belanja Anda kosong.")
        if st.button("Kembali ke Katalog"):
            ganti_halaman("Katalog")
