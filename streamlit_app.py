import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Judul aplikasi
st.title("Katalog Baju Anak dengan Perhitungan Total")

# Data baju anak (kombinasi URL dan gambar lokal)
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
