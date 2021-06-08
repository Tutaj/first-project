#
import csv
import decimal
age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charge = []

with open('insurance.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        for key in row:
            if key == 'age':
                age.append(row['age'])
            elif key== 'sex':
                sex.append(row['sex'])
            elif key == 'bmi':
                bmi.append(row['bmi'])
            elif key == 'children':
                children.append(row['children'])
            elif key == 'smoker':
                smoker.append(row['smoker'])
            elif key == 'region':
                region.append(row['region'])
            elif key == 'charges':
                charge.append(row['charges'])

def calculate_smoker(smoker, charges):
    x = 0
    smokers = 0
    nonsmokers = 0
    total_charges_smoker = decimal.Decimal(0.0)
    total_charges_nonsmoker = decimal.Decimal(0.0)
    for person in smoker: 
        if person == 'yes':
            total_charges_smoker += decimal.Decimal(charges[x])
            smokers +=1
        elif person == 'no':
            total_charges_nonsmoker += decimal.Decimal(charges[x])
            nonsmokers +=1
        x+=1
    #print(str(total_charges_smoker) + " for " + str(smokers) + " smoking people.")
    #print(str(total_charges_nonsmoker) + " for " + str(nonsmokers) + " nonsmoking people.")
    ###########################################################
    avg_charge_smoker = total_charges_smoker / smokers
    avg_charge_smoker = "{:.0f}".format(avg_charge_smoker)
    avg_charge_nonsmoker = total_charges_nonsmoker / nonsmokers
    avg_charge_nonsmoker = "{:.0f}".format(avg_charge_nonsmoker)
    difference = float(avg_charge_smoker) / float(avg_charge_nonsmoker)
    difference = difference * 100
    difference = "{:.0f}".format(difference)
    print("Smokers pay on average: " + str(avg_charge_smoker) + " dollars for their insurance and it's " + str(difference) + "% more than non-smokers for which costs were on average: " + str(avg_charge_nonsmoker) + " dollars." )
    return total_charges_smoker, total_charges_nonsmoker
calculate_smoker(smoker,charge)