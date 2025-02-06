total_legs = 64

for gys in range(total_legs // 2 + 1):
    kroliki = (total_legs - 2 * gys) // 4
    if 2 * gys + 4 * kroliki == total_legs:
        print(f"Гусей: {gys}, Кроликов: {kroliki}")