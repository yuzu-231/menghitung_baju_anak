import streamlit as st
import json
import os

# Path file untuk menyimpan data
USER_DATA_FILE = "user_data.json"
STOK_FILE = "stok.json"

# Fungsi untuk membaca data dari file
def baca_data(file, default):
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    else:
        with open(file, "w") as f:
            json.dump(default, f)
        return default

# Fungsi untuk menyimpan data ke file
def simpan_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f)

# Data awal
users = baca_data(USER_DATA_FILE, [])
stok_awal = {
    "Baju Anak Motif Dinosaurus": 10,
    "Baju Anak Motif Bunga": 15,
    "Baju Anak Motif Mobil": 8,
    "Baju Anak Motif Hewan": 5,
    "Baju Anak Motif Buah": 12,
    "Baju Anak Motif Kartun": 7,
    "Baju Anak Motif Polkadot": 20,
    "Baju Anak Motif Pelangi": 18,
    "Baju Anak Motif Bintang": 12,
    "Baju Anak Motif Luar Angkasa": 10,
}
stok = baca_data(STOK_FILE, stok_awal)

# Inisialisasi session state
if "page" not in st.session_state:
    st.session_state.page = "Login"
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []
if "user_logged_in" not in st.session_state:
    st.session_state.user_logged_in = None
if "total_harga" not in st.session_state:
    st.session_state.total_harga = 0

# Fungsi navigasi
def navigate(page):
    st.session_state.page = page

# Halaman Login
if st.session_state.page == "Login":
    st.title("Login / Daftar")
    login_tab, register_tab = st.tabs(["Login", "Daftar"])

    with login_tab:
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            for user in users:
                if user["username"] == username and user["password"] == password:
                    st.session_state.user_logged_in = user
                    navigate("Katalog")
                    st.success(f"Selamat datang, {username}!")
                    break
            else:
                st.error("Username atau password salah.")

    with register_tab:
        new_username = st.text_input("Username Baru", key="reg_user")
        new_password = st.text_input("Password Baru", type="password", key="reg_pass")
        alamat = st.text_area("Alamat", key="reg_alamat")
        nomor_hp = st.text_input("Nomor HP", key="reg_hp")
        if st.button("Daftar"):
            users.append({
                "username": new_username,
                "password": new_password,
                "alamat": alamat,
                "nomor_hp": nomor_hp,
            })
            simpan_data(USER_DATA_FILE, users)
            st.success("Pendaftaran berhasil! Silakan login.")

# Halaman Katalog
elif st.session_state.page == "Katalog":
    st.title("Katalog Baju Anak")
    for nama, stok_produk in stok.items():
        col1, col2 = st.columns([2, 1])
        with col1:
            st.subheader(nama)
            st.write(f"Stok: {stok_produk}")
        with col2:
            jumlah = st.number_input(f"Jumlah {nama}", min_value=0, max_value=stok_produk, step=1, key=f"jumlah_{nama}")
            if st.button(f"Tambah {nama} ke Keranjang", key=f"btn_{nama}"):
                if jumlah > 0:
                    stok[nama] -= jumlah
                    st.session_state.keranjang.append({"Nama": nama, "Jumlah": jumlah})
                    simpan_data(STOK_FILE, stok)
                    st.success(f"{jumlah} {nama} ditambahkan ke keranjang.")
                else:
                    st.error("Jumlah tidak boleh 0.")

    if st.button("Lihat Keranjang"):
        navigate("Keranjang")

# Halaman Keranjang
elif st.session_state.page == "Keranjang":
    st.title("Keranjang Belanja")
    if st.session_state.keranjang:
        total = 0
        for item in st.session_state.keranjang:
            st.write(f"{item['Nama']} - Jumlah: {item['Jumlah']}")
            total += item["Jumlah"]
        st.write(f"Total Barang: {total}")

        if st.button("Lanjutkan ke Pembayaran"):
            navigate("Pembayaran")
    else:
        st.warning("Keranjang kosong.")

# Halaman Pembayaran
elif st.session_state.page == "Pembayaran":
    st.title("Pembayaran")
    kode_voucher = st.text_input("Kode Voucher (Opsional)")
    st.write("Total Harga: Rp xxx")
    if st.button("Bayar"):
        navigate("Konfirmasi")

# Halaman Konfirmasi
elif st.session_state.page == "Konfirmasi":
    st.title("Pembayaran Berhasil")
    st.success("Terima kasih atas pembelian Anda!")
    if st.button("Kembali ke Katalog"):
        navigate("Katalog")
