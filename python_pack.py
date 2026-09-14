import time
import os
welcome='''\
                *           *   *************   *************   *************
                *           *   *           *   *           *   *           
                *           *   *           *   *           *   *           
                *           *   *           *   *           *   *           
                *************   *           *   *************   *************
                *           *   *           *   *               *
                *           *   *           *   *               *
                *           *   *           *   *               *
                *           *   *************   *               *************
'''
def inerror(s)->None:#输入异常提示函数
    print(s)
    time.sleep(3)
    os.system('cls')

print(welcome+'\a')#开屏动画
time.sleep(3)
os.system('cls')

while True:#主循环
    try:
        pro_addr=input('输入要打包的脚本地址：')
        pro_addr=pro_addr.strip('"')
        if pro_addr[-3:]!='.py':#检查文件格式
            inerror('提供的脚本文件不是.py!')
            continue
        pack_set = 'F'#独立exe文件
        cli_set = 'w'#隐藏黑窗
        name_set = 'k'#命名
        name=''
        print('''\
        选择打包样式：
        1>打包成独立.exe文件
        2>打包成一个运行文件夹
        ''')
        user_in=input('输入选择：')
        if user_in=='2':
            pack_set='D'
        elif user_in!='1':
            inerror('输入错误！')
            continue
        print('''\
        选择是否隐藏黑窗：
        1>是
        2>否
        ''')
        user_in = input('输入选择：')
        if user_in=='2':
            cli_set='c'
        elif user_in != '1':
            inerror('输入错误')
            continue
        print('''\
        选择是否命名：
        1>是
        2>否
        ''')
        user_in = input('输入选择：')
        if user_in == '1':
            name_set = 'n'
            name=input('输入名称:')
        elif user_in != '2':
            inerror('输入错误！')
            continue
        script_folder = os.path.dirname(pro_addr)#拿到待打包脚本的目录
        os.chdir(script_folder)#切换工作目录到该文件夹
        if name_set == 'k':
            os.system(f'python -m PyInstaller -{pack_set} -{cli_set} {pro_addr}\n')
        elif name_set == 'n':
            os.system(f'python -m PyInstaller -{pack_set} -{cli_set} -{name_set} {name} {pro_addr}\n')
        user_in=input('是否继续？（Y/N）')
        if user_in=='Y':
            os.system('cls')
        else:
            break
    except:
        print('输入异常！！！')
        time.sleep(3)
        os.system('cls')