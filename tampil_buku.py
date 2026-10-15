import csv
import os
import tkinter as tk
from tkinter import ttk, messagebox
from models import Buku

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_BUKU = os.path.join(BASE_DIR, "buku.csv")


def muat_data():
    daftar_buku = []

    if not os.path.exists(FILE_BUKU):
        return daftar_buku

    with open(FILE_BUKU, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if len(row) >= 4:
                buku = Buku(
                    judul=row[0],
                    penulis=row[1],
                    isbn=row[2],
                    status=row[3],
                )
                daftar_buku.append(buku)

    return daftar_buku


def tampilkan_buku(tree, label_total):
    for item in tree.get_children():
        tree.delete(item)

    daftar_buku = muat_data()

    for nomor, buku in enumerate(daftar_buku, start=1):
        tree.insert(
            "",
            "end",
            values=(nomor, buku.judul, buku.penulis, buku.isbn, buku.status),
        )

    label_total.config(text=f"Total Buku: {len(daftar_buku)}")

    if not daftar_buku:
        messagebox.showinfo("Informasi", "Tidak ada data buku.")


def main():
    root = tk.Tk()
    root.title("Daftar Buku Perpustakaan")
    root.geometry("920x520")
    root.minsize(760, 430)
    root.configure(bg="#f4f7fb")

    header = tk.Frame(root, bg="#0d6efd", height=82)
    header.pack(fill="x")
    header.pack_propagate(False)

    tk.Label(
        header,
        text="DAFTAR BUKU PERPUSTAKAAN",
        font=("Arial", 19, "bold"),
        bg="#0d6efd",
        fg="white",
    ).pack(pady=23)

    content = tk.Frame(root, bg="#f4f7fb")
    content.pack(fill="both", expand=True, padx=25, pady=22)

    tabel_frame = tk.Frame(content, bg="white")
    tabel_frame.pack(fill="both", expand=True)

    kolom = ("no", "judul", "penulis", "isbn", "status")
    tree = ttk.Treeview(tabel_frame, columns=kolom, show="headings")

    tree.heading("no", text="No.")
    tree.heading("judul", text="Judul")
    tree.heading("penulis", text="Penulis")
    tree.heading("isbn", text="ISBN")
    tree.heading("status", text="Status")

    tree.column("no", width=55, anchor="center", stretch=False)
    tree.column("judul", width=260)
    tree.column("penulis", width=205)
    tree.column("isbn", width=170, anchor="center")
    tree.column("status", width=120, anchor="center")

    scrollbar_y = ttk.Scrollbar(tabel_frame, orient="vertical", command=tree.yview)
    scrollbar_x = ttk.Scrollbar(tabel_frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    tree.grid(row=0, column=0, sticky="nsew")
    scrollbar_y.grid(row=0, column=1, sticky="ns")
    scrollbar_x.grid(row=1, column=0, sticky="ew")
    tabel_frame.rowconfigure(0, weight=1)
    tabel_frame.columnconfigure(0, weight=1)

    footer = tk.Frame(content, bg="#f4f7fb")
    footer.pack(fill="x", pady=(15, 0))

    label_total = tk.Label(
        footer,
        text="Total Buku: 0",
        font=("Arial", 11, "bold"),
        bg="#f4f7fb",
        fg="#263238",
    )
    label_total.pack(side="left")

    tk.Button(
        footer,
        text="Refresh Data",
        command=lambda: tampilkan_buku(tree, label_total),
        font=("Arial", 10, "bold"),
        bg="#0d6efd",
        fg="white",
        relief="flat",
        cursor="hand2",
        width=15,
    ).pack(side="right", ipady=6, padx=(10, 0))

    tk.Button(
        footer,
        text="Keluar",
        command=root.destroy,
        font=("Arial", 10, "bold"),
        bg="#6c757d",
        fg="white",
        relief="flat",
        cursor="hand2",
        width=12,
    ).pack(side="right", ipady=6)

    tampilkan_buku(tree, label_total)
    root.mainloop()


if __name__ == "__main__":
    main()
