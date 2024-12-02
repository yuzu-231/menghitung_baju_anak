import streamlit as st

st.title("Menghitung_Baju_Anak")
import streamlit as st

# Data baju anak
baju_anak = [
    {"Nama": "Baju Anak Motif Bunga", "Motif": "Bunga", "Harga": 100000},
    {"Nama": "Baju Anak Motif Garis", "Motif": "Garis", "Harga": 95000},
    {"Nama": "Baju Anak Motif Polkadot", "Motif": "Polkadot", "Harga": 85000},
    {"Nama": "Baju Anak Motif Kartun", "Motif": "Kartun", "Harga": 120000},
    {"Nama": "Baju Anak Motif Hewan", "Motif": "Hewan", "Harga": 105000},
    {"Nama": "Baju Anak Motif Abstrak", "Motif": "Abstrak", "Harga": 98000},
    {"Nama": "Baju Anak Motif Batik", "Motif": "Batik", "Harga": 115000},
    {"Nama": "Baju Anak Motif Army", "Motif": "Army", "Harga": 110000},
    {"Nama": "Baju Anak Motif Stripe", "Motif": "Stripe", "Harga": 90000},
    {"Nama": "Baju Anak Motif Geometris", "Motif": "Geometris", "Harga": 102000},
]

# Judul Aplikasi
st.title("Daftar Baju Anak")

# Tampilkan daftar baju
st.subheader("Berikut adalah daftar baju anak dengan motif dan harga berbeda:")
for baju in baju_anak:
    st.write(f"*Nama*: {baju['Nama']}")
    st.write(f"*Motif*: {baju['Motif']}")
    st.write(f"*Harga*: Rp{baju['Harga']:,}")
    st.write("---")

# Footer
st.write("Terima kasih telah mengunjungi aplikasi kami!")
