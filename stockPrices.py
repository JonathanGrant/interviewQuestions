def getMaxStockSale(stockPrices):
	if len(stockPrices) < 2:
		return 0
	maxSale = stockPrices[1] - stockPrices[0]
	minStockPrice = stockPrices[0]
	for stockPrice in stockPrices[1:]:
		if stockPrice < minStockPrice:
			minStockPrice = stockPrice
		elif stockPrice - minStockPrice > maxSale:
			maxSale = stockPrice - minStockPrice
	return maxSale


googleStock = [-1, -2, -3, -4, -5]
print getMaxStockSale(googleStock)