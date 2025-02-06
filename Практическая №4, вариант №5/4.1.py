# 1 У гусей и кроликов вместе 64 лапы. Сколько может быть кроликов и сколько гусей (указать все возможные сочетания)?
# Григорьев Максим Денисович

total_legs = 64

for gys in range(total_legs // 2 + 1):
    kroliki = (total_legs - 2 * gys) // 4
    if 2 * gys + 4 * kroliki == total_legs:
        print(f"Гусей: {gys}, Кроликов: {kroliki}")
