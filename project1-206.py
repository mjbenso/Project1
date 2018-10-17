import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows

	infile = open(file, 'r')

	lines = infile.readlines()[1:]
	infile.close()

	dictList = []

	for line in lines:
		line = line.rstrip()

		columns = line.split(",")
		first = columns[0]
		last = columns[1]
		email = columns[2]
		uclass = columns[3]
		dob = columns[4]
		rowDict = {"First":first, "Last":last, "Email":email, "Class":uclass, "DOB":dob}
		dictList.append(rowDict)
	
	return dictList


def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

	for i in range(len(data)):
		for j in range(0, len(data)-1-i):
			if data[j][col] >= data[j+1][col]:
				data[j], data[j+1] = data[j+1], data[j]

			
	word = str(data[0]["First"] + " " + data[0]["Last"])
	return word



def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	senior_count = 0
	junior_count = 0
	soph_count = 0
	fresh_count = 0

	for i in data:
		if i["Class"] == "Senior":
			senior_count += 1
		
		elif i["Class"] == "Junior":
			junior_count += 1

		elif i["Class"] == "Sophomore":
			soph_count += 1

		elif i["Class"] == "Freshman":
			fresh_count += 1

	sen_tup = ("Senior", senior_count)
	jun_tup = ("Junior", junior_count)
	soph_tup = ("Sophomore", soph_count)
	fresh_tup = ("Freshman", fresh_count)

	hist_list = [sen_tup, jun_tup, soph_tup, fresh_tup]

	for i in range(4):
		for j in range(0, 3-i):
			if hist_list[j][1] < hist_list[j+1][1]:
				hist_list[j], hist_list[j+1] = hist_list[j+1], hist_list[j]

	return hist_list


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
	jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

	for i in a:
		date = i["DOB"].split("/")

		if date[0] == "1":
			jan += 1

		elif date[0] == "2":
			feb += 1

		elif date[0] == "3":
			mar += 1

		elif date[0] == "4":
			apr += 1

		elif date[0] == "5":
			may += 1

		elif date[0] == "6":
			jun += 1

		elif date[0] == "7":
			jul += 1

		elif date[0] == "8":
			aug += 1

		elif date[0] == "9":
			sep += 1

		elif date[0] == "10":
			oct += 1

		elif date[0] == "11":
			nov += 1

		elif date[0] == "12":
			dec += 1

	months = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
	max = 0
	index = 12
	for i in range(len(months)):
		if months[i] > max:
			max = months[i]
			index = i

	return index+1

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	for i in range(len(a)):
		for j in range(0, len(a)-1-i):
			if a[j][col] >= a[j+1][col]:
				a[j], a[j+1] = a[j+1], a[j]

	file = open(fileName, "w")
	
	for i in a:
		file.write(i["First"] + "," + i["Last"] + "," + i["Email"] + "\n")
	

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	today = date.today()
	avgAge = relativedelta()

	for i in a:
		birthTup = i["DOB"].split("/")
		dob = int(birthTup[1])
		mob = int(birthTup[0])
		yob = int(birthTup[2])
		birthDate = date(yob, mob, dob)
		avgAge += relativedelta(today, birthDate)
	
	avgAge = avgAge / len(a)
	yearAge = avgAge.years

	return yearAge




################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB2.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
