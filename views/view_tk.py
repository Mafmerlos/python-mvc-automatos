import tkinter as tk
from tkinter import font as tkFont

BG_COLOR = "#f0f0f0"
BTN_COLOR = "#007bff"
BTN_FG_COLOR = "#ffffff"
LABEL_COLOR = "#333333"
TEXT_BG_COLOR = "#ffffff"
BORDER_COLOR = "#cccccc"

window = tk.Tk()
window.title("Analisador de Palavras do Autômato")
window.geometry("500x450")
window.configure(bg=BG_COLOR)
window.resizable(False, False)

FONT_BOLD = tkFont.Font(family="Arial", size=12, weight="bold")
FONT_BUTTON = tkFont.Font(family="Arial", size=10, weight="bold")
FONT_TEXT = tkFont.Font(family="Courier New", size=10)

frame_botoes = tk.Frame(window, bg=BG_COLOR)
frame_botoes.pack(pady=20)

btn_selecionar = tk.Button(
    frame_botoes,
    text="1. Selecionar Arquivos (txt)",
    font=FONT_BUTTON,
    bg=BTN_COLOR,
    fg=BTN_FG_COLOR,
    relief="flat",
    padx=15,
    pady=8,
    activebackground="#0056b3",
    activeforeground="#ffffff"
)
btn_selecionar.grid(row=0, column=0, padx=10)

btn_processar = tk.Button(
    frame_botoes,
    text="2. Processar Palavras",
    font=FONT_BUTTON,
    bg=BTN_COLOR,
    fg=BTN_FG_COLOR,
    relief="flat",
    padx=15,
    pady=8,
    activebackground="#0056b3",
    activeforeground="#ffffff"
)
btn_processar.grid(row=0, column=1, padx=10)

frame_resultados = tk.Frame(window, bg=BG_COLOR)
frame_resultados.pack(padx=20, pady=(0, 20), fill="both", expand=True)

lbl_resultados = tk.Label(
    frame_resultados,
    text="Resultados:",
    font=FONT_BOLD,
    bg=BG_COLOR,
    fg=LABEL_COLOR
)
lbl_resultados.pack(anchor="w", pady=(0, 5))

text_frame = tk.Frame(
    frame_resultados,
    bg=BORDER_COLOR,
    borderwidth=1,
    relief="solid"
)
text_frame.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side="right", fill="y")

txt_resultados = tk.Text(
    text_frame,
    height=15,
    font=FONT_TEXT,
    bg=TEXT_BG_COLOR,
    fg=LABEL_COLOR,
    relief="flat",
    borderwidth=0,
    yscrollcommand=scrollbar.set
)
txt_resultados.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt_resultados.yview)

window.mainloop()