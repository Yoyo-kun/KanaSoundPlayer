import os
import PyInstaller.__main__

script_name = "main.py"    # 主程序文件
audio_dir = "audio"        # 音频文件夹（相对路径）
icon_file = "NERV.ico"     # 图标文件（相对路径）

PyInstaller.__main__.run([
    script_name,
    "--onefile",                   # 生成单个 exe 文件
    "--noconsole",                 # 不显示控制台窗口
    "--icon", icon_file,           # 设置程序图标
    "--add-data", f"{audio_dir}{os.pathsep}{audio_dir}",  # 将 audio 文件夹添加进去
    "--name", "JapaneseAudioPlayer"  # 生成的 exe 文件名称
])
