import shutil, os

# vars
path = "output"

# delete output
shutil.rmtree(path)

# recreate output
os.makedirs(path,0755);

# copy test file
src = "input/index.html"
dst = "output"
shutil.copy2(src, dst)
