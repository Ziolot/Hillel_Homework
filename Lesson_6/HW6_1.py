def lists_concentration(coin, code):
    my_dict = dict(zip(coin, code))
    return my_dict


print(lists_concentration(('Bitcoin', 'Ether', 'Ripple', 'Litecoin'),
                          ('BTC', 'ETH', 'XRP', 'LTC')))
