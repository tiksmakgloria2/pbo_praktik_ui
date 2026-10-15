import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def buka_tambah_buku():
    subprocess.Popen([sys.executable, os.path.join(BASE_DIR, "tambah_buku.py")])


def buka_tampil_buku():
    subprocess.Popen([sys.executable, os.path.join(BASE_DIR, "tampil_buku.py")])


def keluar(root):
    if messagebox.askyesno("Konfirmasi", "Apakah Anda ingin keluar dari aplikasi?"):
        root.destroy()


def menu_utama():
    root = tk.Tk()
    root.title("Sistem Perpustakaan")
    root.geometry("520x390")
    root.resizable(False, False)
    root.configure(bg="#eef3f8")

    header = tk.Frame(root, bg="#174a7e", height=95)
    header.pack(fill="x")
    header.pack_propagate(False)

    tk.Label(
        header,
        text="SISTEM PERPUSTAKAAN",
        font=("Arial", 20, "bold"),
        bg="#174a7e",
        fg="white",
    ).pack(pady=(20, 2))

    tk.Label(
        header,
        text="Aplikasi Pengelolaan Data Buku",
        font=("Arial", 10),
        bg="#174a7e",
        fg="#dcecff",
    ).pack()

    content = tk.Frame(root, bg="#eef3f8")
    content.pack(fill="both", expand=True, padx=55, pady=32)

    tk.Button(
        content,
        text="Tambah Buku",
        command=buka_tambah_buku,
        font=("Arial", 12, "bold"),
        bg="#198754",
        fg="white",
        activebackground="#146c43",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        height=2,
    ).pack(fill="x", pady=7)

    tk.Button(
        content,
        text="Tampilkan Buku",
        command=buka_tampil_buku,
        font=("Arial", 12, "bold"),
        bg="#0d6efd",
        fg="white",
        activebackground="#0a58ca",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        height=2,
    ).pack(fill="x", pady=7)

    tk.Button(
        content,
        text="Keluar",
        command=lambda: keluar(root),
        font=("Arial", 12, "bold"),
        bg="#dc3545",
        fg="white",
        activebackground="#b02a37",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        height=2,
    ).pack(fill="x", pady=7)

    root.protocol("WM_DELETE_WINDOW", lambda: keluar(root))
    root.mainloop()


if __name__ == "__main__":
    menu_utama()
