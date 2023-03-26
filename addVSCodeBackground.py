import re


def match(string: str) -> bool:
    return re.match('(.*?)\.(.*?)', string) != None


def run():
    add_string = input('请输入待加入背景列表的图片名称（包括后缀名）：')

    if not match(add_string):
        raise ValueError('文件名不规范！')
    else:
        with open('background.list', 'a', encoding='utf-8') as f:
            f.write(add_string + '\n')


if __name__ == '__main__':
    run()
