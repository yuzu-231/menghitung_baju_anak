import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Judul aplikasi
st.title("Katalog Toko Baju Andalan")

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

# Inisialisasi keranjang belanja
keranjang = []

# Menampilkan katalog dan pilihan jumlah
st.markdown("## Katalog Produk")
for baju in baju_anak:
    col1, col2 = st.columns([1, 3])
    
    with col1:
        try:
            # Coba ambil gambar dari file lokal
            img = Image.open(baju["Gambar"])
            st.image(img, use_column_width=True)
        except Exception as e:
            st.error(f"Gagal memuat gambar untuk {baju['Nama']}")
        
    with col2:
        st.subheader(baju["Nama"])
        st.write(f"Harga: Rp {baju['Harga']:,}")
        jumlah = st.number_input(f"Jumlah untuk {baju['Nama']}", min_value=0, max_value=10, step=1, key=baju["Nama"])
        
        # Tambahkan ke keranjang jika jumlah > 0
        if jumlah > 0:
            keranjang.append({"Nama": baju["Nama"], "Harga": baju["Harga"], "Jumlah": jumlah})

# Menampilkan keranjang belanja
if keranjang:
    st.markdown("## Keranjang Belanja")
    total_harga = 0
    
    for item in keranjang:
        st.write(f"{item['Nama']} - {item['Jumlah']} x Rp {item['Harga']:,} = Rp {item['Jumlah'] * item['Harga']:,}")
        total_harga += item["Jumlah"] * item["Harga"]
    
    st.markdown("### Total Harga")
    st.write(f"*Rp {total_harga:,}*")
    
    # Tombol checkout
    if st.button("Checkout"):
        st.success("Terima kasih atas pembelian Anda!")
else:
    st.info("Keranjang belanja Anda kosong.")
