"""
저녁식대 계산 모듈
"""

TAX_RATE = 0.0675
TIP_RATE = 0.15

dinner_fee = 150.32
dinner_fee_with_tax = (dinner_fee * TAX_RATE) + dinner_fee;
total_dinner_fee = dinner_fee_with_tax + (dinner_fee_with_tax * TIP_RATE)

print(total_dinner_fee)
