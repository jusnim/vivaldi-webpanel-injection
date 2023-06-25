import os
import shutil
from sys import platform
from sys import argv

# change prepath, thats depends on your OS
if platform == "linux" or platform == "linux2":
    prepath = "/opt/"
elif platform == "darwin":
    prepath = "/Applications/Vivaldi.app/Contents/MacOS/"
elif platform == "win32":
    prepath = os.path.abspath(os.getenv("APPDATA") + "/../Local/");

# find out version number
pathPart1="/Vivaldi/Application/"
version = list(os.walk(prepath + pathPart1, topdown=True))[0][1][0]
pathPart2 = "/resources/vivaldi/"

path= prepath + pathPart1 + version + pathPart2

string = 'this.refWebpanelwebview.current?.executeScript({file:"inject-all-bundle.js"})'
string2 = 'this.refWebpanelwebview.current?.executeScript({file:"webpanel.js"}), this.refWebpanelwebview.current?.executeScript({file:"inject-all-bundle.js"})'

with open(path + "bundle.js", "r", encoding='utf-8') as f:
    content = f.read(-1)

if not "webpanel.js" in content:
    content = content.replace(string, string2)
    with open(path + "bundle.js", "w", encoding='utf-8') as f:
        f.write(content);

shutil.copyfile(argv[1], path + "webpanel.js")