#!/usr/bin/python3
import sys

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
	
	return ('N', 1)

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
	
	return ('N', 1)

def tokenOperador(expresion):
	indice = 0
	estado = 'P0'
	
	while estado != 'Px':
		sigEstado = 'Px'
		char = expresion[indice]
		
		if estado == 'P0':
			sigEstado = {
				'&': 'P1',
				'|': 'P2',
				'!': 'P3',
				'+': 'P4',
				'-': 'P5',
				'/': 'P6',
				'*': 'P7',
				'%': 'P8',
				'=': 'P9',
				'<': 'P10',
				'>': 'P11'
			}.get(char, 'Px')
		
		if estado == 'P1':
			if char == '&':
				return ('&&', 2)
		
		if estado == 'P2':
			if char == '|':
				return ('||', 2)
		
		if estado == 'P3':
			return {
				'=': ('!=', 2)
			}.get(char, ('!', 1))
		
		if estado == 'P4':
			return {
				'+': ('++', 2),
				'=': ('+=', 2)
			}.get(char, ('+', 1))
		
		if estado == 'P5':
			return {
				'-': ('--', 2),
				'=': ('-=', 2)
			}.get(char, ('-', 1))
		
		if estado == 'P6':
			return {
				'=': ('/=', 2)
			}.get(char, ('/', 1))
		
		if estado == 'P7':
			return {
				'=': ('*=', 2)
			}.get(char, ('*', 1))
		
		if estado == 'P8':
			return {
				'=': ('%=', 2)
			}.get(char, ('%', 1))
		
		if estado == 'P9':
			return {
				'=': ('==', 2)
			}.get(char, ('=', 1))
		
		if estado == 'P10':
			return {
				'=': ('<=', 2)
			}.get(char, ('<', 1))
		
		if estado == 'P11':
			return {
				'=': ('>=', 2)
			}.get(char, ('>', 1))
		
		estado = sigEstado
		indice += 1
	
	return ('N', 1)

def tokenSimboloEsp(expresion):
	char = expresion[0]
	return {
		'(': ('(', 1),
		')': (')', 1),
		'{': ('{', 1),
		'}': ('}',1),
		'[': ('[', 1),
		']': (']', 1),
		';': (';', 1),
		',': (',', 1),
		'.': ('.', 1),
		':': (':', 1),
		'#': ('#', 1),
		"'": ("'", 1),
		'"': ('"', 1)
	}.get(char, ('N', 1))

def reconocerToken(expresion):
	token = tokenNumero(expresion)
	if token[0] != 'N': return token
	
	token = tokenIdentificador(expresion)
	if token[0] != 'N': return token
	
	token = tokenOperador(expresion)
	if token[0] != 'N': return token
	
	return tokenSimboloEsp(expresion)

def estaEnAlfabeto(caracter):
	ascii = ord(caracter)
	return ( ( ascii >= 0 and ascii <= 35) or 
				( ascii >= 37 and ascii <= 62 ) or
				( ascii >= 65 and ascii <= 91 ) or
				( ascii >= 97 and ascii <= 125 ) or
				ascii == 93 )
	
def main(nEntrada, nSimbolos, nErrores):
	arcEntrada = open( nEntrada, 'r' )
	arcSimbolos = open( nSimbolos, 'w' )
	arcErrores = open( nErrores, 'w' )
	arcErrores.write('Linea de Error\tSimbolo\n')
	texto = arcEntrada.read()
	numLinea = 1
	while len(texto) > 0:
		token = reconocerToken(texto)
		#Hay que checar si esta en el alfabeto
		if texto[0] == '\n':
			print(numLinea)
			numLinea = numLinea + 1
		car = texto[0]
		texto = texto[token[1]: len(texto)]
		print(car)
		if( not(estaEnAlfabeto(car)) ):
			arcErrores.write( car + '\t\t\t\t' + str(numLinea) + '\n' )
		print(token)
		if token[0] != 'N':
			print(token)
	arcErrores.close()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])