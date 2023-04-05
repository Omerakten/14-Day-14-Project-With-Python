# Currency exchange rate calculator
baseCurrencyName = input("Please enter the base currency name: ")
convertCurrencyName = input("Please enter the currency name to convert: ")
print("{} to {}".format(baseCurrencyName, convertCurrencyName))

baseCurrencyRate = float(input("Please enter the {} currency rate: ".format(baseCurrencyName)))
convertAmount = float(input("Please enter the {} amount to convert: ".format(convertCurrencyName)))

result = convertAmount / baseCurrencyRate

if result.is_integer():
  print(f"Base currency rate {baseCurrencyRate} Convert amount {int(convertAmount)} : Converted amount {int(result)} {baseCurrencyName}")
else:
  print(f"Base currency rate {baseCurrencyRate} Convert amount {convertAmount} : Converted amount {result:.3f} {baseCurrencyName}")
