import base64
import os
import sys
code = ""
try:
        file = raw_input ("[$] file: ")
        code = open(file,"r").read()
except IOERROR:
        print ("[$] file tidak di temukan")
        sys.exit()
rep = str(code).replace("<?php","").replace("?>","")
enc = base64.b64encode(rep)
data = """<?php
// Obfuscated by MASTER TERMUX INDONESIA
eval(base64_decode('%s'));
?>"""%(enc)
out = raw_input("[$] out: ")
open(out,"w").write(data)
print ("[$] berhasil di obfuscate")
