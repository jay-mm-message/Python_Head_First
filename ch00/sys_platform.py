# 使用 sys 提供的 platform 回傳目前系統平台

import sys
import os

current_system = sys.platform
print("Current system: ", current_system)
print("System version: ", sys.version)
#print("os environ: ", os.environ)
print("os getenv('HOME'): ", os.getenv('HOME'))
