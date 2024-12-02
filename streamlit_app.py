import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Judul aplikasi
st.title("Katalog Baju Anak")

# Data baju anak
baju_anak = [
    {"Nama": "Baju Anak Motif Dinosaurus", "Harga": "Rp 100.000", "Gambar": "https://via.placeholder.com/300x300?text=Dinosaurus"},
    {"Nama": "Baju Anak Motif Bunga", "Harga": "Rp 95.000", "Gambar": "https://via.placeholder.com/300x300?text=Bunga"},
    {"Nama": "Baju Anak Motif Mobil", "Harga": "Rp 105.000", "Gambar": "https://via.placeholder.com/300x300?text=Mobil"},
    {"Nama": "Baju Anak Motif Hewan", "Harga": "Rp 110.000", "Gambar": "https://via.placeholder.com/300x300?text=Hewan"},
    {"Nama": "Baju Anak Motif Buah", "Harga": "Rp 98.000", "Gambar": "https://via.placeholder.com/300x300?text=Buah"},
    {"Nama": "Baju Anak Motif Kartun", "Harga": "Rp 120.000", "Gambar": "https://via.placeholder.com/300x300?text=Kartun"},
    {"Nama": "Baju Anak Motif Polkadot", "Harga": "Rp 90.000", "Gambar": "https://via.placeholder.com/300x300?text=Polkadot"},
    {"Nama": "Baju Anak Motif Pelangi", "Harga": "Rp 115.000", "Gambar": "https://via.placeholder.com/300x300?text=Pelangi"},
    {"Nama": "Baju Anak Motif Bintang", "Harga": "Rp 100.000", "Gambar": "https://via.placeholder.com/300x300?text=Bintang"},
    {"Nama": "Baju Anak Motif Geometri", "Harga": "Rp 92.000", "Gambar": "https://via.placeholder.com/300x300?text=Geometri"},
]

# Menampilkan katalog dengan grid
cols = st.columns(2)

for i, baju in enumerate(baju_anak):
    col = cols[i % 2]
    response = requests.get(baju["Gambar"])
    img = Image.open(BytesIO(response.content))
    
    with col:
        st.image(img, caption=baju["Nama"], use_column_width=True)
        st.write(f"*Harga:* {baju['Harga']}")
        st.button("Beli Sekarang", key=baju["Nama"])
        st.markdown("---")
