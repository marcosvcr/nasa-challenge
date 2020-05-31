import csv

f = open('covid_italia.csv')
csv_f = csv.reader(f)

list = []

death = []

cases = []

for row in csv_f:
  list.append(row)
  
  
for i in range(2,102):
	rowDeaths = []
	rowCases = []
	for j in range(1,22):
		if list[i][j] == '':
			list[i][j] = '(0) 0'
		if list[i][j].find('(') == -1:
			list[i][j] = '(0) ' + list[i][j]
		
		text = list[i][j].split(' ')
		dummyDeath = text[0]
		dummyCases = text[1]
		dummyDeath = dummyDeath.replace('(','')
		dummyDeath = dummyDeath.replace(')','')
		print('death: ' + dummyDeath)
		print('case: ' + dummyCases)
		rowDeaths.append(dummyDeath)
		rowCases.append(dummyCases)
	death.append(rowDeaths)
	cases.append(rowCases)
	
with open('deaths.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	for x in death:
		writer.writerow(x)
		
with open('cases.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	for x in cases:
		writer.writerow(x)