#importing libraries 
import os, math, sys


# installing dependencies for firefox

os.system("sudo apt-get install python-pip && sudo apt-get install tor")   
os.system("pip install -U selenium")
os.system("pip install Pysocks")
os.system("pip install pyvirtualdisplay && apt-get install xvfb")


#printing the core values of the OS

os.system('firefox -v > tmp')                  # storing the result of firefox in -v along tmp
result   =  open('tmp', 'r').read()            # results in variables reads the output of the OS
marker   = result.find('Firefox') + 8          # 8th letter marks the marks from the word "Firefox"
version  = result[marker:].splitlines()[0]     # spliting the output, the version is something like aa.bb.cc
a,b,c = version.split(".")                     # a is the var with the aa
os.remove('tmp')                               # deleting temp files for data optimization

FirefoxVersion = int(a)
second = 0

# adding conditional formating
if FirefoxVersion  < 53:

    first = 16
    second = 1
    OS_bit = 64

elif FirefoxVersion == 53 or FirefoxVersion == 54:

    first = 18

elif FirefoxVersion > 54:

    first = 19

# fetching drivers for the new prev release of geckodrivers
os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.{}.{}/geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,first,second,OS_bit))
os.system("tar -xvzf geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,OS_bit))
os.system("rm geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,OS_bit))
os.system("chmod +x geckodriver")
os.system("mv geckodriver /usr/local/bin/")
os.system("chmod +x faitagram && chmod +x setup.py")
