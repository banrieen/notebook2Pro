import os,sys
import subprocess
GITBRANCH = "Algorithms"
pathName = os.path.dirname(__file__)
print(f"{pathName}")
print("Hi, I`m ok!")
print(__file__)
print(os.path.realpath(__file__))
print(os.path.dirname(os.path.realpath(__file__)))
print(os.getcwd())
BookDir = os.path.dirname(os.path.realpath(__file__))
outs = subprocess.Popen(f"cd {BookDir} && git status", stdout=subprocess.PIPE, shell=True)
commit_des = outs.communicate()
commit_des = commit_des[0].decode('UTF-8').split("\n")[4:]
commit_des = ",".join([des.replace("\t","") for des in commit_des if des.strip()])
subprocess.call(f"cd {BookDir} && git add --all", shell=True)
subprocess.call(f"cd {BookDir} && git commit -m '{commit_des}'", shell=True)
# commit_des = commit_des[0].decode('UTF-8')
subprocess.call(f"cd {BookDir} && git pull origin  {GITBRANCH}", shell=True)
subprocess.call(f"cd {BookDir} && git push origin {GITBRANCH}", shell=True)
print(f"commit_des: {commit_des}")
