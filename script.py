print('Une suite récurente s\'exprime sous la forme Un=f(n)')
TermeGeneral = input('Veuillez entrer le terme général de la suite: ')
print('Mode 1: Calcul d`un terme specifique de la suite')
print('Mode 2: Calcul des n premiers réels de la suite la suite')
ModeNumber2 = float(input('Veuillez entrer le mode choisi: '))
if ModeNumber2 == 1:
	ValeurN = input('Veuillez entrer la valeur de n: ')
	TermeDeRangN = TermeGeneral.replace('n', '*' + str(ValeurN))
	Resultat = eval(TermeDeRangN)
	print(f'La valeur de Un pour n={ValeurN} est {Resultat}')
elif ModeNumber2 == 2:
	Terme = float(input('Veuillez entrer le terme initial de la suite: '))
	TermeFinal = float(input('Veuillez entrer le terme final de la suite: '))
	while Terme <= TermeFinal:
		TermeRangN = TermeGeneral.replace('n', '*' + str(Terme))
		Resultat = eval(TermeRangN)
		print(f'U{Terme} = {Resultat}')
		Terme = Terme + float(1)
