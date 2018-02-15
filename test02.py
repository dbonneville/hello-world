import csv
from shutil import copyfile
from titlecase import titlecase

# vars
keyword = 'appliance-repair'

# load cities
with open('input/data/cities.csv', 'rb') as file:
    reader = csv.reader(file)
    cityList = list(reader)

# get rid of header row
cityList.pop(0)
'''
# TEST
for row in cityList:
    print row[0] + ' ' + row[1]
'''
# loop through cities, swap data and save pages to output folder
for row in cityList:

    # assign vars values
    city = row[0]
    state = row[1]
    zipcode = row[3]
    animal = row[2]

    # get the page template
    with open('input/templates/city.html', 'r') as file :
      cityTemplate = file.read()

    # Replace the target string
    cityTemplate = cityTemplate.replace('##CITY##', city)
    cityTemplate = cityTemplate.replace('##STATE##', state)
    cityTemplate = cityTemplate.replace('##ZIPCODE##', zipcode)
    cityTemplate = cityTemplate.replace('##ANIMAL##', animal)

    # remove spaces for use in file URI
    city = city.replace(' ','-')

    # save unique city file to output folder
    with open('output/' + city.lower() + '-' + keyword + '.html', 'w') as file:
      file.write(cityTemplate)


# city list for homepage
cityListOutput = '<ul>'

# get the index page
with open('input/index.html', 'r') as file :
  template = file.read()

for row in cityList:

    # assign vars values
    city = row[0]
    state = row[1]
    cityLower = city.replace(' ','-').lower()

    keywordLink = titlecase(keyword)
    keywordLink = keywordLink.replace('-',' ')

    cityListOutput += '<li><a href="'+ cityLower + '-' + keyword + '.html">' + city + ' ' + state + ' ' + keywordLink + '</a></li>'

# close off city list
cityListOutput += '</ul>'


# Replace the target string
template = template.replace('##CITYLIST##', cityListOutput)

# save new index to output folder
with open('output/index.html', 'w') as file:
  file.write(template)








print 'done'
