from scipy.optimize import linprog

# Coeficientes da função objetivo (maximizar lucro, então usamos coeficientes negativos)
c = [-4, -1]  # Lucro por unidade de mouse e teclado

# Coeficientes das restrições (horas disponíveis)
A = [
    [9, 1],  # Restrição de mão de obra
    [3, 1]   # Restrição da linha de produção
]

# Limites das restrições
b = [18, 12]  # Total de horas disponíveis

# Limites das variáveis (quantidades não podem ser negativas)
x_bounds = [(0, None), (0, None)]

# Resolver o problema de otimização
res = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

# Exibir resultados
if res.success:
    x1, x2 = res.x
    lucro_total = -res.fun  # Como a função objetivo foi multiplicada por -1, invertemos o sinal
    print(f"Quantidade de mouses a serem fabricados: {int(x1)}")
    print(f"Quantidade de teclados a serem fabricados: {int(x2)}")
    print(f"Lucro total máximo: R$ {lucro_total:.2f}".replace('.',','))  
    # Substituir '.' por ',' para o padrão brasileiro

else:
    print("O problema não tem solução viável.")
