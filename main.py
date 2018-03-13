#!/usr/bin/python
import re
import sys

user_input = input('Entrez une equation de niveau 2 : ')

def find_coeff(equation):
    coeff = [0, 0, 0]
    matches = re.findall('(\+|\-|.*?) *?([\d|\.]+\d|\d) *?\* *?[X|x] *?\^(\d)', equation)
    right_side = 1
    for match in matches:
        neg = 1
        if (match[0].strip() == '='):
            right_side = -1
        if (match[0].strip() == '-'):
            neg = -1
        exp = int(match[2])

        coeff[exp] = coeff[exp] + neg * right_side * float(match[1])
    print (coeff)
    return coeff

def reduced_form(coefficients):
    pwr = 0
    reduced = ''
    for coeff in coefficients:
        if (coeff > 0 and reduced != ''):
            reduced = reduced + ' + '
        if (coeff < 0):
            reduced = reduced + ' - '
            coeff = -1 * coeff
        if (coeff != 0):
            reduced = reduced + str(coeff) + ' * X^' + str(pwr)
        pwr = pwr + 1
    reduced = reduced + ' = 0'
    return reduced

def find_solutions(coeff, discriminant):
    if (coeff[2] != 0):
        if (discriminant == 0):
            return [-coeff[1] / (2 * coeff[2])]
        if (discriminant > 0):
            return [
                (-coeff[1] + discriminant**(1/2)) / (2 * coeff[2]),
                (-coeff[1] - discriminant**(1/2)) / (2 * coeff[2])
                ]
        else:
            return [
                (-coeff[1] + j(-discriminant)**(1/2)) / (2 * coeff[2]),
                (-coeff[1] - j(-discriminant)**(1/2)) / (2 * coeff[2])
                ]
    elif (coeff[1] != 0):
        return [-coeff[0] / coeff[1]]

coefficients = find_coeff(user_input)
discriminant = coefficients[1] * coefficients[1] - 4 * coefficients[0] * coefficients[2]
if (coefficients[2]):
    degree = 2
elif (coefficients[1]):
    degree = 1
print('Reduced form: ', end='', flush=True)
print(reduced_form(coefficients))
print('Polynomial degree: ', end='', flush=True)
print(degree)
solutions = find_solutions(coefficients, discriminant)
if (degree == 2):
    if (discriminant > 0):
        print('Discriminant is strictly positive, the two solutions are:')
        print(solutions[0])
        print(solutions[1])
    if (discriminant == 0):
        print('Discriminant is zero, the solution is:')
        print(solutions[0])
elif (degree == 1):
        print(solutions[0])
