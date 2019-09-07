#-*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import openpyxl


workbook = openpyxl.load_workbook('Pesquisa de Interesse em Produtos Reutilizáveis (respostas).xlsx')
sheets = workbook.get_sheet_names()

total_entrevistados = 137
total_18e22 = 91


def graficoConsciencia():
	'''Analise da consciencia ambiental dos 18 aos 22 anos.'''
	sheet = workbook.get_sheet_by_name('Planilha2')

	rows = tuple(sheet['G2':'G92'])
	lista = []

	for row in rows:
		lista.append(row[0].value)

	niveis = {'1': 0, '2': 0, '3':0, '4':0, '5':0}

	for i in lista:
		niveis[str(i)] += 1

	print(niveis)

	# Projetando o gráfico:
	plt.title('Consciência Ambiental entre os 17 e 21 anos')
	plt.rcParams['figure.figsize'] = (11,7)

	x1 = [1]
	y1 = niveis['1']
	plt.bar(x1,y1,color='#00FF00', label='Não está preocupado')

	x2 = [2]
	y2 = niveis['2']
	plt.bar(x2,y2,color='#32CD32',label='Pouco preocupado')

	x3 = [3]
	y3 = niveis['3']
	plt.bar(x3,y3,color='#228B22',label='Mais ou menos')

	x4 = [4]
	y4 = niveis['4']
	plt.bar(x4,y4,color='#008000',label='Preocupado')

	x5 = [5]
	y5 = niveis['5']
	plt.bar(x5,y5,color='#006400',label='Muito preocupado')


	plt.xlabel('Níveis de consciência')
	plt.ylabel('Número de votantes')

	plt.legend()

	plt.savefig('consciencia_17_21.png', dpi=300)

	print(niveis)


def acoes_17_21():
	'''Quais ações sustentáveis os jovens desta faixa praticam?'''

	# Opções da pesquisa:
	opcoes = {'Economia de energia':0, 'Cultivo de plantas':0, 'Compra de alimentos orgânicos':0, 'Reciclagem':0, 'Levagem de carro/bike/moto à seco':0,'Uso de pilhas recarregáveis':0, 'Veganismo':0, \
	'Redução do uso de plástico descartável (copos, talheres, pratos, canudos)':0, 'Evita o uso de sacolas plásticas':0, 'Economia de papel':0, 'Uso de lâmpadas de LED na casa inteira':0, \
	'Separação correta do lixo':0, 'Não jogo óleo no meio ambiente':0, 'Economia de água durante o banho':0, 'Utilizar coletor menstrual':0, 'Não jogo lixo nas ruas':0, 'Reutilizar óleo para fazer sabão.':0}

	sheet = workbook.get_sheet_by_name(sheets[1])

	# Selecionando as células...
	rows = tuple(sheet['H2:H92'])

	# Transformando cada célula em uma lista e verificando se ela contém às opções definidas na pesquisa...
	for row in rows:
		i = row[0].value # pega o valor da célula
		if i is not None: # se a célula não for nula:
			acts = i.split(', ') # transforma o valor da célula em uma lista
			if 'Redução do uso de plástico descartável (copos' in acts:
				opcoes['Redução do uso de plástico descartável (copos, talheres, pratos, canudos)'] += 1
			for opcao in opcoes.keys(): # e verifica se ela contém as opções da pesquisa...
				if opcao in acts:
					opcoes[opcao] += 1
					acts.remove(opcao)
				if acts == []:
					break
		else:
			continue

	print(opcoes)
	return opcoes


def graficoEconomiaRecursos():
	# Importando resultados:
	opcoes = acoes_17_21()

	# Plotando o gráfico relacionado a Economia de Recursos por parte dos jovens:
	plt.title('Economia de recursos entre os 17 e 21 anos')
	plt.rcParams['figure.figsize'] = (11,7)

	x1 = [1]; x2 = [2]; x3 = [3]; x4 =  [4]
	y1 = [opcoes['Economia de energia']]; y2 = [opcoes['Uso de lâmpadas de LED na casa inteira']];
	y3 = [opcoes['Levagem de carro/bike/moto à seco'] + opcoes['Economia de água durante o banho']]; y4 = [opcoes['Economia de papel']]
	
	plt.xlabel('Ações')
	plt.ylabel('Quantidade de pessoas')

	plt.bar(x1,y1,color='#5F9EA0',label='Energia')
	plt.bar(x2,y2,color='#66CDAA',label='Lâmpadas de LED')
	plt.bar(x3,y3,color='#7FFFD4',label='Água')
	plt.bar(x4,y4,color='#008B8B',label='Papel')
	plt.legend()

	plt.savefig('economia de recursos.png', dpi = 300)


def graficoNovosHabitos():
	# Importando resultados:
	opcoes = acoes_17_21()
	# Plotando o gráfico de como está a situação dos jovens perante às tendências e conceitos básicos de sustentabilidade:
	plt.title('Hábitos sustentáveis entre os 17 e 21 anos')
	plt.rcParams['figure.figsize'] = (11,7)

	x1 = [1]; x2 = [2]; x3 = [3]; x4 =  [4]; x5 = [5]
	y1 = [opcoes['Veganismo']]; y2 = [opcoes['Reciclagem']]; y3 = [opcoes['Separação correta do lixo']]; y4 = [opcoes['Compra de alimentos orgânicos']]; y5 = [opcoes['Cultivo de plantas']]

	plt.xlabel('Ações')
	plt.ylabel('Quantidade de pessoas')

	plt.bar(x1,y1,color='#F5DEB3',label='Veganismo')
	plt.bar(x2,y2,color='#FFDEAD',label='Reciclagem')
	plt.bar(x3,y3,color='#F4A460',label='Separação do lixo')
	plt.bar(x4,y4,color='#D2691E',label='Consumo de alimentos orgânicos')
	plt.bar(x5,y5,color='#CD853F',label='Cultivo de plantas')
	plt.legend()

	plt.savefig('novos hábitos.png', dpi = 300)


def graficoPlastico():
	# Importando resultados:
	opcoes = acoes_17_21()
	# Plotando o gráfico sobre o quão o jovem está trabalhando para diminuir o problema do plástico
	plt.title('Jovem e o plástico')
	plt.rcParams['figure.figsize'] = (11,7)

	x1 = [1]; x2 = [2]
	y1 = [opcoes['Redução do uso de plástico descartável (copos, talheres, pratos, canudos)']]; y2 = [opcoes['Evita o uso de sacolas plásticas']]

	plt.xlabel('Itens cujos os jovens estão reduzindo')
	plt.ylabel('Quantidade de jovens')
		
	plt.bar(x1,y1, color = '#FF8C00',label='Redução do plástico de uso único')
	plt.bar(x2,y2, color = '#4682B4',label='Redução do uso de sacolas plásticas')
	plt.legend()

	plt.savefig('redução do plástico.png', dpi = 300)


def pessoascomcanudo():
	'''Verificando quantos jovens possuem um canudo ecológico'''
	sheet = workbook.get_sheet_by_name('Planilha2')
	answers = sheet['K2':'K92']

	opcoes = {
	'Sim! Já tenho um canudo reutilizável':0, #1
	'Sim! O problema é que são um pouco caros':0, #2
	'Sim! O problema é que eu não sei onde vende':0, #3
	'Não, mas irei refletir sobre o assunto':0, #4
	'Não, eu não quero levar um canudo na bolsa':0, #5
	'Não. Nunca ouvi falar sobre esses canudos':0, #6
	'Não. Eu realmente não me importo.':0, #7
	'Outras respostas':0 #8
	}

	leadsConscientes = [] # Que possuem canudo (de acordo com #1) -> podem consumir outros produtos e nos indicar
	leadsPrimarios = [] # Que estão de acordo com #2, #3 -> possuem muita chance de comprar um canudo
	leadsPotenciais = [] # Pessoas que consideram a hipótese de comprar um canudo -> De acordo com opção #4
	leadsResistentes = [] # São pessoas que nunca houviram falar ou não se importam -> #5, #6, #7
	leadsManuais = [] # São os que eu vou precisar verificar um por um -> #8

	keys = list(opcoes.keys())

	for row in answers:
		value = row[0].value
		cell = row[0].coordinate

		# Pegando o instagram da criatura:
		instagramCell = cell.replace('K', 'M')
		instagram = sheet[instagramCell].value

		# Fazendo a triagem das respostas:
		if value is not None:
			if value in keys:
				opcoes[value] += 1
				if value == keys[0]:
					leadsConscientes.append(instagram)
				elif value == keys[1] or value == keys[2]:
					leadsPrimarios.append(instagram)
				elif value == keys[3]:
					leadsPotenciais.append(instagram)
				else:
					leadsResistentes.append(instagram)
			else:
				opcoes['Outras respostas'] += 1
				leadsManuais.append(instagram)
	
	print(opcoes)

	# Plotando o gráfico...
	plt.title('Opinião dos jovens sobre os canudos reutilizáveis')
	plt.rcParams['figure.figsize'] = (11,7)

	xConscientes = [1] ; yConscientes = [opcoes['Sim! Já tenho um canudo reutilizável']]
	plt.bar(xConscientes,yConscientes,color = '#2F4F4F', label='1 - Possui canudo')

	xPrimarios = [2]
	yPrimarios = [opcoes['Sim! O problema é que são um pouco caros']]
	plt.bar(xPrimarios,yPrimarios, color= '#00FA9A', label = '2 - Acham caro')

	xPotenciais = [3]; yPotenciais = [opcoes['Sim! O problema é que eu não sei onde vende']]
	plt.bar(xPotenciais, yPotenciais, color='#00FF7F', label='3- Não sabem onde vende')

	xReflet = [4]; yReflet = [opcoes['Não, mas irei refletir sobre o assunto']]
	plt.bar(xReflet,yReflet,color='#98FB98', label='4 - Prometeram refletir')

	xNaoQuerLevarnaBolsa = [5]; yNaoQuerLevarnaBolsa = [opcoes['Não, eu não quero levar um canudo na bolsa']]
	plt.bar(xNaoQuerLevarnaBolsa,yNaoQuerLevarnaBolsa, color='#90EE90', label='5 - Transporte')

	xDesconhecem = [6]; yDesconhecem = [opcoes['Não. Nunca ouvi falar sobre esses canudos']]
	plt.bar(xDesconhecem,yDesconhecem,color='#3CB371',label='6 - Desconhecem a causa')

	xSemInteresse = [7]; ySemInteresse = [opcoes['Não. Eu realmente não me importo.']]
	plt.bar(xSemInteresse,ySemInteresse,color='#2E8B57', label='7 -Não tem interesse')

	xOutras = [8]; yOutras =[opcoes['Outras respostas']]
	plt.bar(xOutras,yOutras,color='#006400', label='8 - Outras respostas')

	plt.legend()
	plt.savefig('canudos.png', dpi=300)


def genderConscience():
	sheet = workbook.get_sheet_by_name(sheets[1])
	plt.title("Interesse em produtos sustentaveis por genero")

	column = sheet['G2':'G92']
	genders = {'Feminino':0, 'Masculino': 0, 'Não-binário':0, 'Trans Masculino':0, 'Trans Feminino': 0}

	# Valores totais:
	F = 0 # female
	M = 0 # male
	N = 0 # not binary
	TM = 0 # trans masculino
	TF = 0 # trans feminino

	for row in column:

		gender_coordinate = str(row[0].coordinate).replace('G', 'D')
		gender = sheet[gender_coordinate].value

		if row[0].value == 4 or row[0].value == 5:
			if gender == 'Feminino':
				genders['Feminino'] += 1
			elif gender == 'Masculino':
				genders['Masculino'] += 1
			elif gender == 'Não-binário':
				genders['Não-binário'] += 1
			elif gender == 'Trans feminino':
				genders['Trans Feminino'] += 1
			elif gender == 'Trans masculino':
				genders['Trans Masculino'] += 1

		if gender == 'Feminino':
			F += 1
		elif gender == 'Masculino':
			M += 1
		elif gender == 'Não-binário':
			N += 1
		elif gender == 'Trans feminino':
			TF += 1
		elif gender == 'Trans masculino':
			TM += 1

	print('Público feminino:\nConscientes: %d\nTotal: %d\nPorcentagem: %.2f%%\n' % (genders['Feminino'], F, (genders['Feminino']/F*100)))
	print('Público masculino:\nConscientes: %d\nTotal: %d\nPorcentagem: %.2f%%\n' % (genders['Masculino'], M, genders['Masculino']/M*100))
	print('Público não-binário:\nConscientes: %d\nTotal: %d\nPorcentagem: %.2f%%\n' % (genders['Não-binário'], N, genders['Não-binário']/N*100))

	plt.xlabel('Gêneros')
	plt.ylabel('Quantidade')

	plt.bar(1, genders['Feminino'], color='#8B008B', label='Feminino')
	plt.bar(2, genders['Masculino'], color='#DC143C',label='Masculino')
	plt.bar(3, genders['Trans Masculino'],color='#4169E1',label='Trans masculino')
	plt.bar(4, genders['Trans Feminino'], color='#98FB98',label='Trans feminino')
	plt.bar(5, genders['Não-binário'],color='#5F9EA0',label='Não-binário')

	plt.legend()
	plt.savefig('Genero.png', dpi=300)


def genderStraw():
	sheet = get_sheet_by_name(sheets[1])
	