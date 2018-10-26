from dis import dis


def dobro(x):
    return x * 2


# Irá imprimir os atributos da função
for p in dir(dobro):
    print(p)


print(dobro.__name__)  # Retorna o nome da função
print(dobro.__module__)  # Módulo da função
print(dobro.__code__)  # Informações relativas ao código da função

print(dobro.__code__.co_code)  # Bytecode gerado para VM do Python
print(dis(dobro.__code__.co_code))  # Irá "disassemblar" a função, deixando-a legível

dobro.n = 2  # Atribuição dinamica, como qualquer objeto

g = dobro  # Cria uma referência a função dobro

print(g(10))
