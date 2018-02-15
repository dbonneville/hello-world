import csv

# vars
keyword = 'appliance-repair'

# load cities
with open('input/data/cities.csv', 'rb') as file:
    reader = csv.reader(file)
    cityList = list(reader)

# get rid of header row
cityList.pop(0)

# TEST
for row in cityList:
    print row[0] + ' ' + row[1]


# get the page template
with open('input/templates/city.html', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('##CITY##', 'Boston')
filedata = filedata.replace('##ONE##', 'Chocolate')
filedata = filedata.replace('##TWO##', 'Vanilla')
filedata = filedata.replace('##THREE##', 'Cat')

# Write the file out again
with open('output/done.html', 'w') as file:
  file.write(filedata)

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
      file.write(filedata)
