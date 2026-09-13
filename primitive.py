print("================================")

count = 100
count_type = type(count)

print(f"the count: {count}, type: {count_type}")

result1 = count.bit_count()
result2 = count.numerator
print(f"bit count: {result1}, numerator: {result2}")
