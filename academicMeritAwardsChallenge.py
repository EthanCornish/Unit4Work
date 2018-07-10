import csv

listAcademic = []
aImportFile = open('/Users/19ecornish/Downloads/noe-comp.xlsx - academic.csv', 'r')
for line in csv.reader(aImportFile):
    listAcademic.append(line)
aImportFile.close()

# Define lists for the for loop
poppedList = []
tempList = []
# Remove the first record in the array
poppedList.append(listAcademic.pop(0))
# Define a counting variable
number = 0
# Removes unnecessary information and reorders remaining information.
for entry in listAcademic:
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
    listAcademic[number] = entry
    number += 1
# Arranging the order of students to numeric order by UID
listAcademic.sort()

# Defining list to hold the information in listAcademic but one record per student which has all subjects and scores
listByStudent = []
# Resetting number to be used in this loop
number = 0
for e in listAcademic:
    # Adding the information from listAcademic into listByStudent but formatted according to the textfile.
    listByStudent.append([listAcademic[number][0], listAcademic[number][1], listAcademic[number][2],
                          listAcademic[number][3], [ [listAcademic[number][5], listAcademic[number][4]]]])
    # Printing listByStudent in its first form for debugging
    number += 1

# Resetting number to be used in this loop
number = 0
for i in listAcademic:
    # If a student has multiple records in listByStudent it adds the subjects into one record.
    # However the previous records remain and need to be erased.
    if listByStudent[number][0] == listByStudent[number-1][0]:
        listByStudent[number][4] = listByStudent[number][4] + listByStudent[number-1][4]
    number += 1

# Defining variables for while loop

# Total is the number of records in the list before the while loop. Used to determine if the loop is complete.
total = len(listByStudent)
# Resetting number for the loop
number = 0
# Cycles, counts how many times a record has been popped to counter-balance the index changing from popping
cycles = 0
# While loop to clean up from last for loop
while number < total:
    # Checks is the UID for the current record is the same as the last and that the current term is not the first
    if listByStudent[number-cycles][0] == listByStudent[number-1-cycles][0] and number - 1 >= 0:
        # Pops the unneeded data to poppedList
        poppedList.append(listByStudent.pop(number-1-cycles))
        cycles += 1
    number += 1

total = len(listByStudent)
count = 0
while count < total:
    cycle = 0
    number = 0
    sTotal = len(listByStudent[count][4])
    while number < sTotal:
        try:
            listByStudent[count][4][number-cycle][1] = int(listByStudent[count][4][number-cycle][1])
            if listByStudent[count][4][number - cycle][1] <= 84:
                poppedList.append(listByStudent[count][4].pop(number-cycle))
                cycle += 1
        except ValueError:
            if listByStudent[count][4][number-cycle][1] == 'NULL':
                poppedList.append(listByStudent[count][4].pop(number-cycle))
                cycle += 1
        number += 1
    count += 1

print('\n')
for c in listByStudent:
    print(c)

# listMerit = []
# mImportFile = open('/Users/19ecornish/Downloads/noe-comp.xlsx - merit.csv', 'r')
# for line in csv.reader(mImportFile):
#    listMerit.append(line)
# mImportFile.close()
# print('DEBUG listMerit[0:2] =', listMerit[0:2])

