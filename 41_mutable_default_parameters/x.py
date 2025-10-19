def create_multipliers():
    multipliers = []

    for i in range(5):
        def multiplier(x, i=i):
            return i * x
        multipliers.append(multiplier)

    return multipliers

funcs = create_multipliers()
for idx, func in enumerate(funcs):
    print(f"Funzione {idx}: func(10) = {func(1)}")