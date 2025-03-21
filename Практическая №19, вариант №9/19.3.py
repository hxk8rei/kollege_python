def compute_sum(x, n):
    if n < 1 or not isinstance(n, int):
        raise ValueError("n должно быть натуральным числом")
    
    S = 0
    for k in range(1, n + 1):
        exponent = k ** 2
        S += x ** exponent
    return S

x = 2.0 
n = 3   
try:
    result = compute_sum(x, n)
    print(f"S = {result}")
except ValueError as e:
    print(f"Ошибка: {e}")