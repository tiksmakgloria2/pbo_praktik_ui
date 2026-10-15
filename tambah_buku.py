import csv
import os
import tkinter as tk
from tkinter import messagebox
from models import Buku

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_BUKU = os.path.join(BASE_DIR, "buku.csv")


def simpan_buku(entry_judul, entry_penulis, entry_isbn):
    judul = entry_judul.get().strip()
    penulis = entry_penulis.get().strip()
    isbn = entry_isbn.get().strip()

    if not judul or not penulis or not isbn:
        messagebox.showwarning("Peringatan", "Semua kolom harus diisi!")
        return

    buku = Buku(judul, penulis, isbn)
    file_exists = os.path.exists(FILE_BUKU) and os.path.getsize(FILE_BUKU) > 0

    with open(FILE_BUKU, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Judul", "Penulis", "ISBN", "Status"])
        writer.writerow(buku.to_list())

    messagebox.showinfo("Berhasil", "Buku berhasil ditambahkan.")
    entry_judul.delete(0, tk.END)
    entry_penulis.delete(0, tk.END)
    entry_isbn.delete(0, tk.END)
    entry_judul.focus()


def main():
    root = tk.Tk()
    root.title("Tambah Data Buku")
    root.geometry("540x440")
    root.resizable(False, False)
    root.configure(bg="#f4f7fb")

    header = tk.Frame(root, bg="#198754", height=85)
    header.pack(fill="x")
    header.pack_propagate(False)

    tk.Label(
        header,
        text="TAMBAH DATA BUKU",
        font=("Arial", 19, "bold"),
        bg="#198754",
        fg="white",
    ).pack(pady=25)

    form = tk.Frame(root, bg="white", padx=30, pady=25, highlightthickness=1, highlightbackground="#d9e1ea")
    form.pack(fill="both", expand=True, padx=38, pady=28)

    tk.Label(form, text="Judul Buku", font=("Arial", 10, "bold"), bg="white").pack(anchor="w")
    entry_judul = tk.Entry(form, font=("Arial", 11), relief="solid", bd=1)
    entry_judul.pack(fill="x", ipady=7, pady=(5, 14))

    tk.Label(form, text="Penulis", font=("Arial", 10, "bold"), bg="white").pack(anchor="w")
    entry_penulis = tk.Entry(form, font=("Arial", 11), relief="solid", bd=1)
    entry_penulis.pack(fill="x", ipady=7, pady=(5, 14))

    tk.Label(form, text="ISBN", font=("Arial", 10, "bold"), bg="white").pack(anchor="w")
    entry_isbn = tk.Entry(form, font=("Arial", 11), relief="solid", bd=1)
    entry_isbn.pack(fill="x", ipady=7, pady=(5, 20))

    tombol = tk.Frame(form, bg="white")
    tombol.pack(fill="x")

    tk.Button(
        tombol,
        text="Simpan Buku",
        command=lambda: simpan_buku(entry_judul, entry_penulis, entry_isbn),
        font=("Arial", 10, "bold"),
        bg="#198754",
        fg="white",
        relief="flat",
        cursor="hand2",
        width=18,
    ).pack(side="left", ipady=7)

    tk.Button(
        tombol,
        text="Keluar",
        command=root.destroy,
        font=("Arial", 10, "bold"),
        bg="#6c757d",
        fg="white",
        relief="flat",
        cursor="hand2",
        width=12,
    ).pack(side="right", ipady=7)

    entry_judul.focus()
    root.bind("<Return>", lambda event: simpan_buku(entry_judul, entry_penulis, entry_isbn))
    root.mainloop()


if __name__ == "__main__":
    main()
