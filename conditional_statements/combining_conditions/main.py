# The item's discount and stock status have been defined
discounted = False
lowStock = True
# discounted or low stock
movingProduct = discounted or lowStock

promotion = not discounted and not lowStock
print(movingProduct)
print(promotion)
print("Is the item eligible for promotion?", promotion)