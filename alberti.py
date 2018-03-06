#!/usr/bin/python3
# -*- encoding: utf-8 -*-

class Alberti(object):
    """Generalizacion del cifrado de Vigenere"""
    def __init__(self,alphabet,key,plain):
        self.alphabet = alphabet
        self.key = key
        self.plain = plain

    def get_cifer_letter(self,letter,key):
        try:
            alphabet = self.alphabet
            letter = alphabet.index(letter)
            key = alphabet.index(key)
            return (alphabet[key:]+alphabet[:key])[letter]
        except Exception as e:
            return letter

    def get_plain_letter(self,letter,key):
        try:
            alphabet = self.alphabet
            key = alphabet.index(key)
            alphabet = alphabet[key:]+alphabet[:key]
            letter = alphabet.index(letter)
            return self.alphabet[letter]
        except Exception as e:
            return letter

    def recorrer(self,func):
        i = 0
        key_length = len(self.key)
        with open(self.plain,"r") as plain:
            while True:
                c = plain.read(1)
                if not c:
                    break
                print(func(c,self.key[i%key_length]),end="")
                i += 1

    def cifer(self):
        return self.recorrer(self.get_cifer_letter)

    def descifer(self):
        return self.recorrer(self.get_plain_letter)
