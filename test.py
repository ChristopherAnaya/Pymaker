def multiply(expr1, expr2):
    def parse(expr):
        if 'x' in expr:
            if '^' in expr:
                coef, power = expr.split('x^')
            else:
                coef, power = expr[:-1], 1 
            return int(coef) if coef else 1, int(power)  
        return int(expr), 0 

    coef1, power1 = parse(expr1)
    print(coef1, power1)
    coef2, power2 = parse(expr2)
    print(coef2, power2)
    
    print(f"{coef1 * coef2}x^{power1 + power2}" if power1 + power2 else str(coef1 * coef2))

multiply("3x^2", "2")
