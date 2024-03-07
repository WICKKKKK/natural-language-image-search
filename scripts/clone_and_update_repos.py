import os
import subprocess

def clone_or_update_repo(repo_url, repo_dir):
    # 确保repositories目录存在
    if not os.path.exists(repo_dir):
        os.makedirs(repo_dir)

    repo_name = repo_url.split('/')[-1]
    if repo_name.endswith('.git'):
        repo_name = repo_name[:-4]

    repo_path = os.path.join(repo_dir, repo_name)

    # 克隆或更新仓库
    if os.path.isdir(repo_path):
        print(f"更新仓库: {repo_name}")
        subprocess.call(['git', 'pull'], cwd=repo_path)
    else:
        print(f"克隆仓库: {repo_name}")
        subprocess.call(['git', 'clone', repo_url, repo_path])

# 使用示例
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
repo_url = "https://github.com/WICKKKKK/CLIP.git"
clone_or_update_repo(repo_url, repo_dir=os.path.join(base_dir, 'repositories'))