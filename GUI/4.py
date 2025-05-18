import tkinter as tk
from tkinter import messagebox

class StickyNote:
    def __init__(self, master=None):
        self.window = tk.Toplevel(master) if master else tk.Tk()
        self.window.title("MyNote")
        self.window.geometry("400x400")
        self.frame_atas = tk.Frame(self.window)
        self.frame_atas.pack(pady=5)
        self.label_judul = tk.Label(self.frame_atas, text="Idea:") 
        self.label_judul.grid(row=0, column=0)
        self.entry_judul = tk.Entry(self.frame_atas, width=30)
        self.entry_judul.grid(row=0, column=1)
        self.text_catatan = tk.Text(self.window, height=10, width=35)
        self.text_catatan.pack(padx=10, pady=5)
        self.canvas = tk.Canvas(self.window, width=60, height=60, bg="pink", highlightthickness=2)
        self.canvas.create_rectangle(50, 50, 50, 50, fill="orange", outline="")
        self.canvas.pack()
        self.button_simpan = tk.Button(self.window, text="Simpan", command=self.simpan_catatan)
        self.button_simpan.pack(pady=10)

    def simpan_catatan(self):
        judul = self.entry_judul.get()
        isi = self.text_catatan.get("1.0", tk.END).strip()
        if not judul or not isi:
            messagebox.showwarning("Peringatan", "Judul dan isi tidak boleh kosong.")
        else:
            messagebox.showinfo("Tersimpan", f"Catatan '{judul}' disimpan!")

def buka_note_baru():
        StickyNote()

root = tk.Tk()
root.title("MyNote")
root.geometry("350x200")

label = tk.Label(root, text="Sticky Notes App", font=("Arial", 14))
label.pack(pady=10)

tombol_buka = tk.Button(root, text="Buat Note Baru", command=buka_note_baru)
tombol_buka.pack(pady=20)

root.mainloop()