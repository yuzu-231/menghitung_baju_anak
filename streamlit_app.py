import streamlit as st

# Judul aplikasi
st.title("Katalog Baju Anak")

# Data baju anak
baju_anak = [
    {"Nama": "Baju Anak Motif Dinosaurus", "Harga": "Rp 100.000", "Gambar": "https://via.placeholder.com/150?text=Dinosaurus"},
    {"Nama": "Baju Anak Motif Bunga", "Harga": "Rp 95.000", "Gambar": "https://via.placeholder.com/150?text=Bunga"},
    {"Nama": "Baju Anak Motif Mobil", "Harga": "Rp 105.000", "Gambar": "https://via.placeholder.com/150?text=Mobil"},
    {"Nama": "Baju Anak Motif Hewan", "Harga": "Rp 110.000", "Gambar": "https://via.placeholder.com/150?text=Hewan"},
    {"Nama": "Baju Anak Motif Buah", "Harga": "Rp 98.000", "Gambar": "https://via.placeholder.com/150?text=Buah"},
    {"Nama": "Baju Anak Motif Kartun", "Harga": "Rp 120.000", "Gambar": "https://via.placeholder.com/150?text=Kartun"},
    {"Nama": "Baju Anak Motif Polkadot", "Harga": "Rp 90.000", "Gambar": "https://via.placeholder.com/150?text=Polkadot"},
    {"Nama": "Baju Anak Motif Pelangi", "Harga": "Rp 115.000", "Gambar": "https://via.placeholder.com/150?text=Pelangi"},
    {"Nama": "Baju Anak Motif Bintang", "Harga": "Rp 100.000", "Gambar": "https://via.placeholder.com/150?text=Bintang"},
    {"Nama": "Baju Anak Motif Geometri", "Harga": "Rp 92.000", "Gambar": "https://via.placeholder.com/150?text=Geometri"},
]

# Menampilkan katalog
for baju in baju_anak:
    st.image(baju["Gambar"], width=150)
    st.subheader(baju["Nama"])
    st.write(f"Harga: {baju['Harga']}")
    st.write("-")
