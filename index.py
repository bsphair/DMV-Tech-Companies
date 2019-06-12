import csv
import datetime

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

with open('companyList.csv') as csv_file:
    currentDate = datetime.datetime.now()
    date = str(months[currentDate.month - 1]) + " " + str(currentDate.day) + ", " + str(currentDate.year)

    mdFile = open("README.md", "w")

    mdFile.write("# DMV Tech Companies\n\n")
    mdFile.write("This is a list of tech companies in the DC-Maryland-Virginia (DMV) region. To make an update, please update the csv file and submit a pull request.\n\n")
    mdFile.write("Last updated: " + date + "\n\n")

    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            # print("Company\tCity, State\n")
            line_count = line_count + 1
            mdFile.write("| Company | City, State | Address | Website | Stack |\n")
            mdFile.write("| ------------ | ------------ | ------------ | ------------ | ------------ |\n")
        else:
            # print(row[0] + "\t" + row[1])
            mdFile.write("| " + row[0] + " | " + row[1] + " | " + row[2] + " | " + row[3] + " | " + row[4] + "|\n")

