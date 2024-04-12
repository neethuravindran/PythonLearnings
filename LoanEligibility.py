import csv


def getProfession():
    profSet = set()
    f = open('bank-data.csv', 'r')
    with f as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            if line_count > 1:
                profSet.add(row[0].lower())
        f.close()
    return profSet


def getCustData(prof):
    age = set()
    f = open('bank-data.csv', 'r')
    with f as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            if line_count > 1:
                if prof.lower() == row[0].lower():
                    age.add(int(row[2]))

        f.close()
        print(age)
    return age


print("Welcome to Bank of Portugal")
print("Provide profession.\nPlease enter END to exit.")
flag = True
out = {}
while flag:
    prof = input("Enter the profession: ")
    if prof:
        profSet = getProfession()
        if prof.lower() in profSet:
            cage = int(input('Enter Customer Age: '))
            age = getCustData(prof)
            print('Minimum Eligible Age: {} Maximum Eligible Age: {}'.format(min(age), max(age)))
            if min(age) <= cage <= max(age):
                print("Customer is Eligible for loan")
                out[prof] = str(min(age)) + "," + str(max(age))
            else:
                print(
                    "Customer is NOT Eligible for loan. For Profession {} Minimum Eligible Age: {} Maximum Eligible "
                    "Age: {}".format(
                        prof, min(age), max(age)))
                out[prof] = str(min(age)) + "," + str(max(age))
        else:
            if prof.lower() == 'end':
                flag = False
            else:
                print('Customer is NOT Eligible for loan. For Profession {} does not exist in database'.format(prof))
                print('Profession {} does not exist in database'.format(prof))

print(out)
