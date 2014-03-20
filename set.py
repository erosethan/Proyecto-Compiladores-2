selectivas = set(['if', 'else', 'switch', 'case'])
repetitivas = set(['for', 'while', 'do'])
tiposDatos = set(['void', 'int', 'float', 'double', 'char'])
calificadoresTipoDato = set(['short', 'long', 'signed', 'unsigned'])
preprocesador = set(['include', 'define', 'inline'])
Ireturn = set(['return'])
Imain = set(['main'])

def pruebaIdentificador(cadena):
	if cadena in selectivas
		return 'SELECTIVA'
	if cadena in repetitivas
		return 'REPETITIVA'
	if cadena in tiposDatos
		return 'TIPO DE DATO'
	if cadena in calificadoresTipoDato
		return 'CALIFICADOR DE TIPO DE DATO'
	if cadena in preprocesador
		return 'RETURN'
	if cadena in Ireturn
		return 'RETURN'
	if cadena in Imain
		return 'MAIN'
	return None