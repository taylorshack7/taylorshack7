# Name:           Taylor Shackelford
# Date:           D15/ 11/ 2019
import csv


# creates new file for tsv format:  # opens/ creates same file but in csv format
def file():
    with open('WeatherDataWindows.csv', "r") as c, open(name_of_file + '.tsv', "w+") as t:  # open csv as r and new
        # file as w
        cu = csv.reader(c)  # read that thang
        for row in cu:  # iterate through contents
            t.write('\t'.join(row))  # write contents of csv into tsv
            t.write('\n')  # new line gang


name_of_file = input('What is the name of the file you want to convert from csv to tsv? ')  # get name of file
file()  # this program works, simply open the file for proof
print("Done. Open file name you inputted for tsv conversion")
