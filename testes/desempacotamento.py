# Função com muitos parâmetros
def funcao(parametro1, parametro2, parametro3, parametro4, parametro5, parametro6):
    print(parametro1, parametro2, parametro3)
    print(parametro4, parametro5, parametro6)

# Construindo parâmetros
parametros = {
    'parametro1': 1,
    'parametro2': 2,
    'parametro3': 3,
    'parametro4': 4,
    'parametro5': 5,
    'parametro6': 6,
}

# Chamando passando parâmetros desempacotados
funcao(**parametros)

# Criando parâmetros dinamicamente!
funcao(**{f"parametro{i}": i for i in range(1, 7)})
