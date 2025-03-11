#%%
# from  pybind11.build import Cat
import sys
sys.path.append("/home/Docker/pybind/build") # build ディレクトリのパス

from mycat import Cat

cat = Cat("Shiro")
cat.say()   # output "Shiro said meow."
