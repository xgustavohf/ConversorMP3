import os
import tkinter as tk
from pytube import YouTube
from tkinter import simpledialog, messagebox

ROOT = tk.Tk()
ROOT.withdraw()

def input_data(title, prompt):
    result = simpledialog.askstring(title=title, prompt=prompt)
    return result

video_link = input_data("Vídeo Link", "Insira o link do Vídeo: ")

yt = YouTube(video_link)

print(f'Título: {yt.title}')
print(f'Visualizações: {yt.views}')

yd = yt.streams.filter(only_audio=True).first()

#download_path = input_data("Download", "Insira o caminho do download:")

download_file = yd.download()
base, ext = os.path.splitext(download_file)

new_file = base + '.mp3'
os.rename(download_file, new_file)

messagebox.showinfo("Mensagem", f'Download concluído com sucesso em {download_file}')
messagebox.showinfo("Mensagem", f'Criado por Gustavo Henrique Ferreira')