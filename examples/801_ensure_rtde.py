import subprocess
import sys

try:
    import rtde_receive
    print('UR RTDE is available')
except ImportError:
    subprocess.call([sys.executable,  '-m', 'pip', 'install', 'ur-rtde'])
    print('UR RTDE has been installed')
