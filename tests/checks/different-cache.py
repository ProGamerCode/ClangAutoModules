#!/usr/bin/env python

import sys
from shutil import copyfile
from subprocess import call
import os

exit_code = 0
exit_code += call(["rm", "-rf", sys.argv[3]])
exit_code += call(["cp", "-r", sys.argv[2], sys.argv[3]])
copyfile(sys.argv[1] + "/ClangModules.cmake",
         sys.argv[3] + "/ClangModules.cmake")
os.chdir(sys.argv[3])
exit_code += call(["mkdir", "build"])
os.chdir("build")
exit_code += call(["cmake", ".."])
exit_code += call(["make"])

if exit_code != 0:
    print("One of the commands had non-zero exit code!")
    exit(1)

if os.path.isfile("HasClang"):
    if not os.path.isdir("MyCache"):
        print("Couldn't find 'MyCache' custom PCM cache")
        exit(2)

