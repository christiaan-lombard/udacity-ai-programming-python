import math

some_dict = {'a': 1}
some_list = [1,2,3]
x = 100

try:
    print(some_dict['e'])
    pass
except Exception as e:
    print('Undefined dict item access raised: %s' % type(e))

try:
    assert x != 100
    pass
except Exception as e:
    print('Failed assertion raised: %s' % type(e))

try:
    x = some_list[4]
    pass
except Exception as e:
    print('Index out of range raised: %s' % type(e))

try:
    x = int("ad23.5")
    pass
except Exception as e:
    print('Bad argument value raised: %s' % type(e))

try:
    print(math.sqrt('fu'))
    pass
except Exception as e:
    print('Bad argument type raised: %s' % type(e))

