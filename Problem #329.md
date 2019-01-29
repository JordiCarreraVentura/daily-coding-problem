
# Problem #329

> This problem was asked by Amazon.
> 
> The stable marriage problem is defined as follows:
> 
> Suppose you have N men and N women, and each person has ranked their prospective opposite-sex partners in order of preference.
> 
> For example, if N = 3, the input could be something like this:
> 


```python
guy_preferences = {
    'andrew': ['caroline', 'abigail', 'betty'],
    'bill': ['caroline', 'betty', 'abigail'],
    'chester': ['betty', 'caroline', 'abigail'],
}

gal_preferences = {
    'abigail': ['andrew', 'bill', 'chester'],
    'betty': ['bill', 'andrew', 'chester'],
    'caroline': ['bill', 'chester', 'andrew']
}
```

> Write an algorithm that pairs the men and women together in such a way that no two people of opposite sex would both rather be with each other than with their current partners.


```python
guys = sorted(guy_preferences.keys())
gals = sorted(gal_preferences.keys())

couples = []
for guy in guys:
    for girl in gals:
        couple = sorted(tuple([guy, girl]))
        if couple not in couples:
            couples.append(couple)

# print sorted(couples, key=lambda x: tuple(x)[0])
# [['abigail', 'andrew'], ['abigail', 'bill'], ['abigail', 'chester'], ['andrew', 'betty'], ['andrew', 'caroline'], ['betty', 'bill'], ['betty', 'chester'], ['bill', 'caroline'], ['caroline', 'chester']]


def check_for_divorce_risk(somebody, partner):
    # True = guy, False = girl
    gender = True if somebody in guys else False
    preferences = guy_preferences if gender else gal_preferences
    secnereferp = gal_preferences if gender else guy_preferences
    favs = preferences[somebody]
    svaf = secnereferp[partner]
    
    current_partner_rank = favs.index(partner)
    kanr_rentrap_tnerruc = svaf.index(somebody)
    alt_partners = [someone for someone in favs if favs.index(someone) < current_partner_rank]
    
    if not alt_partners:
        return False

    for alt_partner in alt_partners:
        this_partner_rank = secnereferp[alt_partner].index(somebody)
        if this_partner_rank < kanr_rentrap_tnerruc:
            return True
    
    return False


for a, b in couples:
    # if 'a' is the guy and 'b' is the girl
    # -get rank for a's current partner -> r_curr
    # -for every other girl 'g', get a's preference for 'g' if higher than a's -> r_alts
    # -for each girl r_alt in r_alts
    #  > get r_alt's rank for 'a' and r_alt's rank for her current partner;
    #  > if the latter is higher than the former, it's a divorce.
    
    if check_for_divorce_risk(a, b):
        print 'Divorce:', (a, b)
    else:
        print 'Stay married:', (a, b)

```

    Stay married: ('abigail', 'andrew')
    Divorce: ('andrew', 'betty')
    Stay married: ('andrew', 'caroline')
    Divorce: ('abigail', 'bill')
    Stay married: ('betty', 'bill')
    Stay married: ('bill', 'caroline')
    Divorce: ('abigail', 'chester')
    Stay married: ('betty', 'chester')
    Divorce: ('caroline', 'chester')

