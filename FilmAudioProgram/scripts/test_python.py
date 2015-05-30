import subprocess
import os

os.chmod('/Users/Mitali/Desktop/test_script.sh', 0o755)
subprocess.call("/Users/Mitali/Desktop/test_script.sh")
