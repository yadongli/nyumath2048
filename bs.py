import os
import subprocess
import shutil
import sys
import time

def convert(nb, tpl, remote) :
    nb_tpl = './%s.tpl' % nb
    if os.path.isfile(nb_tpl) : #if customized template exists, uses it
        tpl = nb_tpl

    cmd = 'ipython nbconvert --to slides --template %s ' % tpl
    if (remote) :
        cmd += '--reveal-prefix "//cdn.jsdelivr.net/reveal.js/2.6.2" '

    cmd += "%s.ipynb" % nb
    print cmd
    subprocess.call(cmd, shell=True)

def convertAllNb(tpl, remote) :
    return [convert(os.path.splitext(os.path.basename(f))[0], tpl, remote) 
            for f in os.listdir(".") if f.endswith(".ipynb")]

def convertNewNb(tpl, remote) :
    for f in os.listdir(".") :
        if f.endswith(".ipynb") :
            nbt = os.path.getmtime(f)
            htmlf = "../gh-pages/" + f.replace(".ipynb", ".slides.html")
            hashtml = os.path.isfile(htmlf)
            if (not hashtml) or os.path.getmtime(htmlf) < nbt :
                convert(os.path.splitext(os.path.basename(f))[0], tpl, remote)


def convert2PDF(nb, tpl) :    
    nb_tpl = './%s.tplx' % nb
    if os.path.isfile(nb_tpl) : #if customized template exists, uses it
        tpl = nb_tpl

    cmd = 'ipython nbconvert --to latex --post pdf --ExecutePreprocessor.enabled=True --template %s %s.ipynb' % (tpl, nb)
    print cmd
    subprocess.call(cmd, shell=True)

def convertAll2PDF() :
    [convert2PDF(os.path.splitext(os.path.basename(f))[0], "hidecode.tplx") 
            for f in os.listdir(".") if f.endswith(".ipynb")]
    [shutil.copy2(f, '../gh-pages') for f in os.listdir(".") if f.endswith(".pdf")]

if __name__ == "__main__" :
    if len(sys.argv) > 1 :
        convert(sys.argv[1], 'hidecode.tpl', True)
    else: # convert all if nothing is supplied
        convertNewNb("hidecode.tpl", True)

    [shutil.copy(f, '../gh-pages') for f in os.listdir(".") if f.endswith(".html")]
    [os.remove(f) for f in os.listdir(".") if f.endswith(".html")]
