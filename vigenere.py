#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import argparse
import pprint
import string
from vigenere_cifer import VigenereCifer

NUMERO_LLAVES = 3
pp = pprint.PrettyPrinter(indent=4)
parser = argparse.ArgumentParser()
parser.add_argument("text", help="El texto que usaremos para decifrar")

if __name__ == '__main__':
    args = parser.parse_args()
    with open(args.text,"r") as cifer_text:
        v = VigenereCifer("","")
        cifer_text = cifer_text.read()
        CIFER_LENGTH = len(cifer_text)
        bloques= {}
        for t in range(1,CIFER_LENGTH):
            bloque_t = "".join([cifer_text[i] for i in range(CIFER_LENGTH) if i%t == 0 and cifer_text[i] in v.alphabet])
            frecuencias = { x: 0 for x in v.alphabet}
            for letter in bloque_t:
                frecuencias[letter]+=1
            for key in frecuencias:
                frecuencias[key] = frecuencias[key]/len(bloque_t)
            bloques[t] = sum([q**2 for q in frecuencias.values()])
        llaves_frecuencia = { x:bloques[x] for x in bloques if bloques[x] <= 0.0741}
        llaves_escogidas = []
        for i in range(NUMERO_LLAVES):
            llaves_escogidas.append(max(llaves_frecuencia, key=llaves_frecuencia.get))
            llaves_frecuencia.pop(llaves_escogidas[-1],None)

        for key_length in llaves_escogidas:
            bloques = []
            for bloque in range(1,key_length):
                bloques.append("".join([cifer_text[i] for i in range(CIFER_LENGTH) if i%bloque == 0 and cifer_text[i] in v.alphabet]))
            pp.pprint(bloques)
