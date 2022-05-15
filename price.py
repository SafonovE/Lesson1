'''def descounted(price, discount, max_discount = 20):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount > 100:
        raise ValueError ('Максимальная скидка не должна быть больше 100')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    return(price_with_discount)



product = {'name': 'Samsung Galaxy S21', 'price': 50000.0, 'discount': 5}
product['with_discount'] = descounted(product['price'], product['discount'])
print(product)

print(descounted(100,5))
print(descounted(100,50))
print(descounted(100,50, max_discount=60))'''

'''Задание 2'''
def format_price(price):
    price = abs(int(price))
    return(f'Цена:' + str(price) + ' ' + 'руб.')
price = format_price(56.24)
print(price)
