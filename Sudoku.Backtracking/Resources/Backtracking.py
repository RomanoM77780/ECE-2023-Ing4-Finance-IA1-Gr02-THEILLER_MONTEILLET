#solvedSudoku = netSolver.Solve(sudoku)
#instance = ((0,0,0,0,9,4,0,3,0),
#           (0,0,0,5,1,0,0,0,7),
#           (0,8,9,0,0,0,0,4,0),
#           (0,0,0,0,0,0,2,0,8),
#           (0,6,0,2,0,1,0,5,0),
#           (1,0,2,0,0,0,0,0,0),
#           (0,7,0,0,0,0,5,2,0),
#           (9,0,0,0,6,5,0,0,0),
#           (0,4,0,9,7,0,0,0,0))

import numpy as np

#instance = [[0,0,0,0,9,4,0,3,0],
#[0,0,0,5,1,0,0,0,7],
#[0,8,9,0,0,0,0,4,0],
#[0,0,0,0,0,0,2,0,8],
#[0,6,0,2,0,1,0,5,0],
#[1,0,2,0,0,0,0,0,0],
#[0,7,0,0,0,0,5,2,0],
#[9,0,0,0,6,5,0,0,0],
#[0,4,0,9,7,0,0,0,0]]
	  
# Affichage (inutile après avoir fait le lien avec le benchmark)
def print_grid(tab):
	for i in range(9):
		for j in range(9):
			print (tab[i][j], end = " "),
		print ()

# Fonction pour trouver l'entrée dans la grille qui n'est toujours pas utilisée
# Recherche dans la grille pour trouver une entrée qui n'est toujours pas attribuée.
# S'il est trouvé, la ligne des paramètres de référence, col sera défini sur l'emplacement non attribué et true est
# revenu. S'il ne reste aucune entrée non affectée, false est renvoyé.

# 'l' est une variable de liste qui a été transmise par la fonction solve_sudoku pour suivre l'incrémentation des lignes et des colonnes
def is_location_empty(tab, l):
	for ligne in range(9):
		for col in range(9):
			if(tab[ligne][col]== 0):
				l[0]= ligne
				l[1]= col
				return True
	return False

# Renvoie un booléen qui indique si une entrée affectée
# dans la ligne spécifiée correspond au nombre donné.
def is_in_ligne(tab, ligne, valeur):
	for i in range(9):
		if(tab[ligne][i] == valeur):
			return True
	return False

# Renvoie un booléen qui indique si une entrée affectée dans la colonne spécifiée correspond au nombre donné.
def is_in_col(tab, col, valeur):
	for i in range(9):
		if(tab[i][col] == valeur):
			return True
	return False

# Renvoie un booléen qui indique si une entrée affectée dans la zone 3x3 spécifiée correspond au nombre donné
def is_in_box(tab, ligne, col, valeur):
	for i in range(3):
		for j in range(3):
			if(tab[i + ligne][j + col] == valeur):
				return True
	return False

# Vérifie s'il sera possible d'attribuer la valeur à la ligne donnée, col
def check_location_is_safe(arr, ligne, col, valeur):
	
	# Vérifiez si 'valeur' n'est pas déjà placé dans la ligne actuelle, la colonne actuelle et la boîte 3x3 actuelle
	return (not is_in_ligne(arr, ligne, valeur) and
		(not is_in_col(arr, col, valeur) and
		(not is_in_box(arr, ligne - ligne % 3,
						col - col % 3, valeur))))

# Prend une grille partiellement remplie et tente d'attribuer des valeurs à tous les emplacements non attribués de manière à 
# répondre aux exigences de la solution Sudoku (non-duplication entre les lignes, les colonnes et les cases)
def solve_sudoku(arr):
	# 'l' sert de buffer pour stocker les coordonnées dans la fonction is_location_empty
	l =[0, 0]
	
	# teste si il reste un emplacement vide
	if(not is_location_empty(arr, l)):
		return True
	# Attribue les valeurs de la liste à la ligne et à la colonne que nous avons obtenues à partir de la fonction ci-dessus
	ligne = l[0]
	col = l[1]
	

	for valeur in range(1, 10):

		if(check_location_is_safe(arr,ligne, col, valeur)):

			# assigne la valeur testée
			arr[ligne][col]= valeur
			if(solve_sudoku(arr)):
				return True

			# si on a 2 valeurs identiques alors on revient arrière
			arr[ligne][col] = 0
			
	# appel du backtracking	
	return False

	# Si on a une solution alors on affiche le résultat (test inutile une fois qu'on a raccordé au benchmark)
if(solve_sudoku(instance)):
	#print_grid(instance)
	r=instance
else:
	print ("Aucune solution trouvée")