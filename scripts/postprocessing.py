import os
import re
import sys

def get_title(src_dir, file_path):
    """
    从 Markdown 文件中提取标题。

    :param src_dir: 工作目录路径
    :param file_path: Markdown 文件路径
    :return: 标题字符串
    """
    with open(src_dir + file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 匹配标题
    match = re.search(r'^# (.+?)(?: \{#.*\})?$', content, re.MULTILINE)
    if match:
        return match.group(1)
    else:
        return os.path.basename(file_path).replace('.md', '')

def parse_index_md(src_dir, root = '1'):
    """
    解析工作目录路径下的 index.md 文件，提取 toctree 部分的内容并转换格式，
    覆盖原内容，并返回转换后的内容。

    :param src_dir: 工作目录路径
    :param root: '1' 表示当前处理的是根目录，其它值表示当前处理的非根目录
    :return: 转换后的内容
    """
    # 检查根目录下的 index.md
    index_path = os.path.join(src_dir, 'index.md')
    if not os.path.exists(index_path):
        print(f"文件 {index_path} 不存在。")
        exit(1)

    # 读取根目录下的 index.md
    with open(index_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 匹配 toctree 格式
    pattern1 = re.compile(r'::: \{#.*?\.toctree.*?caption="(.*?)"\}(.*?):::', re.DOTALL)
    pattern2 = re.compile(r'::: \{#.*?\.toctree.*?\}(.*?):::', re.DOTALL)

    # 格式化 item
    def format_item(item):
        if item.endswith(".rst"):
            item = item[:-4]
        if item.startswith("[class]()"):
            item = item.replace("[class]()", "class_")
        return item

    # 匹配非 toctree 的内容格式化后生成 SUMMARY.md
    if root == '1':
        matches = pattern1.findall(content)
    else:
        matches = pattern2.findall(content)
    summary_content = ""
    if root == '1':
        for caption, items in matches:
            summary_content += f"# {caption}\n\n"
            for item in items.split():
                item = format_item(item)
                title = get_title(src_dir, f"{item}.md")
                link = f"{item}.md"
                summary_content += f"- [{title.capitalize()}]({link})\n"
                if item.endswith("index"):
                    summary_content += parse_index_md(src_dir + item[:-5], src_dir)
                item = f"- [{title.capitalize()}]({link})\n"
    else:
        for items in matches:
            for item in items.split():
                item = format_item(item)
                title = get_title(src_dir, f"{item}.md")
                link = f"{src_dir.removeprefix(root)}{item}.md"
                summary_content += f"  - [{title.capitalize()}]({link})\n"
                if item.endswith("index"):
                    summary_content += parse_index_md(src_dir + item[:-5], root)
                item = f"- [{title.capitalize()}]({item}.md)\n"

    # 将原本 toctree 的地方替换成 - []()
    new_content = ""
    with open(index_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
        print(f"已修改 {src_dir}index.md")

    return summary_content

def postprocessing(src_dir):
    """
    通过解析 index.md 文件，生成 SUMMARY.md 目录文件；
    在指定文件夹中处理转化后的 .md 文件，并覆盖原文件。
    
    :param src_dir: 工作目录路径
    """
    # 检查 src_dir 是否为 / 结尾的路径
    if not src_dir.endswith('/'):
        print(f"{src_dir} 应以 / 结尾。")
        exit(1)

    # 确保目标目录存在
    if not os.path.exists(src_dir):
        print(f"目录 {src_dir} 不存在。")
        exit(1)

    # 生成 SUMMARY.md 文件
    summary_content = parse_index_md(src_dir)
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