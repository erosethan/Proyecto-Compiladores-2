#!/usr/bin/python3

def esDigito(char):
	return '0' <= char <= '9'

def esIdValido(char):
	if 'a' <= char <= 'z':
		return True
	if 'A' <= char <= 'Z':
		return True
	return char == '_'

def tokenIdentificador(expresion):
	indice = 0
	estado = 'I0'
	
	while estado != 'I2':
		sigEstado = 'I2'
		char = expresion[indice]
		
		if estado == 'I0':
			if esIdValido(char):
				sigEstado = 'I1'
		
		if estado == 'I1':
			if esIdValido(char):
				sigEstado = 'I1'
			elif esDigito(char):
				sigEstado = 'I1'
			else:
				return ('I', indice)
		
		estado = sigEstado
		indice += 1
	
	return ('N', 0)

def tokenNumero(expresion):
	indice = 0
	estado = 'N0'
	
	while estado != 'N4':
		sigEstado = 'N4'
		char = expresion[indice]
		
		if estado == 'N0':
			if esDigito(char):
				sigEstado = 'N1'
			elif char == '.':
				sigEstado = 'N2'
		
		elif estado == 'N1':
			if esDigito(char):
				sigEstado = 'N1'
			elif char == '.':
				sigEstado = 'N3'
			else:
				return ('E', indice)
		
		elif estado == 'N2':
			if esDigito(char):
				sigEstado = 'N3'
		
		elif estado == 'N3':
			if esDigito(char):
				sigEstado = 'N3'
			else:
				return ('F', indice)
		
		estado = sigEstado
		indice += 1
	
	return ('N', 0)

test = input() + '\n'
print(tokenIdentificador(test))