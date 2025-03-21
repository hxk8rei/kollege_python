class Polynomial:
    def __init__(self, coeffs):
        while len(coeffs) > 1 and coeffs[-1] == 0:
            coeffs.pop()
        self.coeffs = coeffs

    def degree(self):
        return len(self.coeffs) - 1 if self.coeffs else -1

    def __add__(self, other):
        if self.degree() < other.degree():
            self, other = other, self
        result_coeffs = self.coeffs[:]
        for i in range(len(other.coeffs)):
            result_coeffs[i] += other.coeffs[i]
        return Polynomial(result_coeffs)

    def __sub__(self, other):
        result_coeffs = self.coeffs[:]
        for i in range(len(other.coeffs)):
            if i < len(result_coeffs):
                result_coeffs[i] -= other.coeffs[i]
            else:
                result_coeffs.append(-other.coeffs[i])
        return Polynomial(result_coeffs)

    def __mul__(self, other):
        result_coeffs = [0] * (self.degree() + other.degree() + 1)
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                result_coeffs[i + j] += self.coeffs[i] * other.coeffs[j]
        return Polynomial(result_coeffs)

    def __eq__(self, other):
        return self.coeffs == other.coeffs

    def __ne__(self, other):
        return not (self == other)

    def derivative(self):
        if self.degree() == 0:
            return Polynomial([0])
        result_coeffs = [i * self.coeffs[i] for i in range(1, len(self.coeffs))]
        return Polynomial(result_coeffs)

    def evaluate(self, x0):
        result = 0
        for coeff in reversed(self.coeffs):
            result = result * x0 + coeff
        return result

    def __pow__(self, k):
        if k < 0:
            raise ValueError("Степень должна быть неотрицательной")
        result = Polynomial([1])
        for _ in range(k):
            result *= self
        return result

    def divide(self, other):
        if other.degree() < 0 or not any(other.coeffs):
            raise ValueError("Деление на нулевой многочлен")
        dividend = self.coeffs[:]
        divisor = other.coeffs[:]
        quotient = [0] * (max(0, len(dividend) - len(divisor) + 1))
        while len(dividend) >= len(divisor):
            if dividend[-1] == 0:
                dividend.pop()
                continue
            factor = dividend[-1] / divisor[-1]
            degree_diff = len(dividend) - len(divisor)
            quotient[degree_diff] = factor
            for i in range(len(divisor)):
                dividend[degree_diff + i] -= factor * divisor[i]
            while len(dividend) > 0 and dividend[-1] == 0:
                dividend.pop()
        remainder = Polynomial(dividend if dividend else [0])
        quotient = Polynomial(quotient)
        return quotient, remainder

def gcd(p, q):
    while q.degree() >= 0 and any(q.coeffs):
        p, q = q, p.divide(q)[1]
    return p

def compute_expression(p, q, s, r):
    p_pow_s = p ** s
    q_pow_r = q ** r
    result = p_pow_s - q_pow_r
    return result

p = Polynomial([1, 2, 3])  
q = Polynomial([1, 1])     

print("Сложение:", (p + q).coeffs)            
print("Вычитание:", (p - q).coeffs)           
print("Умножение:", (p * q).coeffs)          
quotient, remainder = p.divide(q)
print("Деление:", quotient.coeffs, remainder.coeffs) 
print("Производная P:", p.derivative().coeffs)        
print("Значение P(1):", p.evaluate(1))               
print("P^2:", (p ** 2).coeffs)                        
print("НОД:", gcd(p, q).coeffs)                      


s, r = 2, 1
result = compute_expression(p, q, s, r)
print("P^2 - Q^1:", result.coeffs)                   