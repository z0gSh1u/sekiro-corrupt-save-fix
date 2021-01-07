<p align="center">
  <img src="https://i.loli.net/2021/01/07/rbsZSOzmgyQkFVN.png"></img>
</p>

# 只狼坏档修复工具 / sekiro-corrupt-save-fix

**简体中文**  |  **[English](./README-EN.md)**

坏档，往往发生在蓝屏 / 断电之后。数十小时游戏进度的消失，连狼也忍不住流出眼泪。幸好，你还有 **只狼坏档修复工具**！

本工具根据 Reddit 上的 [这篇](https://www.reddit.com/r/Sekiro/comments/b5rkzx/fix_save_data_failed_sekiro_the_save_data_is/) 讨论，经修正后编写而成。它能够修正存档的校验和，使游戏再次认可存档的有效性，找回你最近的游戏进度。

## 如何使用

### 丑话说在前头

- 尽管工具本身会对存档进行备份后再操作，但不排除因为权限原因、逻辑错误或是其他等等情况造成备份失败。因此，建议您先手动将现有存档备份稳妥后，再使用本工具操作。
- 工具修复的成功率从不保证是 100%。坏档修不好、好档修坏的可能性都有，请自行斟酌后再使用。
- 根据本开源工具的 MIT License，作者对使用该工具产生的一系列后果都不负责。

### 两个基本概念

- **只狼存档位置** 通常在 `C:/Users/<你的用户名>/AppData/Roaming/Sekiro/<你的Steam ID>/S0000.sl2`。
- **存档槽编号** 指的是要修复的存档在 LOAD GAME 菜单的位置，**从 0 开始数**。如果你只有一个档，保持 0 就可以了。

### 使用 .exe [最简单的方式]

- 在 [这里](https://github.com/z0gSh1u/sekiro-corrupt-save-fix/releases) 下载最新的 Release 版修复工具 `scsf.exe`，它长这样：

  ![scsf_index](https://i.loli.net/2021/01/07/NULkCvxSDEQH15P.png)

- 打开该工具，点击 [Browse S0000.sl2] 按钮，选择只狼存档位置

- 在下拉框内选择要修复的存档槽编号

- 点击 [Start fixing] 按钮，如果正确无误，下方会出现 "Fixing done successfully!" 提示

- 先前的存档会被备份为 S0000.sl2 同目录下的 S0000.sl2.fixbackup 文件

### 使用 Python 脚本

- 克隆本仓库

  ```
  git clone git@github.com:z0gSh1u/sekiro-corrupt-save-fix.git
  ```

- 如果需要图形界面，执行

  ```
  cd tool
  python gui.py
  ```

- 如果不需要图形界面，设法执行 `/tool/fix.py` 中的 `main` 函数即可

  ```python
  def main(sl2_path: str, slot_index: int): # sl2_path: 只狼存档路径；slot_index: 存档槽编号
  ```

### 使用自己打包的 .exe

- 克隆本仓库

  ```
  git clone git@github.com:z0gSh1u/sekiro-corrupt-save-fix.git
  ```
  
- 需要 pyinstaller 工具进行打包，如果没有，则安装之

  ```
  pip install pyinstaller
  ```

- 执行打包脚本

  ```
  build_exe.cmd
  ```

## 欢迎贡献

这个方法在一次蓝屏后成功修复了我位于 0 号存档槽的存档，对于其它坏档情况并没有充分测试（也希望没有机会测试 😅）。如果你发现这个工具有什么问题，欢迎 [提出 Issue](https://github.com/z0gSh1u/sekiro-corrupt-save-fix/issues) 或者 [发起 PR](https://github.com/z0gSh1u/sekiro-corrupt-save-fix/pulls)，我会尽力完善它的！

<hr>
<p align="center">
  <b>要上了，只狼 ~</b>
</p>