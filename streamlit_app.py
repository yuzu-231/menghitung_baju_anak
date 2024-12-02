import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Judul aplikasi
st.title("Baju Anak")

# Data baju anak
baju_anak = [
    {"Nama": "Baju Anak Motif Dinosaurus", "Harga": 100000, "Gambar": "image/baju_dino.jpg"},
    {"Nama": "Baju Anak Motif Bunga", "Harga": 95000, "Gambar": "https://via.placeholder.com/300x300?text=Bunga"},
    {"Nama": "Baju Anak Motif Mobil", "Harga": 105000, "Gambar": "https://via.placeholder.com/300x300?text=Mobil"},
    {"Nama": "Baju Anak Motif Hewan", "Harga": 110000, "Gambar": "https://via.placeholder.com/300x300?text=Hewan"},
    {"Nama": "Baju Anak Motif Buah", "Harga": 98000, "Gambar": "https://via.placeholder.com/300x300?text=Buah"},
    {"Nama": "Baju Anak Motif Kartun", "Harga": 120000, "Gambar": "https://via.placeholder.com/300x300?text=Kartun"},
    {"Nama": "Baju Anak Motif Polkadot", "Harga": 90000, "Gambar": "https://via.placeholder.com/300x300?text=Polkadot"},
    {"Nama": "Baju Anak Motif Pelangi", "Harga": 115000, "Gambar": "https://via.placeholder.com/300x300?text=Pelangi"},
    {"Nama": "Baju Anak Motif Bintang", "Harga": 100000, "Gambar": "https://via.placeholder.com/300x300?text=Bintang"},
    {"Nama": "Baju Anak Motif Gunung", "Harga": 85000, "Gambar": "https://via.placeholder.com/300x300?text=Gunung"},
]

# Inisialisasi total harga
total_harga = 0

# Menampilkan katalog dan pilihan jumlah
for baju in baju_anak:
    col1, col2 = st.columns([1, 3])
    
    with col1:
        image = Image.open(baju["Gambar]")
        st.image(img, use_column_width=True)
        
    with col2:
        st.subheader(baju["Nama"])
        st.write(f"**Harga:** Rp {baju['Harga']:,}")
        jumlah = st.number_input(f"Jumlah untuk {baju['Nama']}", min_value=0, max_value=10, step=1, key=baju["Nama"])
        total_harga += jumlah * baju["Harga"]

# Menampilkan total harga
st.markdown("## Total Harga")
st.write(f"*Rp {total_harga:,}*")

# Tombol beli
if st.button("Beli Sekarang"):
   st.success("Terima kasih atas pembelian Anda!")
