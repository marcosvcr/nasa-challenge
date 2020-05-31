import csv

f = open('covid_brazil.csv')
csv_f = csv.reader(f)

list = []

death = []

cases = []

for row in csv_f:
  list.append(row)
  
  
for i in range(2,187):
	rowDeath = []
	rowCase = []
	for j in range(2,29):
		if list[i][j] == '':
			list[i][j] = '0'

		
		if list[i][1] == 'Deaths':
			rowDeath.append(list[i][j])
		elif list[i][1] == 'Cases':
			rowCase.append(list[i][j])
	death.append(rowDeath)
	cases.append(rowCase)
print(death)		

	
with open('deaths_brazil.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	for x in death:
		writer.writerow(x)
		
with open('cases_brazil.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	for x in cases:
		writer.writerow(x)