a = 5


def f(a=3):
    b = 3  # Não transborda o escopo para global

    print(globals())  # Escopo global
    print(locals())  # Escopo local
    print(a)  # Irá buscar no escopo local


print("Irá imprimir dados relativos a classe A")


class A:
    a = 8 #Disponível apenas no escopo da classe

    print(a)
    print(globals())
    print(locals())


print("Irá imprimir dados relativos a função f: ")
f()
