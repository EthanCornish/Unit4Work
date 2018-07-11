# exit code 1 is for incorrect input for file name and directory
# exit code 2 is for incorrect file format for merit input file

# CSV library used when reading files to automatically strip the \n from each line and split at each comma into a list
import csv

# Defining listAcademic1, reading file
listAcademic1 = []
fileName = input('Directory and Name of location for Academic Input .csv file. '
                 'e.g. /Users/19ecornish/Downloads/academic.csv\n:')
try:
    aImportFile = open(fileName, 'r')
except FileNotFoundError:
    print('The input file could not be found.\nExiting the program.')
    exit(1)
# Using csv.reader to strip and split each line.
for line in csv.reader(aImportFile):
    listAcademic1.append(line)
aImportFile.close()

# Define lists for the for loop
poppedList = []
tempList = []
# Remove the first record in the array
poppedList.append(listAcademic1.pop(0))
# Define a counting variable
number = 0
# Removes unnecessary information and reorders remaining information.
for entry in listAcademic1:
    # Popping all of the unimportant information
    poppedList.append(entry.pop(0))
    poppedList.append(entry.pop(1))
    poppedList.append(entry.pop(2))
    poppedList.append(entry.pop(5))
    poppedList.append(entry.pop(6))
    poppedList.append(entry.pop(6))
    poppedList.append(entry.pop(6))

    # Rearranging the order of the list
    # Make a copy of the sublist, wipe original sublist then add things back in correct order
    tempList = entry
    entry = []
    entry.append(tempList[1])
    entry.append(tempList[4])
    entry.append(tempList[3])
    entry.append(tempList[2])
    entry.append(tempList[5])
    entry.append(tempList[0])
    listAcademic1[number] = entry
    number += 1
# Arranging the order of students to numeric order by UID
listAcademic1.sort()

# Defining list to hold the information in listAcademic1 but one record per student which has all subjects and scores
listAcademic2 = []
# Resetting number to be used in this loop
number = 0
for e in listAcademic1:
    # Adding the information from listAcademic1 into listAcademic2 but formatted according to the textfile.
    listAcademic2.append([listAcademic1[number][0], listAcademic1[number][1], listAcademic1[number][2],
                          listAcademic1[number][3], [ [listAcademic1[number][5], listAcademic1[number][4]]]])
    # Printing listAcademic2 in its first form for debugging
    number += 1

# Resetting number to be used in this loop
number = 0
for i in listAcademic1:
    # If a student has multiple records in listAcademic2 it adds the subjects into one record.
    # However the previous records remain and need to be erased.
    if listAcademic2[number][0] == listAcademic2[number-1][0]:
        listAcademic2[number][4] = listAcademic2[number][4] + listAcademic2[number-1][4]
    number += 1

# Defining variables for while loop

# Total is the number of records in the list before the while loop. Used to determine if the loop is complete.
total = len(listAcademic2)
# Resetting number for the loop
number = 0
# Cycles, counts how many times a record has been popped to counter-balance the index changing from popping
cycles = 0
# While loop to put all of the subjects for each person in one record so each person has only one record
while number < total:
    # Checks is the UID for the current record is the same as the last and that the current term is not the first
    if listAcademic2[number-cycles][0] == listAcademic2[number-1-cycles][0] and number - 1 >= 0:
        # Pops the unneeded data to poppedList
        poppedList.append(listAcademic2.pop(number-1-cycles))
        cycles += 1
    number += 1

# Resetting total and count for while loop
total = len(listAcademic2)
count = 0
# While loop to remove any subjects that do not have academic awards
while count < total:
    # Resetting cycle and number for each student.
    cycle = 0
    number = 0
    # The number of subjects for each student
    sTotal = len(listAcademic2[count][4])
    # Sub loop removes the subjects for the individual student record in listAcademic2)
    while number < sTotal:
        # Removes the record if the score for the subject is a number (not NULL).
        # try loop to catch error if trying to make 'NULL' an int
        try:
            listAcademic2[count][4][number-cycle][1] = int(listAcademic2[count][4][number-cycle][1])
            # If the score is less than or equal to 84 pop that subject and score.
            if listAcademic2[count][4][number - cycle][1] <= 84:
                poppedList.append(listAcademic2[count][4].pop(number-cycle))
                cycle += 1
        except ValueError:
            # If the score is 'NULL' then pop it
            if listAcademic2[count][4][number-cycle][1] == 'NULL':
                poppedList.append(listAcademic2[count][4].pop(number-cycle))
                cycle += 1
        number += 1
    count += 1

# Resetting number, cycle and total for loop
number = 0
cycle = 0
total = len(listAcademic2)
# Loop to remove any records that have no academic awards
while number < total:
    # If the subjects sublist is empty
    if listAcademic2[number-cycle][4] == []:
        # Remove the record
        poppedList.append(listAcademic2.pop(number-cycle))
        cycle += 1
    number += 1

# Taking listAcademic2 and converting it into listAcademic3

# Defining listAcademic 3 and resetting number
listAcademic3 = []
number = 0
# For loop to go through each record
for a in listAcademic2:
    # Subjects is a sub list that stores the name of the subjects a person will recieve an academic for
    subjects = []
    # Adds the subjects to the sublist
    for item in listAcademic2[number][4]:
        subjects.append(item[0])
    # Appending each record in listAcademic2 to listAcademic3
    listAcademic3.append([listAcademic2[number][0], listAcademic2[number][1], listAcademic2[number][2],
                          listAcademic2[number][3], subjects, len(subjects)])
    number += 1


# ------------------------------------------------------------------ #


# Defining listMerit1, reading file (fileName will be input from user)
listMerit1 = []
fileName = input('\nDirectory and Name of location for Merit Input .csv file. '
                 'e.g. /Users/19ecornish/Downloads/merit.csv\n:')
try:
    mImportFile = open(fileName, 'r')
except FileNotFoundError:
    print('The input file could not be found.\nExiting the program.')
    exit(1)
# Using csv.reader to strip and split each line.
for line in csv.reader(mImportFile):
   listMerit1.append(line)
mImportFile.close()

# If the merit input is in the form: UID, Surname, Preferred, Year Level, Class Description with another column for
#   score then this block should run. It was in this form in the sample input file however there was no column for score
#   so I added one with both 'merit' and 'none' as the data for testing.
if len(listMerit1[0]) == 6:
    # Remove the header record from the array
    poppedList.append(listMerit1.pop(0))
    # Rearranging the order of the list in the same way listAcademic1 was done
    for record in listMerit1:
        tempList = record
        record = []
        record.append(tempList[0])
        record.append(tempList[2])
        record.append(tempList[1])
        record.append(tempList[3])
        record.append(tempList[4])
        record.append(tempList[5])

# If the merit input file is in the form: UID, Surname, Preferred, Gender, Year Level, Class Description, Class Teacher,
#    Score as it is on the instructions then this block should run and output listMerit1 as shown in textfile
elif len(listMerit1[0]) == 8:
    # Remove the header record from the array
    poppedList.append(listMerit1.pop(0))
    # Rearranging the order of the list in the same way listAcademic1 was done
    for record in listMerit1:
        # Popping all of the unimportant information
        poppedList.append(record.pop(3))
        poppedList.append(record.pop(5))

        # Rearranging the order of the list
        # Make a copy of the sublist, wipe original sublist then add things back in correct order
        tempList = record
        record = []
        record.append(tempList[0])
        record.append(tempList[2])
        record.append(tempList[1])
        record.append(tempList[3])
        record.append(tempList[4])
        record.append(tempList[5])
        listAcademic1[number] = record
        number += 1
else:
    print('Merit Input File Format was not Recignised.')
    exit(2)

# Sorts listMerit1 by student number
listMerit1.sort()

# While loop to remove all records that do not have merit awards for
# Number is used as a counting variable
number = 0
# Counts how many times a record has been popped to counter-balance the index changing
cycles = 0
# Total for the while loop. Set now as the len of the list will change due to popping
total = len(listMerit1)
while number < total:
    if listMerit1[number-cycles][5] == 'none' or listMerit1[number-cycles][5] == 'None' or\
            listMerit1[number-cycles][5] == 'NONE':
        poppedList.append(listMerit1.pop(number-cycles))
        cycles += 1
    number += 1

# Creating listMerit2 in the form shown in the textfile
# Defining listMerit2 and resetting number
listMerit2 = []
number = 0
for b in listMerit1:
    # The fourth index is in a sublist as more subjects can be added
    listMerit2.append([listMerit1[number][0], listMerit1[number][2], listMerit1[number][1], listMerit1[number][3], [listMerit1[number][4]] ])
    number += 1

# If a student has multiple records in listAcademic2 it adds the subjects into one record.
number = 0
for c in listMerit2:
    if listMerit2[number][0] == listMerit2[number-1][0]:
        listMerit2[number][4] = listMerit2[number][4] + listMerit2[number-1][4]
    number += 1


# Loop to make sure that each person only has one record (the record with all of the subjects)
# Resetting number, cycles and total
number = 0
cycles = 0
total = len(listMerit2)
while number < total:
    # If the UID on the current record is the same as the previous record and the current record is not the first
    if listMerit2[number-cycles][0] == listMerit2[number-cycles-1][0] and number - 1 >= 0:
        # Pop the previous record
        poppedList.append(listMerit2.pop(number-1-cycles))
        cycles += 1
    number += 1


# Creating listMerit3 in form shown in textfile
listMerit3 = []
for d in listMerit2:
    listMerit3.append([d[0], d[1], d[2], d[3], d[4], len(d[4])])

# Creating listOutput as shown in textfile

# Defining list
listOutput = []
# Space is used as a placeholder for the empty column in the output table
space = ''
# Loop goes through each record in ListAcademic 3 and if there is also a
#       record for merit for the same student then it is added as one record
#       otherwise the record is left as just the academic with place holders

# Goes through each record in academic list
for i in listAcademic3:
    # found records if there is a match in the UIDs for academic and merit lists
    found = False
    # Goes through each record for merit list resetting cycle each time
    cycle = 0
    for item in listMerit3:
        # Match found
        if item[0] == i[0]:
            found = True
            break
        cycle += 1
    if found:
        # Add a record to listOutput formatted according to instructions with both academic and merit
        listOutput.append(
            [i[0], i[1], i[2], i[3], i[4], i[5], space, listMerit3[cycle][0], listMerit3[cycle][1],
                listMerit3[cycle][2], listMerit3[cycle][3], listMerit3[cycle][4], listMerit3[cycle][5]])
    elif not found:
        # Add a record to listOutput only with values for academic awards, merit values are left blank
        listOutput.append([i[0], i[1], i[2], i[3], i[4], i[5], space, space, space, space, space, space, space])

# Loop checks if there are any records in the merit list that haven't
#   already been added to output list. If there are it adds them
for i in listMerit3:
    # records if a match was found
    found = False
    # Goes through each record already in output list
    for item in listOutput:
        if i[0] == item[0]:
            # match found, exits sub for loop. Nothing needs to be added
            found = True
            break
    if not found:
        # If the match was not found then add the merit record to output list using placeholders for academic values
        listOutput.append([space, space, space, space, space, space, space, i[0], i[1], i[2], i[3], i[4], i[5]])


fileName = input('\nName and Directory to place output file. '
                       'e.g. /Users/19ecornish/Desktop/AcademicMeritOutput.csv\n:')

try:
    outputFile = open(fileName, 'w')
except FileNotFoundError:
    print('The output file could not be created. The directory may be incorrect.\nExiting the program.')
    exit(1)

outputFile.write(
        'UID, Preferred, Surname, Year, Academic, Count A, , UID, Preferred, Surname, Year, Merit, Count M\n')

for record in listOutput:
    # Write UID Academic
    outputFile.write(record[0])
    outputFile.write(',')
    # Write Preferred Name Academic
    outputFile.write(record[1])
    outputFile.write(',')
    # Write Surname Academic
    outputFile.write(record[2])
    outputFile.write(',')
    # Write Year Level Academic
    outputFile.write(record[3])
    outputFile.write(',')
    # Write Subjects for Academic
    for i in record[4]:
        outputFile.write(i)
        if i != record[4][-1]:
            outputFile.write(';')
    outputFile.write(',')
    # Write Count A
    record[5] = str(record[5])
    outputFile.write(record[5])
    outputFile.write(',')
    # Write Blank Space
    outputFile.write(record[6])
    outputFile.write(',')
    # Write UID Merit
    outputFile.write(record[7])
    outputFile.write(',')
    # Write Preferred Name Merit
    outputFile.write(record[8])
    outputFile.write(',')
    # Write Surname Merit
    outputFile.write(record[9])
    outputFile.write(',')
    # Write Year Level Merit
    outputFile.write(record[10])
    outputFile.write(',')
    # Write Subjects for Merit
    for i in record[11]:
        outputFile.write(i)
        if i != record[11][-1]:
            outputFile.write(';')
    outputFile.write(',')
    # Write Count M
    record[12] = str(record[12])
    outputFile.write(record[12])

    outputFile.write('\n')
outputFile.close()

print("\nInput Files Processed. Output Saved at: '{0}'".format(fileName))