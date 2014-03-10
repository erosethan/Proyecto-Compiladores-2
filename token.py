#!/usr/bin/python

def esDigito(char):
	return '0' <= char <= '9'

def tokenEntero(expresion):
	indice = 0
	estado = 'E0'
	
	while estado != 'E2':
		sigEstado = 'E2'
		char = expresion[indice]
		
		if estado == 'E0':
			if esDigito(char):
				sigEstado = 'E1'
		
		elif estado == 'E1':
			if esDigito(char):
				sigEstado = 'E1'
			else:
				return indice
		
		estado = sigEstado
		indice += 1
	
	return 0
	
def tokenFlotante(expresion):
	indice = 0
	estado = 'F0'
	
	while estado != 'F4':
		sigEstado = 'F4'
		char = expresion[indice]
		
		if estado == 'F0':
			if esDigito(char):
				sigEstado = 'F1'
			elif char == '.':
				sigEstado = 'F2'
		
		elif estado == 'F1':
			if esDigito(char):
				sigEstado = 'F1'
			elif char == '.':
				sigEstado = 'F3'
			else:
				return indice
		
		elif estado == 'F2':
			if esDigito(char):
				sigEstado = 'F3'
		
		elif estado == 'F3':
			if esDigito(char):
				sigEstado = 'F3'
			else:
				return indice
		
		estado = sigEstado
		indice += 1
	
	return 0

test = raw_input() + '\n'
print tokenFlotante(test)
print tokenEntero(test)
