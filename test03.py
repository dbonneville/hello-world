import csv, shutil, os
from shutil import copyfile
from titlecase import titlecase
# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# vars
path = "output"
keyword = 'appliance-repair'

# delete output
shutil.rmtree(path)

# recreate output
os.makedirs(path,0755);

# copy assets
shutil.copytree('input/css','output/css')
shutil.copytree('input/js','output/js')

###

# load cities
with open('input/data/uscities2000.csv', 'rb') as file:
    reader = csv.reader(file)
    cityList = list(reader)

# get rid of header row
cityList.pop(0)

#load header
with open('input/html/header.html', 'r') as file :
  header = file.read()


# loop through cities, swap data and save pages to output folder
for row in cityList:

    # assign vars values
    city = row[1]
    state = row[2]
    zipcodes = row[4]
    authlink = 'https://en.wikipedia.org/wiki/' + city.replace(' ','_') + ',_' + state.replace(' ','_')

    # get the page template
    with open('input/templates/city.html', 'r') as file :
      cityTemplate = file.read()

    # Replace the target string
    cityTemplate = cityTemplate.replace('##CITY##', city)
    cityTemplate = cityTemplate.replace('##STATE##', state)
    cityTemplate = cityTemplate.replace('##ZIPCODES##', zipcodes)
    cityTemplate = cityTemplate.replace('##AUTHLINK##', authlink)

    # insert header
    cityTemplate = cityTemplate.replace('##HEADER##', header)

    # remove spaces for use in file URI
    city = city.replace(' ','-')

    # save unique city file to output folder
    with open('output/' + city.lower() + '-' + keyword + '.html', 'w') as file:
      file.write(cityTemplate)


######################
### HOMEPAGE START ###
######################

# city list for homepage
cityListOutput = '<ul>'

# get the index page
with open('input/index.html', 'r') as file :
  template = file.read()

# insert header
template = template.replace('##HEADER##', header)

for row in cityList:

    # assign vars values
    city = row[0]
    state = row[3]
    cityLower = city.replace(' ','-').lower()

    keywordLink = titlecase(keyword)
    keywordLink = keywordLink.replace('-',' ')

    cityListOutput += '<li><a href="'+ cityLower + '-' + keyword + '.html">' + city + ' ' + state + ' ' + keywordLink + '</a></li>'

# close off city list
cityListOutput += '</ul>'

# Replace the target string
template = template.replace('##CITYLIST##', cityListOutput)



### states start
# empty list
stateOutput = []

# load list of states
with open('input/data/uscities2000.csv', 'rb') as file:
    reader = csv.reader(file)
    stateList = list(reader)

# loop over data and shove states into our list
for row in stateList:
    state = row[3]
    stateOutput.append([state])

# function to remove duplicate elements from our list
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

# run function
stateOutput = Remove(stateOutput)

# remove header row from list
stateOutput.pop(0)

# loop through list and create HTML snippet
stateListHTML = ''

for row in stateOutput:

    keywordLink = titlecase(keyword)
    keywordLink = keywordLink.replace('-',' ')

    state = row[0].lower()

    # remove spaces for use in file URI
    state = state.replace(' ','-')

    stateListHTML += '<a href="' + state.lower() + '-' +keyword + '.html">' + row[0] + ' ' + keywordLink + '</a>'

print stateListHTML;

# Replace the target string
template = template.replace('##STATELIST##', stateListHTML)


### states end



### WRITE ###
# save new index to output folder
with open('output/index.html', 'w') as file:
  file.write(template)

######################
### HOMEPAGE END   ###
######################





print 'done'
