import streamlit as st
from PIL import Image
import os

# Judul aplikasi
st.title("Katalog Toko Baju Anak Andalan")

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

# Inisialisasi keranjang belanja
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []

# Fungsi untuk menambahkan produk ke keranjang
def tambah_ke_keranjang(nama, harga, jumlah):
    if jumlah > 0:
        st.session_state.keranjang.append({"Nama": nama, "Harga": harga, "Jumlah": jumlah})
        st.success(f"{nama} berhasil ditambahkan ke keranjang!")

# Menampilkan katalog produk
st.markdown("## Katalog Produk")
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
        if st.button(f"Tambah ke Keranjang {baju['Nama']}", key=f"btn-{baju['Nama']}"):
            tambah_ke_keranjang(baju["Nama"], baju["Harga"], jumlah)

# Menampilkan isi keranjang
st.markdown("## Keranjang Belanja")
if st.session_state.keranjang:
    total_harga = 0
    for idx, item in enumerate(st.session_state.keranjang):
        st.write(f"{idx+1}. *{item['Nama']}* - {item['Jumlah']} x Rp {item['Harga']:,} = Rp {item['Jumlah'] * item['Harga']:,}")
        total_harga += item['Jumlah'] * item['Harga']

    st.markdown("### Total Harga")
    st.write(f"*Rp {total_harga:,}*")

    # Tombol checkout
    if st.button("Checkout"):
        st.success("Pesanan Anda berhasil diproses! Terima kasih.")
        st.session_state.keranjang = []  # Reset keranjang setelah checkout
else:
    st.info("Keranjang belanja Anda kosong.")

# Informasi tambahan
st.sidebar.title("Informasi Toko")
st.sidebar.markdown("""
- *Alamat:* Jl. Mawar No. 123
- *Telepon:* 0812-3456-7890
- *Jam Operasional:* 08.00 - 20.00
""")
