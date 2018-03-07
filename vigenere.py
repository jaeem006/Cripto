#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import unittest

from vigenere_cifer import VigenereCifer

VIGENERE = VigenereCifer()
ALPHABET = VIGENERE.alphabet
CONSTANT_DISTRIBUTION = 0.0741

def create_block(text,i,t):
    clean_text = "".join([x for x in text if x in ALPHABET])
    return "".join([clean_text[i+x] for x in range(len(clean_text)-i) if x%t ==0])

def frec(block):
    f = { x : 0 for x in ALPHABET}
    for i in block:
        f[i]+=1
    for x in f:
        f[x] = f[x]/len(block)
    return f

def square_frec(block):
    frec_ = frec(block)
    return sum([frec_[x]**2 for x in frec_])

def calc_key_length(cifer_text):
    with open(cifer_text) as cifer:
        cifer = cifer.read()
        cifer = "".join([x for x in cifer if x in ALPHABET])

    conjunto_frec= []

    for i in range(len("ANITCONSTITUCIONALMENTE")):
        dict_frec = {}
        for t in range(1,len("ANITCONSTITUCIONALMENTE")):
            dict_frec[t] = square_frec(create_block(cifer,i,t))
        dict_frec = { k:v for k,v in dict_frec.items() if v <= 0.0841 and v >= 0.0641}
        conjunto_frec.append(dict_frec)

    porcentaje_clave = {k:v for d in conjunto_frec for k,v in d.items()}
    return [x for x in porcentaje_clave.keys()]

# def llaves(cifer_text,keys_length):
#     llave = {}
#     for length in keys_length:
#         llave[length] = {}
#         for i in range(length):
#             block = create_block(cifer_text,i,length)
#             frecuencias_letras = {}
#             for i in ALPHABET:
#                 block = "".join([VIGENERE.get_plain_text(x,ALPHABET[i]) for x in block])
#                 frecuencias_letras[ALPHABET[i]] = square_frec(block)
#             dict_frec = { k:v for k,v in frecuencias_letras.items() if v <= 0.0841 and v >= 0.0641}
#             llave[length][i] = dict_frec.keys()
#     print(llave)

# 
#       TEST CODE
# 
class BlockTest(unittest.TestCase):
    texto = "ESTE.ES.UN TEXTO ALGO SENCILLO"
    def test_blocks(self):
        self.assertEqual(create_block(self.texto,0,2),"ETEUTXOLOECLO")
        self.assertEqual(create_block(self.texto,1,2),"SESNETAGSNIL")

    def test_frecuency(self):
        x = sum([ x for x in frec(create_block(self.texto,0,2)).values()])
        self.assertAlmostEqual(x,1)
        self.assertGreaterEqual(x,0.999)

    def test_square_frec(self):
        self.assertIsNotNone(square_frec(create_block(self.texto,0,2)), msg="No debe ser nulo")

    def test_calc_key_length(self):
        self.assertIn(9,calc_key_length("JUANRULFO_cifrado.txt"))
        self.assertIn(8,calc_key_length("SALANDER_cifrado.txt"))

if __name__ == '__main__':
    unittest.main()
