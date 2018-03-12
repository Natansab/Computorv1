#!/usr/bin/python

user_input = raw_input('Entrez une equation de niveau 2 : ')
coeff = []

def find_coeff(equation):
      (\+|\-|.*?) *?([\d|\.]+\d|\d) *?\* *?[X|x] *?\^(\d)
