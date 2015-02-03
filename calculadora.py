#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) != 4:
    print
    sys.exit("No se puede realizar la operacion, recuerde: operacion numero1 numero2")   

operacion = sys.argv[1]
operando1 = sys.argv[2]
operando2 = sys.argv[3]

def suma(term1, term2):
    return float(term1) + float(term2)
    
def resta(term1, term2):
    return float(term1) - float(term2)

def multiplica(term1, term2):
    return float(term1) * float(term2)

def divide(term1, term2):
    return float(term1) / float(term2)


if __name__ == "__main__":
    
    if operacion == "suma":
        try:
            print str(suma(operando1, operando2))
        except ValueError:
            print "Introduzca dos numeros por favor"
    elif operacion == "resta":
        try:
            print str(resta(operando1, operando2))
        except ValueError:
            print "Introduzca dos numeros por favor"
    elif operacion == "multiplica":
        try:
            print str(multiplica(operando1, operando2))
        except ValueError:
            print "Introduzca dos numeros por favor"
    elif operacion == "divide":
        try:
            print str(divide(operando1, operando2))
        except ZeroDivisionError:
			print 'Error al dividir, no se puede dividir entre 0'
        except ValueError:
            print "Introduzca dos numeros por favor"
    else:
        print "Las operaciones disponibles son: suma resta multiplica divide." 
