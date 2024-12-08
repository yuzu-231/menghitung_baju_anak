import streamlit as st
from PIL import Image

# Inisialisasi session state
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []
if "page" not in st.session_state:
    st.session_state.page = "Login"  # Halaman default
if "total_harga" not in st.session_state:
    st.session_state.total_harga = 0
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "diskon" not in st.session_state:
    st.session_state.diskon = 0

# Data produk baju anak dengan stok
baju_anak = [
    {"Nama": "Baju Anak Motif Dinosaurus", "Harga": 100000, "Gambar": "images/Dino.jpg", "Stok": 10},
    {"Nama": "Baju Anak Motif Bunga", "Harga": 95000, "Gambar": "images/Bunga.jpg", "Stok": 15},
    {"Nama": "Baju Anak Motif Mobil", "Harga": 105000, "Gambar": "images/Mobil.jpg", "Stok": 8},
    {"Nama": "Baju Anak Motif Hewan", "Harga": 110000, "Gambar": "images/Hewan.jpg", "Stok": 5},
    {"Nama": "Baju Anak Motif Buah", "Harga": 98000, "Gambar": "images/Buah.jpg", "Stok": 12},
    {"Nama": "Baju Anak Motif Kartun", "Harga": 120000, "Gambar": "images/Kartun.jpg", "Stok": 7},
]

# Fungsi untuk menambahkan produk ke keranjang
def tambah_ke_keranjang(nama, harga, jumlah, stok):
    if jumlah > 0 and jumlah <= stok:
        st.session_state.keranjang.append({"Nama": nama, "Harga": harga, "Jumlah": jumlah, "Subtotal": jumlah * harga})
        st.success(f"{nama} berhasil ditambahkan ke keranjang!")
    elif jumlah > stok:
        st.error(f"Jumlah melebihi stok tersedia ({stok}).")

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
        with col1:
            try:
                img = Image.open(baju["Gambar"])
                st.image(img, use_column_width=True)
            except:
                st.error(f"Gambar untuk {baju['Nama']} tidak ditemukan.")
        with col2:
            st.subheader(baju["Nama"])
            st.write(f"*Harga:* Rp {baju['Harga']:,}")
            st.write(f"*Stok:* {baju['Stok']}")
        with col3:
            jumlah = st.number_input(f"Jumlah untuk {baju['Nama']}", min_value=0, max_value=baju["Stok"], step=1, key=baju["Nama"])
            if st.button(f"Tambah {baju['Nama']}", key=f"btn-{baju['Nama']}"):
                tambah_ke_keranjang(baju["Nama"], baju["Harga"], jumlah, baju["Stok"])

    if st.button("Lihat Keranjang"):
        ganti_halaman("Keranjang")

# Halaman Keranjang
elif st.session_state.page == "Keranjang" and st.session_state.logged_in:
    st.title("Keranjang Belanja Anda")
    
    if st.session_state.keranjang:
        total_harga = sum(item["Subtotal"] for item in st.session_state.keranjang)
        st.session_state.total_harga = total_harga
        
        for idx, item in enumerate(st.session_state.keranjang):
            st.write(f"{idx+1}. *{item['Nama']}* - {item['Jumlah']} x Rp {item['Harga']:,} = Rp {item['Subtotal']:,}")
        
        st.markdown("### Total Harga Sebelum Diskon")
        st.write(f"*Rp {total_harga:,}*")
        
        voucher = st.text_input("Masukkan kode voucher (opsional):")
        if st.button("Gunakan Voucher"):
            if voucher == "DISKON10":
                st.session_state.diskon = 0.1 * total_harga
                st.success("Voucher berhasil digunakan! Diskon 10% diterapkan.")
            else:
                st.warning("Kode voucher tidak valid.")
        
        total_setelah_diskon = total_harga - st.session_state.diskon
        st.markdown("### Total Harga Setelah Diskon")
        st.write(f"*Rp {total_setelah_diskon:,}*")
        
        if st.button("Lanjutkan ke Pembayaran"):
            ganti_halaman("Pembayaran")
    else:
        st.info("Keranjang Anda kosong.")
        if st.button("Kembali ke Katalog"):
            ganti_halaman("Katalog")

# Halaman Pembayaran
elif st.session_state.page == "Pembayaran" and st.session_state.logged_in:
    st.title("Konfirmasi Pembayaran")
    
    st.markdown("### Rincian Pesanan")
    for idx, item in enumerate(st.session_state.keranjang):
        st.write(f"{idx+1}. *{item['Nama']}* - {item['Jumlah']} x Rp {item['Harga']:,} = Rp {item['Subtotal']:,}")
    
    st.markdown("### Total Harga")
    st.write(f"*Rp {st.session_state.total_harga - st.session_state.diskon:,}*")
    
    st.markdown("### Estimasi Pengiriman")
    st.write("Pesanan Anda akan dikirim dalam waktu 2-3 hari kerja.")
    
    if st.button("Konfirmasi Pembayaran"):
        st.success("Pesanan Anda berhasil diproses! Terima kasih.")
        st.session_state.keranjang = []
        st.session_state.total_harga = 0
        st.session_state.diskon = 0
        ganti_halaman("Katalog")
    elif st.button("Kembali ke Keranjang"):
        ganti_halaman("Keranjang")
