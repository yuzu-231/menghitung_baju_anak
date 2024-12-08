import streamlit as st
from PIL import Image

# Inisialisasi session state untuk menyimpan data
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []
if "page" not in st.session_state:
    st.session_state.page = "Katalog"  # Halaman default
if "total_harga" not in st.session_state:
    st.session_state.total_harga = 0

# Fungsi untuk menambahkan produk ke keranjang
def tambah_ke_keranjang(nama, harga, jumlah):
    if jumlah > 0:
        st.session_state.keranjang.append({"Nama": nama, "Harga": harga, "Jumlah": jumlah})
        st.success(f"{nama} berhasil ditambahkan ke keranjang!")

# Fungsi untuk mengganti halaman
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
]

# Halaman Katalog
if st.session_state.page == "Katalog":
    st.title("Katalog Toko Baju Andalan")

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

    # Tombol menuju halaman keranjang
    if st.button("Lihat Keranjang"):
        ganti_halaman("Keranjang")

# Halaman Keranjang
elif st.session_state.page == "Keranjang":
    st.title("Keranjang Belanja Anda")

    if st.session_state.keranjang:
        total_harga = 0
        for idx, item in enumerate(st.session_state.keranjang):
            st.write(f"{idx+1}. *{item['Nama']}* - {item['Jumlah']} x Rp {item['Harga']:,} = Rp {item['Jumlah'] * item['Harga']:,}")
            total_harga += item["Jumlah"] * item["Harga"]

        st.session_state.total_harga = total_harga
        st.markdown("### Total Harga")
        st.write(f"*Rp {total_harga:,}*")

        # Tombol untuk melanjutkan ke konfirmasi
        if st.button("Lanjutkan ke Pembayaran"):
            ganti_halaman("Pembayaran")
          if st.button("Kembali Ke Pesanan")
            ganti_halaman("Katalog")
    else:
        st.info("Keranjang Anda kosong.")
        if st.button("Kembali ke Katalog"):
            ganti_halaman("Katalog")

# Halaman Pembayaran
elif st.session_state.page == "Pembayaran":
    st.title("Konfirmasi Pembayaran")

    st.markdown("### Rincian Pesanan")
    for idx, item in enumerate(st.session_state.keranjang):
        st.write(f"{idx+1}. *{item['Nama']}* - {item['Jumlah']} x Rp {item['Harga']:,} = Rp {item['Jumlah'] * item['Harga']:,}")

    st.markdown("### Total Harga")
    st.write(f"*Rp {st.session_state.total_harga:,}*")

    # Tombol konfirmasi
    if st.button("Konfirmasi Pembayaran"):
        st.success("Pesanan Anda berhasil diproses! Terima kasih.")
        st.session_state.keranjang = []  # Reset keranjang setelah checkout
        st.session_state.total_harga = 0
        ganti_halaman("Katalog")
    elif st.button("Kembali ke Pesanan"):
        ganti_halaman("Katalog")
