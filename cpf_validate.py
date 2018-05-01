'''Escreva um código em Python para validar CPFs.  Procure o algoritmo de validação pelo Google.
Assuma que o CPF a ser validado consiste de uma string com dígitos e possíveis caracteres de separação (por exemplo, "." ou "-").
Se não houver 11 dígitos, considere o CPF inválido.  Se houver mais de 15 caracteres na string também considere o CPF inválido.
A validação do CPF deve consistir apenas da validação dos 2 dígitos verificadores.'''

cpf_input = input('Digite o número do CPF: ')
numero = [int(x) for x in cpf_input if x.isnumeric()]
first = str((sum([(10-i)*y for i,y in enumerate(numero[:9])]) *10) %11)
second = str((sum([(11-a)*z for a,z in enumerate(numero[:10])]) *10) %11)
print(int(first[-1]) == numero[-2] and int(second[-1]) == numero[-1] and len(cpf_input) < 15 and len(numero) == 11)

'''
O código recebe qualquer forma de entrada de um número de CPF, seja como os exemplos apresentados abaixo ou variações.
099.599.274-66
099.599.274/66
09959927466
099.599.278-90

A lista 'numero' é uma lista composta apenas dos números do CPF digitado, independente se foi usado algum tipo de separador ou não.

'first' e 'second' recebem valores a partir do algoritmo utilizado para validar um determinado CPF 
são strings e na comparação é pego o último dígito de cada um, dessa forma, se o resultado tiver apenas unidade, esse será o valor
utilizado, e para o caso de ter dezena e unidade, é pego apenas a unidade. Isso resolve o problema de quando um dos valores é igual
a 10, já que quando for igual a 10 deve-se considerar como 0.
(https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/)
 


Por fim, é retornado 'True' se todas as condições do algoritmo e do enunciado da atividade são respeitadas, caso contrário
é retornado 'False'
'''