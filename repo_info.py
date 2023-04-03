import subprocess as subp

from huggingface_hub import HfApi, login

repo_id = input("Paste Repo:")

# ここにAccess Tokenを記入
token = "hf_xxxxxxxxxxxxxxxxxxxxxxxxxxx"
log = "model_info.log"

api = HfApi()

repo_info = api.repo_info(repo_id=repo_id,token=token,files_metadata=True)
files_info = repo_info.siblings

with open(log, "w", encoding="utf-8") as f:
    # ファイル名とサイズを追記
    for file_info in files_info:
        f.write(str(file_info) + "\n")

subp.run([r"notepad.exe",log])
exit()