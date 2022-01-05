import os
import shutil
import PyInstaller.__main__

# Get the current PJP version
version = ""
version_ini = open("../library/version.ini", "r")
for line in version_ini.readlines():
    if line.startswith("installed version"):
        version = line.replace("installed version: ", "").rstrip()
version_ini.close()

# Package into .exe and create installer, without templates
PyInstaller.__main__.run(["../packer.py", "--onefile", "--windowed",
    "--icon=../library/packer images/icon.ico", "--name=Paint Job Packer",
    "--add-data=../library:library"])

if (sys.platform == "darwin"):
    shutil.make_archive("paint-job-packer-v{}-mac".format(version), "zip", "dist")
else:
    shutil.make_archive("paint-job-packer-v{}-linux".format(version), "zip", "dist")
shutil.rmtree("build")
shutil.rmtree("dist")
os.remove("Paint Job Packer.spec")