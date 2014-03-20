dicc = dict('(': 'PARENTESIS-ABIERTO',
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
		'"': 'COMILLA-DOBLE')
		
def esSimboloEspecial(char):
	if dicc[char] is None:
		return False
	return True
	
def obtenSimboloEspecial(char):
	return dicc[char]