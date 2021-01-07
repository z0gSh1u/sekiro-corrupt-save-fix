<p align="center">
  <img src="https://i.loli.net/2021/01/07/rbsZSOzmgyQkFVN.png"></img>
</p>
# 只狼坏档修复工具 / sekiro-corrupt-save-fix

**[简体中文](./README.md)**  |  **English**

Save corruption, usually happens after BSOD / Power Down. Even Sekiro cannot stop crying for tens of hours of game progress being vanished. But fortunately, you have **sekiro-corrupt-save-fix**!

This tool is written based on [this](https://www.reddit.com/r/Sekiro/comments/b5rkzx/fix_save_data_failed_sekiro_the_save_data_is/) discussion on Reddit, with a little correction. It re-calculates the checksum of your save, so that the game will recognize it again. Then, your recent game progress is recovered.

## How to use

### DISCLAIMER

- Although the tool will back up the save before it operates, but we cannot deny the possibility of failure because of permission issues, wrong logics or whatever else. So, we advise you backup your save well manually before you use this tool.
- The rate of success is never 100%. A corrupt save might still be corrupt. Or something worse, a good save becomes corrupt after using this tool. Think twice before you use it.
- According to MIT License of this tool, the author takes no responsibility for any consequence of using this tool.

### Two Basic Concepts

- **Sekiro Save Path** usually locates at `C:/Users/<Your username>/AppData/Roaming/Sekiro/<Your Steam ID>/S0000.sl2` .
- **Save Slot Index** is the position of corrupt save in LOAD GAME menu, zero-based. If you only play one save, just keep it to 0.

### Use .exe [The Most Simple Way]

- Download the lastest Release version of `scsf.exe` from [here](https://github.com/z0gSh1u/sekiro-corrupt-save-fix/releases). It looks like this:

  ![scsf_index](https://i.loli.net/2021/01/07/NULkCvxSDEQH15P.png)

- Open it, click button [Browse S0000.sl2], select Sekiro Save Path

- Select Save Slot Index to fix on the combobox

- Click button [Start fixing]. If everything is fine, there goes "Fixing done successfully!" message at the bottom

- The previous save will be backed up to S0000.sl2.fixbackup at the same directory of S0000.sl2

### Use Python Script

- Clone this repository

  ```
  git clone git@github.com:z0gSh1u/sekiro-corrupt-save-fix.git
  ```

- Run this if you need graphical user interface (GUI)

  ```
  cd tool
  python gui.py
  ```

- If you don't need GUI, just manage to execute `main` function inside`/tool/fix.py`

  ```python
  def main(sl2_path: str, slot_index: int): # sl2_path: Sekiro Save Path；slot_index: Save Slot Index
  ```

### Packup .exe Yourself

- Clone this repository

  ```
  git clone git@github.com:z0gSh1u/sekiro-corrupt-save-fix.git
  ```
  
- pyinstaller is required. Install it if you don't have one

  ```
  pip install pyinstaller
  ```

- Run the packup script

  ```
  build_exe.cmd
  ```

## Contribution Is Welcomed

This solution fixed my save at slot 0 after a BSOD successfully. Tests are not covered for other corruption situations (And I wish I won't get a chance to test 😅). If you found any problems, just [Raise an Issue](https://github.com/z0gSh1u/sekiro-corrupt-save-fix/issues) or [Make a PR](https://github.com/z0gSh1u/sekiro-corrupt-save-fix/pulls). I will try my best to optimize it.

<hr>
<p align="center">
  <b>Go, Sekiro ~</b>
</p>