# python_pack —— PyInstaller 交互式打包助手

把 `.py` 脚本一键打包成 exe 的小工具：用菜单选择“单文件/文件夹”“是否隐藏黑窗”“是否自定义名称”，自动拼出 PyInstaller 命令并执行。

## 功能

程序是一个循环菜单，每轮处理一个脚本：

1. 输入要打包的脚本路径（支持带双引号的粘贴路径，自动去引号；非 `.py` 会拒绝）
2. 选择打包样式：
   - `1` 打包成独立 `.exe` 文件 → PyInstaller `-F`
   - `2` 打包成一个运行文件夹 → PyInstaller `-D`
3. 选择是否隐藏黑窗：
   - `1` 是 → `-w`（不显示控制台窗口，适合 GUI 程序）
   - `2` 否 → `-c`（保留控制台窗口，适合命令行程序）
4. 选择是否命名：
   - `1` 是 → 额外加 `-n <名称>`
   - `2` 否 → 用脚本文件名作为 exe 名
5. 自动切换到脚本所在目录并调用 PyInstaller，完成后询问是否继续（`Y` 继续）

## 生成的命令

| 选择 | 实际执行的命令 |
| --- | --- |
| 独立 exe + 隐藏黑窗 + 不命名 | `python -m PyInstaller -F -w <脚本路径>` |
| 文件夹 + 显示黑窗 + 命名 | `python -m PyInstaller -D -c -n <名称> <脚本路径>` |

打包产物默认输出到脚本所在目录的 `dist/` 文件夹，中间文件在 `build/`，同时会生成 `<脚本名>.spec`。

## 运行环境

- Windows + Python 3.13
- **需要额外安装 PyInstaller**（本项目的 `.venv` 中目前只有 `pip`，尚未安装）：

  ```powershell
  pip install pyinstaller
  ```

  安装后确认可用：

  ```powershell
  python -m PyInstaller --version
  ```

- 脚本自身只依赖标准库 `time` / `os`，没有其他第三方依赖。

## 使用方法

```powershell
python python_pack.py
```

示例交互：

```
输入要打包的脚本地址："E:\PyCharm_project\python_pack\python_pack.py"
选择打包样式：
1>打包成独立.exe文件
2>打包成一个运行文件夹
输入选择：1
选择是否隐藏黑窗：
1>是
2>否
输入选择：1
选择是否命名：
1>是
2>否
输入选择：1
输入名称:my_tool
```

## 已知问题 / 注意事项

- **需要 Python 环境中已装 PyInstaller**：脚本调用的是 `python -m PyInstaller`，用的是当前环境的 `python`；若 PyCharm 的虚拟环境没装 PyInstaller，会报 `No module named PyInstaller`。
- **建议使用绝对路径**：程序先取 `os.path.dirname(脚本路径)` 再 `os.chdir` 过去，因此输入**相对路径**时会因目录切换而找不到脚本；请始终粘贴完整路径。
- **自定义名称不要带空格**：`-n {name}` 未加引号，名称中含空格会被 PyInstaller 解析成多个参数。
- **打包时不要占用 dist 目录**：如果上一次生成的 exe 正在运行，PyInstaller 无法覆盖它，会写入失败，需要先关闭该程序。
- 输入校验失败时进入 `inerror()`：打印提示 → 延时 3 秒 → 清屏 → 重新开始本轮。
- 外层用了 `except:` 兜底，任何异常都会被显示为 `输入异常！！！`，不利于定位真实错误；排查问题时建议单独在命令行手动执行 PyInstaller 命令看完整报错。
- 清屏用 `os.system('cls')`，仅在 Windows 上有效。

## 目录结构

```
python_pack/
├── python_pack.py        # 主程序：交互式 PyInstaller 打包助手
├── README.md
├── .venv/                # 虚拟环境（目前仅 pip，打包前请装 pyinstaller）
└── .idea/                # PyCharm 工程配置
```

## 仓库

- GitHub：<https://github.com/Bulehopejiang/python_pack.git>
- 分支：`master`
- 最近提交：`4f0de84` 代码提交
