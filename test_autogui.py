import subprocess
import time
import pyautogui
from security import safe_command



safe_command.run(subprocess.Popen, 'study.exe')
time.sleep(10)

pyautogui.press('j')
