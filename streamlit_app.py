import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Judul aplikasi
st.title("Katalog Baju Anak dengan Perhitungan Total")

# Data baju anak (kombinasi URL dan gambar lokal)
baju_anak = [
    {"Nama": "Baju Anak Motif Dinosaurus", "Harga": 100000, "Gambar": "images/dino.jpg"},
    {"Nama": "Baju Anak Motif Bunga", "Harga": 95000, "Gambar": "images/bunga.jpg"},
    {"Nama": "Baju Anak Motif Mobil", "Harga": 105000, "Gambar": "images/mobil.jpg"},  
    {"Nama": "Baju Anak Motif Hewan", "Harga": 110000, "Gambar": "images/hewan.jpg"}, 
    {"Nama": "Baju Anak Motif Buah", "Harga": 98000, "Gambar": "images/buah.jpg"},
    {"Nama": "Baju Anak Motif Kartun", "Harga": 120000, "Gambar": "images/kartun.jpg"},
    {"Nama": "Baju Anak Motif Polkadot", "Harga": 90000, "Gambar": "images/polkadot.jpg"}, 
    {"Nama": "Baju Anak Motif Pelangi", "Harga": 115000, "Gambar": "images/pelangi.jpg"},
    {"Nama": "Baju Anak Motif Bintang", "Harga": 100000, "Gambar": "images/bintang.jpg"},
    {"Nama": "Baju Anak Motif Luar Angkasa", "Harga": 92000, "Gambar": "images/luar angkasa.jpg"},
]

# Inisialisasi total harga
total_harga = 0

# Menampilkan katalog dan pilihan jumlah
for baju in baju_anak:
    col1, col2 = st.columns([1, 3])
    
    with col1:
        try:
            # Coba ambil gambar dari URL
            if baju["Gambar"].startswith("http"):
                response = requests.get(baju["Gambar"])
                img = Image.open(BytesIO(response.content))
            else:
                # Jika gambar lokal
                img = Image.open(baju["Gambar"])
                
            st.image(img, use_column_width=True)
        except Exception as e:
            st.error(f"Gagal memuat gambar untuk {baju['Nama']}")
        
    with col2:
        st.subheader(baju["Nama"])
        st.write(f"*Harga:* Rp {baju['Harga']:,}")
        jumlah = st.number_input(f"Jumlah untuk {baju['Nama']}", min_value=0, max_value=10, step=1, key=baju["Nama"])
        total_harga += jumlah * baju["Harga"]

# Menampilkan total harga
st.markdown("## Total Harga")
st.write(f"*Rp {total_harga:,}*")

# Tombol beli
if st.button("Beli Sekarang"):
    st.success("Terima kasih atas pembelian Anda!")


import os

# Path folder gambar
folder_path = "images/"

# Periksa apakah folder ada
if os.path.exists(folder_path):
    st.write(f"Folder '{folder_path}' ditemukan.")
else:
    st.error(f"Folder '{folder_path}' tidak ditemukan. Pastikan path benar.")

# Periksa izin baca pada folder
if os.access(folder_path, os.R_OK):
    st.write(f"Streamlit memiliki izin membaca pada folder '{folder_path}'.")
else:
    st.error(f"Streamlit tidak memiliki izin membaca pada folder '{folder_path}'. Periksa izin file/folder.")





for baju in baju_anak:
    if not baju["Gambar"].startswith("http"):  # Hanya periksa file lokal
        file_path = baju["Gambar"]
        if os.path.exists(file_path):
            if os.access(file_path, os.R_OK):
                st.write(f"File '{file_path}' dapat diakses.")
            else:
                st.error(f"File '{file_path}' tidak memiliki izin baca.")
        else:
            st.error(f"File '{file_path}' tidak ditemukan.")

ls -ld images/
chmod +r images/
