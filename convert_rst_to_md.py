import os
import shutil
import subprocess

def convert_rst_to_md(src_dir, dest_dir):
    """
    将源目录中的所有 .rst 文件转换为 .md 文件，并保存到目标目录中，保持原有的目录结构。
    
    :param src_dir: 源目录路径
    :param dest_dir: 目标目录路径
    """
    # 确保目标目录存在
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # 遍历源目录及其子目录
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.rst'):
                # 构建完整的文件路径
                src_file_path = os.path.join(root, file)
                # 计算相对于源目录的相对路径
                rel_path = os.path.relpath(root, src_dir)
                # 构建目标目录路径
                dest_subdir = os.path.join(dest_dir, rel_path)
                # 确保目标子目录存在
                if not os.path.exists(dest_subdir):
                    os.makedirs(dest_subdir)
                # 构建目标文件路径
                dest_file_path = os.path.join(dest_subdir, file[:-4] + '.md')
                # 使用 pandoc 转换文件
                subprocess.run(['pandoc', src_file_path, '-f', 'rst', '-t', 'markdown_strict', '-o', dest_file_path], check=True)
                print(f"已把 {src_file_path} 转换到 {dest_file_path}")

# 示例调用
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("使用方法：python convert_rst_to_md.py <源目录路径> <目标目录路径>")
        sys.exit(1)
    
    src_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    convert_rst_to_md(src_dir, dest_dir)