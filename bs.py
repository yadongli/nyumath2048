import os
import subprocess
import shutil
import sys
import time

reveal = ' --reveal-prefix="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/" '


def convert(nb, tpl) :
    nb_tpl = './%s.tpl' % nb
    if os.path.isfile(nb_tpl) : #if customized template exists, uses it
        tpl = nb_tpl

    cmd = 'jupyter nbconvert --to slides --template ' + tpl + reveal
    cmd += "{:s}.ipynb".format(nb)
    print(cmd)
    subprocess.call(cmd, shell=True)

def convertAllNb(tpl) :
    return [convert(os.path.splitext(os.path.basename(f))[0], tpl) 
            for f in os.listdir(".") if f.endswith(".ipynb")]

def convertNewNb(tpl) :
    for f in os.listdir(".") :
        if f.endswith(".ipynb") :
            nbt = os.path.getmtime(f)
            htmlf = f.replace(".ipynb", ".slides.html")
            hashtml = os.path.isfile(htmlf)
            if (not hashtml) or os.path.getmtime(htmlf) < nbt :
                convert(os.path.splitext(os.path.basename(f))[0], tpl)

if __name__ == "__main__" :
    if len(sys.argv) > 1 :
        convert(sys.argv[1], 'hidecode.tpl')
    else: # convert all if nothing is supplied
        convertNewNb("hidecode.tpl")

    [shutil.copy(f, '../gh-pages') for f in os.listdir(".") if f.endswith(".html")]
