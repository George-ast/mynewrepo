"""String formatting.

we have norway text in old style formatting
re-write the same text as:
1 string with format() call
2 f-string
use linter(https://github.com/wemake-services/wemake-python-styleguide)
to check your new created python module for possible linter errors
try to run code from pycharm/command line

norway_text = 'Automatisering akselererer %syeblikket da roboter vil erobre planeten v%sr. (%s)' % ('ø', 'å', 'Æ')
print(norway_text).

"""

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