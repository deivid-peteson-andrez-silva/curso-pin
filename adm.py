import tkinter as tk
from tkinter import font
import sys
import io

class ExecPythonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cod")
        self.root.geometry("700x600")
        self.root.configure(bg="#f5f5f5")

        # Fontes personalizadas
        self.font_label = font.Font(family="Segoe UI", size=12, weight="bold")
        self.font_code = font.Font(family="Consolas", size=11)

        # Título
        tk.Label(root, text=" Digite seu código Python:", font=self.font_label, bg="#f5f5f5", anchor="w").pack(padx=20, pady=(20, 5), fill="x")

        # Caixa de texto para código
        self.codigo_text = tk.Text(root, height=12, width=80, font=self.font_code, bd=2, relief="groove", bg="#ffffff")
        self.codigo_text.pack(padx=20, pady=5, fill="both", expand=True)

        # Botão de execução
        tk.Button(root, text="▶ Executar Código", font=("Segoe UI", 10), bg="#4CAF50", border=" 10px", fg="white", activebackground="#45a049",
                  relief="flat", padx=10, pady=6, command=self.executar_codigo).pack(pady=15)

        # Label de saída
        tk.Label(root, text="📤 Saída:", font=self.font_label, bg="#f5f5f5", anchor="w").pack(padx=20, pady=(10, 5), fill="x")

        # Caixa de texto para saída
        self.output_text = tk.Text(root, height=10, width=80, font=self.font_code, bg="#eeeeee", bd=2, relief="groove", state='disabled')
        self.output_text.pack(padx=20, pady=(0, 20), fill="both", expand=True)

    def executar_codigo(self):
        codigo = self.codigo_text.get("1.0", tk.END)

        buffer = io.StringIO()
        sys_stdout_original = sys.stdout
        sys_stderr_original = sys.stderr
        sys.stdout = sys.stderr = buffer

        try:
            exec(codigo, {})  # Executa código em escopo isolado
        except Exception as e:
            print(f"Erro: {e}")
        finally:
            sys.stdout = sys_stdout_original
            sys.stderr = sys_stderr_original
  
        resultado = buffer.getvalue()
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, resultado)
        self.output_text.config(state='disabled')

# Roda a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = ExecPythonApp(root)
    root.mainloop()
