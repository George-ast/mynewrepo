"""old_text."""

symbol1 = 'ø'
symbol2 = 'å'
symbol3 = 'Æ'

t2 = ('Automatisering akselererer, {0}syeblikket da roboter'
    'vil erobre planeten v{1} ({2})').format(symbol1, symbol2, symbol3)
print(t2)

t3 = (f'Automatisering akselererer, {symbol1}syeblikket da roboter'
    f'vil erobre planeten v{symbol2} ({symbol3})')
print(t3)
if t2 == t3:
    print('success')