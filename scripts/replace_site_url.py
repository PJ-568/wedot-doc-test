import subprocess
import sys

def get_current_branch():
    """获取当前 Git 分支名称"""
    try:
        result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"获取当前分支名称时出错：{e}")
        sys.exit(1)

def replace_site_url(file_path, branch_name):
    """替换文件中的 {site.url} 为当前分支名称"""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        new_content = content.replace('{site.url}', branch_name)
        
        with open(file_path, 'w') as file:
            file.write(new_content)
        
        print(f"Replaced {site.url} with {branch_name} in {file_path}")
    except Exception as e:
        print(f"替换 site url 时出错：{e}")
        sys.exit(1)

if __name__ == "__main__":
    """
    将指定文件中的 {site.url} 替换为当前分支名称。
    """
    if len(sys.argv) != 2:
        print("使用方法：python replace_site_url.py <文件>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    branch_name = get_current_branch()
    replace_site_url(file_path, branch_name)