#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import argparse
import string
from alberti import Alberti

class VigenereCifer(Alberti):
    def __init__(self,key,plain):
        alfabeto = string.ascii_uppercase
        alfabeto = alfabeto[:14]+"Ñ"+alfabeto[14:]
        super(VigenereCifer,self).__init__(alfabeto,key,plain)

parser = argparse.ArgumentParser()
parser.add_argument("key", help="La clave del cifrado vigenere")
parser.add_argument("--descifer",help="Descifrar",action="store_true")
parser.add_argument("texto", help="El nombre del texto a cifrar")


if __name__ == '__main__':
    args = parser.parse_args()

    v = VigenereCifer(args.key,args.texto)
    if not args.descifer:
        v.cifer()
    else:
        v.descifer()
