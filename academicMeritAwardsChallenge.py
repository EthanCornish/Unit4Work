import csv

listAcademic1 = []
aImportFile = open('/Users/19ecornish/Downloads/noe-comp.xlsx - academic.csv', 'r')
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
    # Make a copy of the sublist, wipe origional sublist then add things back in correct order
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
                          listAcademic2[number][3], subjects ])
    number += 1

for c in listAcademic3:
    print(c)


# listMerit = []
# mImportFile = open('/Users/19ecornish/Downloads/noe-comp.xlsx - merit.csv', 'r')
# for line in csv.reader(mImportFile):
#    listMerit.append(line)
# mImportFile.close()
# print('DEBUG listMerit[0:2] =', listMerit[0:2])

