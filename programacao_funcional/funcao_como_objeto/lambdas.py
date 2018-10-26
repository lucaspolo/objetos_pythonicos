from dis import dis


dobro = lambda x: x * 2

print(dis(dobro.__code__.co_code))  # Como podemos ver, o código assembly da função é o mesmo.

print(dobro.__name__)  # Funções lambda possuem sempre o mesmo nome '<lambda>'

# Não é a melhor prática usar lambdas, pois a falta de nome dificulta o entendimento do código.
