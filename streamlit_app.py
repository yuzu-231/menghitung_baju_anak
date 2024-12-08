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
        st.write(f"Harga: Rp {baju['Harga']:,}")
        jumlah = st.number_input(f"Jumlah untuk {baju['Nama']}", min_value=0, max_value=10, step=1, key=baju["Nama"])
        total_harga += jumlah * baju["Harga"]


import tkinter as tk
from tkinter import messagebox


class ShoppingCartApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Keranjang Belanja")
        
        # Data keranjang
        self.cart = []
        
        # Elemen GUI
        self.create_widgets()
    
    def create_widgets(self):
        # Label dan Entry untuk menambahkan barang
        tk.Label(self.root, text="Nama Barang").grid(row=0, column=0, padx=10, pady=5)
        self.item_name = tk.Entry(self.root)
        self.item_name.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(self.root, text="Jumlah").grid(row=1, column=0, padx=10, pady=5)
        self.item_qty = tk.Entry(self.root)
        self.item_qty.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(self.root, text="Harga").grid(row=2, column=0, padx=10, pady=5)
        self.item_price = tk.Entry(self.root)
        self.item_price.grid(row=2, column=1, padx=10, pady=5)
        
        # Tombol untuk menambahkan barang
        tk.Button(self.root, text="Tambah ke Keranjang", command=self.add_to_cart).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Tampilkan keranjang
        self.cart_list = tk.Listbox(self.root, width=50, height=15)
        self.cart_list.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        # Tombol untuk menghitung total
        tk.Button(self.root, text="Hitung Total", command=self.calculate_total).grid(row=5, column=0, columnspan=2, pady=10)
    
    def add_to_cart(self):
        name = self.item_name.get()
        qty = self.item_qty.get()
        price = self.item_price.get()
        
        # Validasi input
        if not name or not qty or not price:
            messagebox.showwarning("Peringatan", "Mohon isi semua data barang!")
            return
        
        try:
            qty = int(qty)
            price = float(price)
        except ValueError:
            messagebox.showerror("Error", "Jumlah dan Harga harus berupa angka!")
            return
        
        # Tambahkan ke keranjang
        self.cart.append({"name": name, "qty": qty, "price": price})
        self.cart_list.insert(tk.END, f"{name} - Jumlah: {qty}, Harga: {price}")
        
        # Reset input
        self.item_name.delete(0, tk.END)
        self.item_qty.delete(0, tk.END)
        self.item_price.delete(0, tk.END)
    
    def calculate_total(self):
        if not self.cart:
            messagebox.showinfo("Info", "Keranjang kosong!")
            return
        
        total = sum(item["qty"] * item["price"] for item in self.cart)
        messagebox.showinfo("Total Harga", f"Total harga semua barang: Rp {total:.2f}")


if _name_ == "_main_":
    root = tk.Tk()
    app = ShoppingCartApp(root)
    root.mainloop()
# Menampilkan total harga
st.markdown("## Total Harga")
st.write(f"Rp {total_harga:,}")

# Tombol beli
if st.button("Beli Sekarang"):
    st.success("Terima kasih atas pembelian Anda!")
