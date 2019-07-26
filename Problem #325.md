
# Problem #325

> This problem was asked by Jane Street.
>
> The United States uses the imperial system of weights and measures, which means that there are many different, seemingly arbitrary units to measure distance. There are 12 inches in a foot, 3 feet in a yard, 22 yards in a chain, and so on.
>
> Create a data structure that can efficiently convert a certain quantity of one unit to the correct amount of any other unit. You should also allow for additional units to be added to the system.


```python
INCHES_IN_FOOT = 12
FEET_IN_YARD = 3
YARDS_IN_CHAIN = 22
CHAINS_IN_FURLONG = 10
FURLONGS_IN_MILE = 8
MILES_IN_LEAGUE = 3


class Unit:
    name = ''
    inches = 0
    
    def __str__(self):
        return '<Unit name="%s" inches=%d>' % (
            self.name, self.inches
        )

    def __call__(self, n, unit, remainder=False):
        src_inches = self.inches * n
        if not remainder:
            return src_inches / unit.inches
        else:
            return (src_inches % unit.inches) / self.inches
    
    def __le__(self, unit):
        if self.inches <= unit.inches:
            return True
        return False



class Inch(Unit):
    name = 'in'
    inches = 1

class Foot(Inch):
    name = 'ft'
    def __init__(self):
        Inch.__init__(self)
        self.inches *= INCHES_IN_FOOT

class Yard(Foot):
    name = 'yd'
    def __init__(self):
        Foot.__init__(self)
        self.inches *= FEET_IN_YARD

class Chain(Yard):
    name = 'ch'
    def __init__(self):
        Yard.__init__(self)
        self.inches *= YARDS_IN_CHAIN

class Furlong(Chain):
    name = 'fur'
    def __init__(self):
        Chain.__init__(self)
        self.inches *= CHAINS_IN_FURLONG
    
class Mile(Furlong):
    name = 'mi'
    def __init__(self):
        Furlong.__init__(self)
        self.inches *= FURLONGS_IN_MILE

class League(Mile):
    name = 'lea'
    def __init__(self):
        Mile.__init__(self)
        self.inches *= MILES_IN_LEAGUE




class MeasureConverter:

    def __init__(self, units):
        self.units = units

    def __call__(self, n, u_from, u_to, discrete=False):
        src = self[u_from]
        tgt = self[u_to]
        if not discrete:
            return src(n, tgt)
        else:
            applicable_units = sorted(
                [u for u in self.units if u <= tgt],
                key=lambda x: x.inches,
                reverse=True
            )
            history = []
            curr = n
            while applicable_units:
                u = applicable_units.pop(0)
                converted = src(curr, u)
                summand = (int(converted), u.name)
                curr = src(curr, u, remainder=True)
                history.append(summand)
            return history
    
    def __getitem__(self, unit):
        if isinstance(unit, str):
            for u in self.units:
                if u.name == unit:
                    return u
        return unit
```


```python
_in = Inch()
ft = Foot()
yd = Yard()
ch = Chain()
fur = Furlong()
mi = Mile()
lea = League()

tests = [
    (1, 'mi', 'in'),
    (1, mi, _in),
    (1, mi, 'in'),
    (1, 'in', 'mi'),
    (0.1, 'mi', 'in'),
    (785, 'ft', 'yd'),
    (785, ft, yd),
    (785, 'ft', 'yd'),
    (44194, 'ch', 'mi'),
    (655817.233, 'yd', 'lea'),
    (655817, 'yd', 'lea')
]

units = [_in, ft, yd, ch, fur, mi, lea]

mc = MeasureConverter(units)
for n, u_from, u_to in tests:
    print(n, u_from, u_to, mc(n, u_from, u_to))
    print(n, u_from, u_to, mc(n, u_from, u_to, discrete=True))
    print()
```

    1 mi in 63360.0
    1 mi in [(63360, 'in')]
    
    1 <Unit name="mi" inches=63360> <Unit name="in" inches=1> 63360.0
    1 <Unit name="mi" inches=63360> <Unit name="in" inches=1> [(63360, 'in')]
    
    1 <Unit name="mi" inches=63360> in 63360.0
    1 <Unit name="mi" inches=63360> in [(63360, 'in')]
    
    1 in mi 1.5782828282828283e-05
    1 in mi [(0, 'mi'), (0, 'fur'), (0, 'ch'), (0, 'yd'), (0, 'ft'), (1, 'in')]
    
    0.1 mi in 6336.0
    0.1 mi in [(6336, 'in')]
    
    785 ft yd 261.6666666666667
    785 ft yd [(261, 'yd'), (2, 'ft'), (0, 'in')]
    
    785 <Unit name="ft" inches=12> <Unit name="yd" inches=36> 261.6666666666667
    785 <Unit name="ft" inches=12> <Unit name="yd" inches=36> [(261, 'yd'), (2, 'ft'), (0, 'in')]
    
    785 ft yd 261.6666666666667
    785 ft yd [(261, 'yd'), (2, 'ft'), (0, 'in')]
    
    44194 ch mi 552.425
    44194 ch mi [(552, 'mi'), (3, 'fur'), (4, 'ch'), (0, 'yd'), (0, 'ft'), (0, 'in')]
    
    655817.233 yd lea 124.20780928030304
    655817.233 yd lea [(124, 'lea'), (0, 'mi'), (4, 'fur'), (9, 'ch'), (19, 'yd'), (0, 'ft'), (8, 'in')]
    
    655817 yd lea 124.20776515151515
    655817 yd lea [(124, 'lea'), (0, 'mi'), (4, 'fur'), (9, 'ch'), (19, 'yd'), (0, 'ft'), (0, 'in')]
    

