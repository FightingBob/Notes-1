# 字典推导

CODES = [(86, 'China'), (1, 'US')]

country_code = {country: code for country, code in CODES}
print(country_code)
# 182
