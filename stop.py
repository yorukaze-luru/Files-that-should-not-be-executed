import os
import signal
import subprocess

def stop_process(target_name):
    # システム内のプロセスを確認するために`ps`コマンドを使用
    try:
        result = subprocess.check_output(['ps', '-A'], text=True)
        for line in result.splitlines():
            if target_name in line:
                # プロセスIDを抽出して終了
                pid = int(line.split(None, 1)[0])  # PIDは行の先頭にある
                os.kill(pid, signal.SIGTERM)
                print(f"Stopped process: PID {pid}, Line: {line}")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    # 停止させたいプロセス名（例: pythonスクリプト）
    target_process_name = "python"
    stop_process(target_process_name)
