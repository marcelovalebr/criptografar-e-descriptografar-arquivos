import tkinter as tk
from tkinter import messagebox, filedialog
from cryptography.fernet import Fernet
import os

class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo de Criptografia de Dados")
        self.key = None
        self.create_widgets()

    def create_widgets(self):
        # Frame para Geração e Entrada de Chave
        key_frame = tk.LabelFrame(self.root, text="Chave", padx=10, pady=10)
        key_frame.pack(padx=10, pady=10, fill="x")

        tk.Label(key_frame, text="Chave:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.key_entry = tk.Entry(key_frame, width=50)
        self.key_entry.grid(row=0, column=1, padx=5, pady=5)

        self.generate_key_button = tk.Button(key_frame, text="Gerar Chave", command=self.generate_key)
        self.generate_key_button.grid(row=0, column=2, padx=5, pady=5)

        # Frame para Seleção de Arquivo/Pasta
        file_frame = tk.LabelFrame(self.root, text="Seleção de Arquivo/Pasta", padx=10, pady=10)
        file_frame.pack(padx=10, pady=10, fill="x")

        tk.Label(file_frame, text="Arquivo/Pasta:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.file_entry = tk.Entry(file_frame, width=50)
        self.file_entry.grid(row=0, column=1, padx=5, pady=5)

        self.browse_file_button = tk.Button(file_frame, text="Selecionar Arquivo", command=self.browse_file)
        self.browse_file_button.grid(row=0, column=2, padx=5, pady=5)

        self.browse_folder_button = tk.Button(file_frame, text="Selecionar Pasta", command=self.browse_folder)
        self.browse_folder_button.grid(row=1, column=2, padx=5, pady=5)

        # Frame para Entrada de Extensão
        ext_frame = tk.LabelFrame(self.root, text="Extensão", padx=10, pady=10)
        ext_frame.pack(padx=10, pady=10, fill="x")

        tk.Label(ext_frame, text="Extensão:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.ext_entry = tk.Entry(ext_frame, width=10)
        self.ext_entry.grid(row=0, column=1, padx=5, pady=5)
        self.ext_entry.insert(0, "enc")  # Extensão padrão

        # Frame para Ações
        action_frame = tk.Frame(self.root, padx=10, pady=10)
        action_frame.pack(padx=10, pady=10)

        self.encrypt_button = tk.Button(action_frame, text="Criptografar", command=self.encrypt, width=15)
        self.encrypt_button.grid(row=0, column=0, padx=10, pady=5)

        self.decrypt_button = tk.Button(action_frame, text="Descriptografar", command=self.decrypt, width=15)
        self.decrypt_button.grid(row=0, column=1, padx=10, pady=5)

    def generate_key(self):
        self.key = Fernet.generate_key()
        self.key_entry.delete(0, tk.END)
        self.key_entry.insert(0, self.key.decode())
        messagebox.showinfo("Chave Gerada", "Uma nova chave de criptografia foi gerada.")

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, folder_path)

    def encrypt(self):
        path = self.file_entry.get()
        extension = self.ext_entry.get()
        if not path:
            messagebox.showerror("Erro", "Por favor, selecione um arquivo ou pasta para criptografar.")
            return

        if not self.key_entry.get():
            messagebox.showerror("Erro", "Por favor, gere ou insira uma chave de criptografia.")
            return

        if not extension:
            messagebox.showerror("Erro", "Por favor, insira uma extensão.")
            return

        self.key = self.key_entry.get().encode()
        cipher_suite = Fernet(self.key)

        if os.path.isfile(path):
            self.encrypt_file(cipher_suite, path, extension)
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    self.encrypt_file(cipher_suite, file_path, extension)
        messagebox.showinfo("Sucesso", "Criptografia concluída.")

    def decrypt(self):
        path = self.file_entry.get()
        extension = self.ext_entry.get()
        if not path:
            messagebox.showerror("Erro", "Por favor, selecione um arquivo ou pasta para descriptografar.")
            return

        if not self.key_entry.get():
            messagebox.showerror("Erro", "Por favor, gere ou insira uma chave de criptografia.")
            return

        if not extension:
            messagebox.showerror("Erro", "Por favor, insira uma extensão.")
            return

        self.key = self.key_entry.get().encode()
        cipher_suite = Fernet(self.key)

        if os.path.isfile(path):
            self.decrypt_file(cipher_suite, path, extension)
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    self.decrypt_file(cipher_suite, file_path, extension)
        messagebox.showinfo("Sucesso", "Descriptografia concluída.")

    def encrypt_file(self, cipher_suite, file_path, extension):
        try:
            with open(file_path, 'rb') as file:
                file_data = file.read()

            encrypted_data = cipher_suite.encrypt(file_data)

            encrypted_file_path = f"{file_path}.{extension}"
            with open(encrypted_file_path, 'wb') as file:
                file.write(encrypted_data)

            os.remove(file_path)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao criptografar o arquivo {file_path}: {str(e)}")

    def decrypt_file(self, cipher_suite, file_path, extension):
        try:
            if not file_path.endswith(f".{extension}"):
                return

            with open(file_path, 'rb') as file:
                encrypted_data = file.read()

            decrypted_data = cipher_suite.decrypt(encrypted_data)

            original_file_path = file_path.rsplit(f".{extension}", 1)[0]
            with open(original_file_path, 'wb') as file:
                file.write(decrypted_data)

            os.remove(file_path)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao descriptografar o arquivo {file_path}: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()
