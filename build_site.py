import shutil, os
'''
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
'''

import jinja2

from jinja2 import Template
t = Template("Hello {{ something }}!")
t.render(something="World")

t = Template("My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
t.render()

import csv
with open('input/data/cities.csv', 'rb') as f:
    reader = csv.reader(f)
    cities = list(reader)

print cities

'''
from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader('file/path/'),
    autoescape=select_autoescape(['html', 'xml']),
)
'''
