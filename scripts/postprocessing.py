import os
import re
import sys

def parse_index_md(index_path):
    """
    解析 index.md 文件，提取 toctree 部分的内容并转换格式。

    :param index_path: index.md 文件路径
    :return: 转换后的内容
    """
    with open(index_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 匹配 toctree 格式
    pattern = r'::: \{#[^\s]+\.toctree\s+[^}]+\scaption="([^"]+)"\}\n((?:.|\n)*?)\n:::'
    matches = re.findall(pattern, content)

    summary_content = ""
    for caption, items in matches:
        summary_content += f"# {caption}\n\n"
        for item in items.split():
            title = os.path.basename(item).replace('.md', '')
            link = f"{item}.md"
            summary_content += f"- [{title.capitalize()}]({link})\n"
        summary_content += "\n"

    return summary_content

def postprocessing(src_dir):
    """
    通过解析 index.md 文件，生成 SUMMARY.md 目录文件；
    在指定文件夹中处理转化后的 .md 文件，并覆盖原文件。
    
    :param src_dir: 工作目录路径
    """
    # 确保目标目录存在
    if not os.path.exists(src_dir):
        print(f"目录 {src_dir} 不存在。")
        exit(1)

    index_path = os.path.join(src_dir, 'index.md')
    if not os.path.exists(index_path):
        print(f"文件 {index_path} 不存在。")
        exit(1)

    # 生成 SUMMARY.md 文件
    summary_content = parse_index_md(index_path)
    summary_path = os.path.join(src_dir, 'SUMMARY.md')
    with open(summary_path, 'w', encoding='utf-8') as file:
        file.write(summary_content)

    print(f"SUMMARY.md 已生成在 {summary_path}")

# 示例调用
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法：python postprocessing.py <目录路径>")
        sys.exit(1)
    
    src_dir = sys.argv[1]
    postprocessing(src_dir)