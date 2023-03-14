import csv
from prettytable import PrettyTable


#List of dictionaries
lista = []

# with certifica que o ficheiro é bem aberto e fechado
with open('myheart.csv','r') as file:
	dicionarios = csv.DictReader(file)
	for linha in dicionarios:
		lista.append(linha)


def distribution_by_sex(lista):
	dict_por_sexo = {'M': 0, 'F': 0}

	for dicionario in lista:
		#print(dicionario)
		if (dicionario['sexo'] == 'M' and dicionario['temDoença'] == '1'):
			dict_por_sexo['M'] += 1
		if (dicionario['sexo'] == 'F' and  dicionario['temDoença'] == '1'):
			dict_por_sexo['F'] += 1

	return dict_por_sexo
	
def distribution_by_age(lista):
	dict_por_idade = {'[30-34]': 0, '[35-39]': 0, '[40-44]': 0}

	for dicionario in lista:
		#print(dicionario)
		if (int(dicionario['idade']) >= 30 and int(dicionario['idade']) <= 34):
			dict_por_idade['[30-34]'] += 1
		if (int(dicionario['idade']) >= 35 and int(dicionario['idade']) <= 39):
			dict_por_idade['[35-39]'] += 1
		if (int(dicionario['idade']) >= 40 and int(dicionario['idade']) <= 44):
			dict_por_idade['[40-44]'] += 1

	

	return dict_por_idade





def distribution_by_colesterol(lista):
	dict_por_colesterol = {}



	for i in range(0, 604, 10):
		dict_por_colesterol[str(i) + '-' + str(i+10)] = 0 #{'0-10': 0, '10-20': 0, '20-30': 0....}


	for i in range(0, 604, 10):
		for dicionario in lista:
			if(int(dicionario['colesterol']) >= i and int(dicionario['colesterol']) < i+10):
				dict_por_colesterol[str(i) + '-' + str(i+10)] += 1


	return dict_por_colesterol


def pretty_print(dicionario):
	table = PrettyTable()
	table.field_names = ['Key', 'Value']

	for key, value in dicionario.items():
		table.add_row([key, value])

	print(table)




if __name__ == '__main__':
	#print(lista)
	print("Por sexo:")
	pretty_print(distribution_by_sex(lista)) 
	print("Por faixa etária")
	pretty_print(distribution_by_age(lista)) 
	print("Por colesterol, separado por intervalos de 10\n")
	pretty_print(distribution_by_colesterol(lista)) 

