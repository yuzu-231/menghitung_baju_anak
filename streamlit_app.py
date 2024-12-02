import streamlit as st

st.title("Menghitung Baju Anak")
import streamlit as st

# Data baju anak
baju_anak = [
    {"Nama": "Baju Anak Motif Bunga(1)", "Motif": "Bunga", "Harga": 100000},
    {"Nama": "Baju Anak Motif Garis(2)", "Motif": "Garis", "Harga": 95000},
    {"Nama": "Baju Anak Motif Polkadot(3)", "Motif": "Polkadot", "Harga": 85000},
    {"Nama": "Baju Anak Motif Kartun(4)", "Motif": "Kartun", "Harga": 120000},
    {"Nama": "Baju Anak Motif Hewan(5)", "Motif": "Hewan", "Harga": 105000},
    {"Nama": "Baju Anak Motif Abstrak(6)", "Motif": "Abstrak", "Harga": 98000},
    {"Nama": "Baju Anak Motif Batik(7)", "Motif": "Batik", "Harga": 115000},
    {"Nama": "Baju Anak Motif Army(8)", "Motif": "Army", "Harga": 110000},
    {"Nama": "Baju Anak Motif Stripe(9)", "Motif": "Stripe", "Harga": 90000},
    {"Nama": "Baju Anak Motif Geometris(10)", "Motif": "Geometris", "Harga": 102000},
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
 
baju = st.number_input("masukan baju anak yg ingin dibeli :" ,0)
jb = st.number_input("masukan jumlah baju :",0)

if st.button("Hitung Jumlah", type="primary"):
  loading = st.progress(0)
  for i in range(100):
    time.sleep(0.01)
    loading.progress(i+1)
      
# Footer
st.write("Terima kasih telah mengunjungi aplikasi kami!")
