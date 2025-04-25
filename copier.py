import shutil
import subprocess
import uuid
import os

# オリジナルのファイル
original_file = "original_script.py"

# ランダムなファイル名生成（UUIDを使用）
while True:
    random_filename = f"{uuid.uuid4().hex}.py"
    if not os.path.exists(random_filename):
        break  # 同名ファイルが存在しない場合のみ使用

# ファイルをコピー
shutil.copy(original_file, random_filename)

# コピーしたファイルを実行
subprocess.run(["python", random_filename])

print(f"Copied and executed file: {random_filename}")
