import subprocess
import sys

try:
    import compas_rrc
    print('COMPAS RRC is available')
except ImportError:
    subprocess.call([sys.executable,  '-m', 'pip', 'install', 'compas_rrc'])
    print('COMPAS RRC has been installed')
