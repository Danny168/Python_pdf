#!C:\Users\Danny.Tjahjadi\source\repos\Python_pdf\Python_pdf\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'tika==1.23','console_scripts','tika-python'
__requires__ = 'tika==1.23'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('tika==1.23', 'console_scripts', 'tika-python')()
    )
