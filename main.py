import sys
import os
import tkinter as tk
from tkinter import messagebox
import random
import threading
import pygame

# 初始化 pygame 混音器，用于播放音频
pygame.mixer.init()

def resource_path(relative_path):
    """获取资源的绝对路径，适用于开发和 PyInstaller 打包后的一体化执行环境"""
    try:
        base_path = sys._MEIPASS  # PyInstaller 临时文件夹路径
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_audio_filename(text):
    # 根据平假名生成对应的音频文件名（与下载代码保持一致），并通过 resource_path 定位
    code = "-".join(format(ord(c), 'x') for c in text)
    return resource_path(f"audio/{code}.mp3")

def speak_japanese(kana):
    def play():
        try:
            filename = get_audio_filename(kana)
            if not os.path.exists(filename):
                messagebox.showerror("错误", f"音频文件不存在：{filename}")
                return
            sound = pygame.mixer.Sound(filename)
            sound.play()
        except Exception as e:
            messagebox.showerror("错误", f"音频播放失败：{str(e)}")
    threading.Thread(target=play).start()

# 切换按钮状态：循环显示【平假名 → 罗马字 → 片假名 → 罗马字】
def toggle_kana(button, group):
    button.state = (button.state + 1) % 4
    if button.state == 0:
        new_text = group[0]  # 平假名
        new_color = 'lightblue'
    elif button.state == 1:
        new_text = group[1]  # 罗马字
        new_color = 'lightyellow'
    elif button.state == 2:
        new_text = group[2]  # 片假名
        new_color = 'lightgreen'
    elif button.state == 3:
        new_text = group[1]  # 罗马字
        new_color = 'lightyellow'
    button.config(text=new_text, bg=new_color)
    # 无论当前显示什么，都播放对应假名（group[0]）的日语发音
    speak_japanese(group[0])

# 假名数据
seion = [
    ['あ', 'a', 'ア'], ['い', 'i', 'イ'], ['う', 'u', 'ウ'],
    ['え', 'e', 'エ'], ['お', 'o', 'オ'], ['か', 'ka', 'カ'],
    ['き', 'ki', 'キ'], ['く', 'ku', 'ク'], ['け', 'ke', 'ケ'],
    ['こ', 'ko', 'コ'], ['さ', 'sa', 'サ'], ['し', 'shi', 'シ'],
    ['す', 'su', 'ス'], ['せ', 'se', 'セ'], ['そ', 'so', 'ソ'],
    ['た', 'ta', 'タ'], ['ち', 'chi', 'チ'], ['つ', 'tsu', 'ツ'],
    ['て', 'te', 'テ'], ['と', 'to', 'ト'], ['な', 'na', 'ナ'],
    ['に', 'ni', 'ニ'], ['ぬ', 'nu', 'ヌ'], ['ね', 'ne', 'ネ'],
    ['の', 'no', 'ノ'], ['は', 'ha', 'ハ'], ['ひ', 'hi', 'ヒ'],
    ['ふ', 'fu', 'フ'], ['へ', 'he', 'ヘ'], ['ほ', 'ho', 'ホ'],
    ['ま', 'ma', 'マ'], ['み', 'mi', 'ミ'], ['む', 'mu', 'ム'],
    ['め', 'me', 'メ'], ['も', 'mo', 'モ'], ['や', 'ya', 'ヤ'],
    ['ゆ', 'yu', 'ユ'], ['よ', 'yo', 'ヨ'], ['ら', 'ra', 'ラ'],
    ['り', 'ri', 'リ'], ['る', 'ru', 'ル'], ['れ', 're', 'レ'],
    ['ろ', 'ro', 'ロ'], ['わ', 'wa', 'ワ'], ['を', 'wo', 'ヲ'],
    ['ん', 'n', 'ン']
]

dakuon = [
    ['が', 'ga', 'ガ'], ['ぎ', 'gi', 'ギ'], ['ぐ', 'gu', 'グ'],
    ['げ', 'ge', 'ゲ'], ['ご', 'go', 'ゴ'], ['ざ', 'za', 'ザ'],
    ['じ', 'ji', 'ジ'], ['ず', 'zu', 'ズ'], ['ぜ', 'ze', 'ゼ'],
    ['ぞ', 'zo', 'ゾ'], ['だ', 'da', 'ダ'], ['ぢ', 'ji', 'ヂ'],
    ['づ', 'zu', 'ヅ'], ['で', 'de', 'デ'], ['ど', 'do', 'ド'],
    ['ば', 'ba', 'バ'], ['び', 'bi', 'ビ'], ['ぶ', 'bu', 'ブ'],
    ['べ', 'be', 'ベ'], ['ぼ', 'bo', 'ボ'], ['ぱ', 'pa', 'パ'],
    ['ぴ', 'pi', 'ピ'], ['ぷ', 'pu', 'プ'], ['ぺ', 'pe', 'ペ'],
    ['ぽ', 'po', 'ポ']
]

youon = [
    ['きゃ', 'kya', 'キャ'], ['きゅ', 'kyu', 'キュ'], ['きょ', 'kyo', 'キョ'],
    ['しゃ', 'sha', 'シャ'], ['しゅ', 'shu', 'シュ'], ['しょ', 'sho', 'ショ'],
    ['ちゃ', 'cha', 'チャ'], ['ちゅ', 'chu', 'チュ'], ['ちょ', 'cho', 'チョ'],
    ['にゃ', 'nya', 'ニャ'], ['にゅ', 'nyu', 'ニュ'], ['にょ', 'nyo', 'ニョ'],
    ['ひゃ', 'hya', 'ヒャ'], ['ひゅ', 'hyu', 'ヒュ'], ['ひょ', 'hyo', 'ヒョ'],
    ['みゃ', 'mya', 'ミャ'], ['みゅ', 'myu', 'ミュ'], ['みょ', 'myo', 'ミョ'],
    ['りゃ', 'rya', 'リャ'], ['りゅ', 'ryu', 'リュ'], ['りょ', 'ryo', 'リョ'],
    ['ぎゃ', 'gya', 'ギャ'], ['ぎゅ', 'gyu', 'ギュ'], ['ぎょ', 'gyo', 'ギョ'],
    ['じゃ', 'ja', 'ジャ'], ['じゅ', 'ju', 'ジュ'], ['じょ', 'jo', 'ジョ'],
    ['びゃ', 'bya', 'ビャ'], ['びゅ', 'byu', 'ビュ'], ['びょ', 'byo', 'ビョ'],
    ['ぴゃ', 'pya', 'ピャ'], ['ぴゅ', 'pyu', 'ピュ'], ['ぴょ', 'pyo', 'ピョ']
]

def generate_groups():
    info_label.pack_forget()  # 结果生成后移除提示

    for widget in result_frame.winfo_children():
        widget.destroy()

    selected_groups = []
    if seion_var.get():
        selected_groups.extend(seion)
    if dakuon_var.get():
        selected_groups.extend(dakuon)
    if youon_var.get():
        selected_groups.extend(youon)

    if not selected_groups:
        messagebox.showerror("错误", "请至少选择一个假名类型")
        return

    total = len(selected_groups)
    if total > 119:
        messagebox.showerror("错误", f"选择的假名数量（{total}）超过119，请减少选择")
        return

    random.shuffle(selected_groups)
    if total < 119:
        selected_groups += random.choices(selected_groups, k=119 - total)

    for idx, group in enumerate(selected_groups):
        initial_state = random.choice([0, 2])  # 0：平假名；2：片假名
        if initial_state == 0:
            text = group[0]
            color = 'lightblue'
        else:
            text = group[2]
            color = 'lightgreen'
        btn = tk.Button(
            result_frame,
            text=text,
            bg=color,
            font=("Arial", 20, "bold"),
            width=4,
            height=2,
            wraplength=100
        )
        btn.state = initial_state
        btn.config(command=lambda b=btn, g=group: toggle_kana(b, g))
        btn.grid(row=idx // 17, column=idx % 17, padx=5, pady=5)

root = tk.Tk()
root.title("假名学习工具")
root.state('zoomed')

selection_frame = tk.Frame(root)
selection_frame.pack(pady=10)

seion_var = tk.BooleanVar(value=True)
dakuon_var = tk.BooleanVar()
youon_var = tk.BooleanVar()

tk.Checkbutton(selection_frame, text="清音（46个）", variable=seion_var,
               font=("微软雅黑", 14, "bold")).grid(row=0, column=0, padx=10)
tk.Checkbutton(selection_frame, text="浊音（25个）", variable=dakuon_var,
               font=("微软雅黑", 14, "bold")).grid(row=0, column=1, padx=10)
tk.Checkbutton(selection_frame, text="拗音（33个）", variable=youon_var,
               font=("微软雅黑", 14, "bold")).grid(row=0, column=2, padx=10)

generate_btn = tk.Button(root, text="生成假名表", command=generate_groups,
                         font=("微软雅黑", 16, "bold"), bg="#4CAF50", fg="white")
generate_btn.pack(pady=15)

result_frame = tk.Frame(root)
result_frame.pack(padx=20, pady=10)

info_label = tk.Label(root,
                      text="点击假名后依次显示：平假名 → 罗马字 → 片假名 → 罗马字\n并自动播放对应发音（均为日语发音）",
                      font=("微软雅黑", 16, "bold"), fg="gray")
info_label.pack(pady=10)

root.mainloop()
