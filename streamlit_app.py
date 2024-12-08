import streamlit as st
from PIL import Image

# Inisialisasi session state
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []
if "page" not in st.session_state:
    st.session_state.page = "Katalog"  # Halaman default
if "total_harga" not in st.session_state:
    st.session_state.total_harga = 0
if "riwayat_pesanan" not in st.session_state:
    st.session_state.riwayat_pesanan = []

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

        # Input kode diskon
        st.markdown("### Kode Diskon")
        kode_diskon = st.text_input("Masukkan kode diskon jika ada (contoh: DISKON10)")
        diskon = 0
        if kode_diskon == "DISKON10":
            diskon = 0.1 * total_harga
            st.success(f"Diskon 10% berhasil diterapkan! Anda hemat Rp {diskon:,}.")
        elif kode_diskon:
            st.error("Kode diskon tidak valid.")

        total_harga -= diskon
        st.markdown("### Total Harga Setelah Diskon")
        st.write(f"*Rp {total_harga:,}*")

        # Tombol untuk melanjutkan ke pembayaran
        if st.button("Lanjutkan ke Pembayaran"):
            st.session_state.total_harga = total_harga
            ganti_halaman("Pembayaran")
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

    # Opsi metode pembayaran
    st.markdown("### Pilih Metode Pembayaran")
    metode_pembayaran = st.radio("Metode Pembayaran", ["Transfer Bank", "E-Wallet", "COD"])

    # Tombol konfirmasi
    if st.button("Konfirmasi Pembayaran"):
        st.success("Pesanan Anda berhasil diproses! Terima kasih.")
        st.session_state.riwayat_pesanan.append({
            "Keranjang": st.session_state.keranjang.copy(),
            "Total": st.session_state.total_harga,
            "Metode Pembayaran": metode_pembayaran,
        })
        st.session_state.keranjang = []  # Reset keranjang setelah checkout
        st.session_state.total_harga = 0
        ganti_halaman("Riwayat")
    elif st.button("Kembali ke Keranjang"):
        ganti_halaman("Keranjang")

# Halaman Riwayat Pesanan
elif st.session_state.page == "Riwayat":
    st.title("Riwayat Pesanan")

    if st.session_state.riwayat_pesanan:
        for idx, pesanan in enumerate(st.session_state.riwayat_pesanan):
            st.markdown(f"### Pesanan {idx+1}")
            for item in pesanan["Keranjang"]:
                st.write(f"- *{item['Nama']}* - {item['Jumlah']} x Rp {item['Harga']:,}")
            st.write(f"*Total: Rp {pesanan['Total']:,}*")
            st.write(f"*Metode Pembayaran:* {pesanan['Metode Pembayaran']}")
            st.markdown("---")
    else:
        st.info("Belum ada riwayat pesanan.")
    
    if st.button("Kembali ke Katalog"):
        ganti_halaman("Katalog")
