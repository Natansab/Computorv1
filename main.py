#!/usr/bin/python
import re
import sys

def find_coefficients(equation):
    coeff = [0, 0, 0]
    matches = re.findall('([-+=]?)\s*([\d\.]+)?(\s*\*?\s*[xX](?:\s*\^\s*(\d+))?)?\s*', equation)
    right_side = 1
    exp = -1
    for match in matches:
        neg = 1
        print(match)
        if (match[0].strip() == '='):
            right_side = -1
        if (match[0].strip() == '-'):
            neg = -1
        if (match[3]):
            exp = int(match[3])
        elif(match[3] == '' and match[2] != ''):
            exp = 1
        elif (match[1] != '' and match[2] == ''):
            exp = 0
        print(right_side)
        print(neg)
        print(exp)
        if (exp > -1 and match[1] == '' and match[2] != ''):
                coeff[exp] = coeff[exp] + right_side
                exp = -1
        elif (exp > -1 and match[1] != ''):
                coeff[exp] = coeff[exp] + neg * right_side * float(match[1])
                exp = -1
        print(coeff)
    # print(coeff)
    return coeff

def print_reduced_form(coefficients):
    pwr = 0
    reduced = ''
    for coeff in coefficients:
        if (coeff > 0 and reduced != ''):
            reduced = reduced + ' + '
        if (coeff < 0):
            reduced = reduced + ' - '
            coeff = -1 * coeff
        if (coeff != 0 and pwr == 0):
            reduced = reduced + str(coeff)
        elif (coeff != 0):
            reduced = reduced + str(coeff) + ' * X^' + str(pwr)
        pwr = pwr + 1
    if (coefficients[0] == 0 and coefficients[1] == 0 and coefficients[2] == 0):
        reduced = '0'
    reduced = reduced + ' = 0'
    print(reduced)

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
                (-coeff[1] + 1j * (-discriminant)**(1/2)) / (2 * coeff[2]),
                (-coeff[1] - 1j * (-discriminant)**(1/2)) / (2 * coeff[2])
                ]
    elif (coeff[1] != 0):
        return [-coeff[0] / coeff[1]]

def find_degree(coefficients):
    if (coefficients[2]):
        return 2
    elif (coefficients[1]):
        return 1
    return 0


def print_solutions(solutions, degree, discriminant, coefficients):
    if (degree == 2):
        if (discriminant > 0):
            print('Discriminant is strictly positive, the two solutions are:')
            print(solutions[0])
            print(solutions[1])
        if (discriminant < 0):
            print('Discriminant is strictly negative, the two complexe solutions are:')
            print(solutions[0])
            print(solutions[1])
        if (discriminant == 0):
            print('Discriminant is zero, the solution is:')
            print(solutions[0])
    elif (degree == 1):
            print(solutions[0])
    elif (degree == 0):
        if(coefficients[0] == 0):
            print('Solution toujours vraie')
        else:
            print('Il n\'y a pas de solution')


def main():
    user_input = input('Entrez une equation de niveau 2 : ')
    error = re.findall('([^\d^ x.*=X+]|\^ *?[3456789])', user_input)
    if(error):
        print('Error, can\'t solve or format error')
    else:
        coefficients = find_coefficients(user_input)
        discriminant = coefficients[1] * coefficients[1] - 4 * coefficients[0] * coefficients[2]
        degree = find_degree(coefficients)
        print('Reduced form: ', end='', flush=True)
        print_reduced_form(coefficients)
        print('Polynomial degree: ', end='', flush=True)
        print(degree)
        solutions = find_solutions(coefficients, discriminant)
        print_solutions(solutions, degree, discriminant, coefficients)

main()
