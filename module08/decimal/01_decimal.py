from decimal import Decimal, ROUND_HALF_EVEN, ROUND_HALF_UP

num = Decimal(1.45)

+ - * /

print(num.quantize(Decimal('1.0'), rounding=ROUND_HALF_EVEN))

num = Decimal('1.45')
print(num.quantize(Decimal('1.0'), rounding=ROUND_HALF_UP))

print(Decimal('3.14159').quantize((Decimal('1.000'))))