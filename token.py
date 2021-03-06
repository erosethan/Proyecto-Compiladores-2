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
	
	while estado != 'P12':
		sigEstado = 'P12'
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
			}.get(char, 'P12')
		
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
		'}': ('}', 1),
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

def esEspacio(char):
	return {
		 ' ': True,
		'\n': True,
		'\t': True,
	}.get(char, False)

def valorLexema(cadena):
	return {
		 '(': 'PARENTESIS-ABIERTO',
		 ')': 'PARENTESIS-CERRADO',
		 '{': 'LLAVE-ABIERTA',
		 '}': 'LLAVE-CERRADA',
		 '[': 'CORCHETE-ABIERTO',
		 ']': 'CORCHETE-CERRADO',
		 ';': 'PUNTO-Y-COMA',
		 ',': 'COMA',
		 '.': 'PUNTO',
		 ':': 'DOS-PUNTOS',
		 '#': 'NUMERAL',
		'\'': 'COMILLA-SIMPLE',
		'"' : 'COMILLA-DOBLE',
		'++': 'INCREMENTO-POSITIVO',
		'--': 'INCREMENTO-NEGATIVO',
		'=' : 'ASIGNACION',
		'+=': 'SUMA-ASIGNACION',
		'-=': 'RESTA-ASIGNACION',
		'*=': 'MULTIPLICACION-ASIGNACION',
		'/=': 'DIVISION-ASIGNACION',
		'if': 'IF',
	  'else': 'ELSE',
	'switch': 'SWITCH',
	  'case': 'CASE',
	   'for': 'FOR',
	 'while': 'WHILE',
		'do': 'DO',
		'&&': 'Y',
		'||': 'O',
		 '!': 'NEGACION',
		'!=': 'DIFERENTE',
		 '>': 'MAYOR',
		 '<': 'MENOR',
		'==': 'IGUAL',
		'>=': 'MAYOR-IGUAL',
		'<=': 'MENOR-IGUAL',
		 '+': 'SUMA',
		 '-': 'RESTA',
		 '*': 'MULTIPLICACION',
		 '/': 'DIVISION',
		 '%': 'MODULO',
	   'int': 'INT',
	 'float': 'FLOAT',
	'double': 'DOUBLE',
	  'char': 'CHAR',
	  'void': 'VOID',
	 'short': 'SHORT',
	  'long': 'LONG',
	'signed': 'SIGNED',
  'unsigned': 'UNSIGNED',
   'include': 'INCLUDE',
	'define': 'DEFINE',
	'inline': 'INLINE',
	'return': 'RETURN',
	  'main': 'MAIN'
	}.get(cadena, cadena)

def componenteLexico(token, cadena):
	selectivas = set(['if', 'else', 'switch', 'case'])
	repetitivas = set(['for', 'while', 'do'])
	tiposDatos = set(['void', 'int', 'float', 'double', 'char'])
	calificadoresTipoDato = set(['short', 'long', 'signed', 'unsigned'])
	preprocesador = set(['include', 'define', 'inline'])
	Ireturn = set(['return'])
	Imain = set(['main'])
	logico = set(['&&', '||', '!', '!='])
	relacional = set(['>', '<', '==', '>=', '<='])
	aritmetico = set(['+', '-', '*', '/', '%'])
	asignacion = set(['=', '+=', '-=', '*=', '/='])
	incremento = set(['++', '--'])
	
	if cadena in selectivas:
		return 'ESTRUCTURA SELECTIVA'
	if cadena in repetitivas:
		return 'ESTRUCTURA REPETITIVA'
	if cadena in tiposDatos:
		return 'TIPO DE DATO'
	if cadena in calificadoresTipoDato:
		return 'CALIFICADOR DE TIPO DE DATO'
	if cadena in preprocesador:
		return 'INSTRUCCION DE PREPROCESADOR'
	if cadena in Ireturn:
		return 'RETURN'
	if cadena in Imain:
		return 'MAIN'
	if cadena in logico:
		return 'OPERADOR LOGICO'
	if cadena in relacional:
		return 'OPERADOR RELACIONAL'
	if cadena in aritmetico:
		return 'OPERADOR ARITMETICO'
	if cadena in asignacion:
		return 'ASIGNACION'
	if cadena in incremento:
		return 'INCREMENTO'
	if token == 'E':
		return 'NUMERO ENTERO'
	if token == 'F':
		return 'NUMERO FLOTANTE'
	if token == 'I':
		return 'IDENTIFICADOR'
	return 'SIMBOLO ESPECIAL'

def main(nEntrada, nSimbolos, nErrores):
	arcEntrada = open(nEntrada, 'r')
	arcErrores = open(nErrores, 'w')
	arcSimbolos = open(nSimbolos, 'w')

	arcErrores.write('%15s%10s\n' % ('Linea de Error', 'Simbolo'))
	arcSimbolos.write('%30s%20s%25s\n' % ('Componente Lexico', 'Lexema', 'Valor'))
	
	numLinea = 1
	texto = arcEntrada.read()
	while len(texto) > 0:
		char = texto[0]
		token = reconocerToken(texto)
		
		if char == '\n':
			numLinea += 1
			
		lexema = texto[0: token[1]]
		texto = texto[token[1]: len(texto)]
		
		if token[0] != 'N':
			arcSimbolos.write('%30s%20s%25s\n' % (componenteLexico(token[0], lexema), lexema, valorLexema(lexema)))
		elif not esEspacio(char):
			arcErrores.write('%15s%10s\n' % (str(numLinea), char))
	
	arcErrores.close()
	arcSimbolos.close()

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print('No se ha especificado archivo de entrada')
	elif len(sys.argv) < 3:
		print('No se ha especificado archivo de resultados')
	elif len(sys.argv) < 4:
		print('No se ha especificado archivo de errores')
	else:
		main(sys.argv[1], sys.argv[2], sys.argv[3])