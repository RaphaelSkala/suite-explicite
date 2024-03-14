#input du terme général de la suite et du mode
print('Une suite récurente s\'exprime sous la forme Un=f(n)')
TermeGeneral = input('Veuillez entrer le terme général de la suite: ')
print('Mode 1: Calcul d`un terme specifique de la suite')
print('Mode 2: Calcul des n premiers réels de la suite la suite')
ModeNumber = float(input('Veuillez entrer le mode choisi: '))

#si le mode choisi est le mode 1, on calcul un terme spécifique de la suite
if ModeNumber == 1:
	#on input la valeur de n
	ValeurN = input('Veuillez entrer la valeur de n: ')
	#on remplace n par sa valeur donnée précédament
	TermeDeRangN = TermeGeneral.replace('n', '*' + str(ValeurN))
	#on calcul le résultat
	Resultat = eval(TermeDeRangN)
	#on print le résultat
	print(f'La valeur de Un pour n={ValeurN} est {Resultat}')
	
#Si le mode choisi est le mode 2, on calcul tout les termes de la suite, d'un terme initial jusqu'a un terme final
elif ModeNumber == 2:
	#on input les valeurs du terme initial et du terme final
	Terme = float(input('Veuillez entrer le terme initial de la suite: '))
	TermeFinal = float(input('Veuillez entrer le terme final de la suite: '))
	#tant que le terme de la suite n'est pas le terme final, la boucle tourne
	while Terme <= TermeFinal:
		#on remplace n par sa valeur
		TermeRangN = TermeGeneral.replace('n', '*' + str(Terme))
		#on calcul le résultat
		Resultat = eval(TermeRangN)
		#on print le résultat
		print(f'U{Terme} = {Resultat}')
		#on ajoute 1 au terme pour passer au terme suivant
		Terme = Terme + float(1)
		
#si le mode séléctionné n'est pas 1 ou 2, on affiche Mode incorrect
else:
	print("Mode incorrect")
