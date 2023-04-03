import os
import shutil
import subprocess

from huggingface_hub import HfApi, hf_hub_download, login, snapshot_download

# ここにAccess Tokenを記入
token = "hf_xxxxxxxxxxxxxxxxxxxxxxxxxxx"
repo_id = input("repo_id:")
filename = input("file or foldername:")
allow_patterns = filename + "/.*"

# DL先のディレクトリを指定
local_dir = "D:/f/Download/"
output_dir = local_dir + filename

# login(token=token,add_to_git_credential=True)



try:
    local_file_path = hf_hub_download(
        repo_id=repo_id,
        filename=filename,
        token=token
    )
    shutil.move(local_file_path, local_dir)
    subprocess.run(["explorer",local_dir.replace("/","\\")])
except Exception as e:
    print(e)
    os.makedirs(output_dir, exist_ok=True)

    api = HfApi()

    repo_info = api.repo_info(repo_id=repo_id,token=token,files_metadata=True)

    file_list = [file for file in repo_info.siblings if file.rfilename.startswith(filename)]

    # print(f"'{filename}'フォルダ内のファイル一覧:")
    for file in file_list:
        local_file_path = hf_hub_download(
            repo_id=repo_id,
            filename=file.rfilename,
            cache_dir=local_dir,
            token=token
        )
        # ダウンロードしたファイルを新しいディレクトリに移動
        shutil.move(local_file_path, output_dir, file.rfilename.replace("\\","/"))

    shutil.rmtree(local_dir + "models--" + repo_id.replace("/","--"))
    subprocess.run(["explorer",output_dir.replace("/","\\")])

