import streamlit as st
import pandas as pd

# Data penjualan baju
data_baju = {
    "Nama Baju": ["Baju Motif Dinosaurus", "Baju Motif Bunga", "Baju Motif Polkadot", "Baju Motif Hewan", "Baju Motif Buah"],
    "Harga": [100000, 95000, 90000, 110000, 90000],
    "Stok": [10, 20, 30, 40, 50],
    "Deskripsi": ["Baju motif Dinosaurus untuk anak anak usia 2-6 tahun", "Baju mottif Bunga cocok untuk anak anak yang menyukai desain cantik dan elegant", "Baju motif Polkadot cocok untuk sehari hari atau acara khusus untuk umur 1-10 tahun", "Baju motif Hewan dapat meningkatkan kreativitas dan imanjinasi anak anak dengan desain yang unik ", "Baju motif Buah dengan desain buah yang beragam serta warna warna cerah dan menarik"]
}

# Buat DataFrame dari data penjualan baju
df_baju = pd.DataFrame(data_baju)

# Buat aplikasi Streamlit
st.title("TOKO BAJU ANDALAN")
st.write("Selamat datang di toko baju Andalan kami!")

# Tampilkan data penjualan baju
st.write("Data Penjualan Baju:")
st.write(df_baju)

# Buat tab untuk menampilkan detail baju
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Baju Motif Dinosaurus", "Baju Motif Bunga", "Baju Motif Polkadot", "Baju Motif Hewan", "Baju Motif Buah"])

# Tampilkan detail baju motoif Dinosaurus
with tab1:
    st.write("Detail Baju motif Dinosaurus:")
    st.write(f"Nama Baju: {df_baju['Nama Baju'][0]}")
    st.write(f"Harga: {df_baju['Harga'][0]}")
    st.write(f"Stok: {df_baju['Stok'][0]}")
    st.write(f"Deskripsi: {df_baju['Deskripsi'][0]}")

# Tampilkan detail baju motif Bunga
with tab2:
    st.write("Detail Baju motif Bunga:")
    st.write(f"Nama Baju: {df_baju['Nama Baju'][1]}")
    st.write(f"Harga: {df_baju['Harga'][1]}")
    st.write(f"Stok: {df_baju['Stok'][1]}")
    st.write(f"Deskripsi: {df_baju['Deskripsi'][1]}")

# Tampilkan detail baju motif Polkadot
with tab3:
    st.write("Detail Baju motif Polkadot:")
    st.write(f"Nama Baju: {df_baju['Nama Baju'][2]}")
    st.write(f"Harga: {df_baju['Harga'][2]}")
    st.write(f"Stok: {df_baju['Stok'][2]}")
    st.write(f"Deskripsi: {df_baju['Deskripsi'][2]}")

# Tampilkan detail baju motif Hewan
with tab4:
    st.write("Detail Baju motif Hewan:")
    st.write(f"Nama Baju: {df_baju['Nama Baju'][3]}")
    st.write(f"Harga: {df_baju['Harga'][3]}")
    st.write(f"Stok: {df_baju['Stok'][3]}")
    st.write(f"Deskripsi: {df_baju['Deskripsi'][3]}")

# Tampilkan detail baju motif Buah 
with tab5:
    st.write("Detail Baju motif Buah:")
    st.write(f"Nama Baju: {df_baju['Nama Baju'][4]}")
    st.write(f"Harga: {df_baju['Harga'][4]}")
    st.write(f"Stok: {df_baju['Stok'][4]}")
    st.write(f"Deskripsi: {df_baju['Deskripsi'][4]}")

# Buat form untuk memesan baju
st.write("Pesan Baju:")
with st.form("pesan_baju"):
    nama_baju = st.selectbox("Pilih Nama Baju", df_baju["Nama Baju"])
    jumlah = st.number_input("Jumlah", min_value=1, max_value=100)
    submit = st.form_submit_button("Pesan")

# Proses pesanan baju
if submit:
    st.write("Pesanan Anda:")
    st.write(f"Nama Baju: {nama_baju}")
    st.write(f"Jumlah: {jumlah}")
    st.write("Terima kasih telah memesan baju di kami!")
