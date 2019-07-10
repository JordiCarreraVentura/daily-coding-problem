
# Problem #250

> This problem was asked by Google.
> 
> A cryptarithmetic puzzle is a mathematical game where the digits of some numbers are represented by letters. Each letter represents a unique digit.
>
> For example, a puzzle of the form:

```  
  SEND
+ MORE
--------
 MONEY```

>
> may have the solution:

```{'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O', 0, 'R': 8, 'Y': 2}```

> Given a three-word puzzle like the one above, create an algorithm that finds a solution.


# General remarks

* Multiple solutions are acceptable. In cases where the hypothesis does not lead to any conflicts, _3 + 4 = 7_ is an acceptable soltuion, and so is _4 + 3 = 7_.

* Every letter must map to a different number, and only one. E.g. each letter can be assigned a number chosen at random from the pool of the unique numbers observed. That number must then be removed from assignment for any other letters.

* Every pair of letters at the top sums to some other number, and that's the letter at the bottom. Some sums may carry one.

* Start with a single digit for simplicity and convenience, then add more digits to the problem.


# Solution

## Initialization
First, we declare any dependencies and initialize a few constants:


```python
import random
import re

PROBLEM_PARSER = re.compile('([A-Z]+)[^A-Z]*([A-Z]+)[^A-Z]*([A-Z]+)')

LETTERS = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(' ')
```

## Sample problem generation

Next, we create a function to generate a random problem according to the directions in the problem statement:


```python
def digit_to_crypt(encrypt, digits):
    return ''.join([encrypt[digit] for digit in digits])


def make_problem_text(digits_n1, digits_n2, summed, encrypt):
    crypt11 = digit_to_crypt(encrypt, digits_n1)
    crypt12 = digit_to_crypt(encrypt, digits_n2)
    crypt2 = digit_to_crypt(encrypt, summed)
    max_len = max([len(crypt11), len(crypt12), len(crypt2)])
    template = """
        %%%ds
        %%%ds
        %%s
        %%%ds
    """ % (max_len, max_len, max_len)
    
    return template % (
        crypt11,
        crypt12,
        '-' * max_len,
        crypt2
    )
    
    

def new_problem(len_n1, len_n2):
    digits_n1, digits_n2, digit_vocab = '', '', set([])

    while len(digits_n1) < len_n1:
        digit = str(random.randrange(0, 10))
        digits_n1 += digit
        digit_vocab.add(digit)
        
    while len(digits_n2) < len_n2:
        digit = str(random.randrange(0, 10))
        digits_n2 += digit
        digit_vocab.add(digit)
        
    summed = str(int(digits_n1) + int(digits_n2))
    digit_vocab.update(summed)
    
    used_vocab = random.sample(LETTERS, len(digit_vocab))
    encrypt = dict([])
    for digit in digit_vocab:
        encrypt[digit] = used_vocab.pop(0)
    
    problem_text = make_problem_text(digits_n1, digits_n2, summed, encrypt)
    
    return problem_text, encrypt, (digits_n1, digits_n2, summed)
```

We take a look at the output of the previous function to make sure everything makes sense:


```python
text, encrypt, (n1, n2, n12) = new_problem(3, 3)

print(text)

print(encrypt)
```

    
             SUW
             VYR
            ----
            ZRRW
        
    {'3': 'Y', '5': 'V', '0': 'R', '4': 'S', '8': 'W', '1': 'Z', '7': 'U'}


## Implement solver

The main function `f` below takes a problem (in text format) and an encryption key (only for convenience, it is not used during solving) and produces a decryption hypothesis. The hypothesis may or may not match the exact values used in the encryption key, but it will be arithmetically compatible with the problem statement, and therefore a valid solution.

Helper function `parse_problem_text` simply extracts the words from the problem's text (so, the numbers after undergoing encryption).

Function `try_solve` evaluates every candidate hypothesis. The three first arguments (`n1, n2` and `summed`) are constant and are the values extracted by `parse_problem_text` -they are simply used as the reference to evaluate the validity of a given hypothesis against. The important argument is `key`, which stores each candidate hypothesis (only one in every call). In each hypothesis, every letter observed in the input problem is assigned a digit at random. Given that hypothesis, this function then tries to solve mathematically the operation expressed in the problem. Upon success, it returns the key and a `True` value.


```python
def parse_problem_text(problem_text):
    match = PROBLEM_PARSER.search(problem_text)
    n1 = match.group(1)
    n2 = match.group(2)
    summed = match.group(3)
    return n1, n2, summed


def try_solve(n1, n2, summed, key):
    
    def decrypt(n, key):
        return ''.join([key[letter] for letter in n])
    
    d1 = decrypt(n1, key)
    d2 = decrypt(n2, key)
    d3 = decrypt(summed, key)
    if len(str(int(d3))) == len(summed) \
    and int(d1) + int(d2) == int(d3):
        return True, (d1, d2, d3)
    return False, (d1, d2, d3)


def f(problem_text, encrypt):
    decrypt = dict([])
    digit_vocab = encrypt.keys()
    letters = encrypt.values()

    n1, n2, summed = parse_problem_text(problem_text)
    _n1, _n2, _summed = None, None, None

    while True:
        space = [digit for digit in random.sample(digit_vocab, len(digit_vocab))]
        key = {
            letter: space.pop(0) for letter in letters
        }
        solved, (_n1, _n2, _summed) = try_solve(n1, n2, summed, key)
        if solved:
            decrypt = key
            break

    return decrypt, (_n1, _n2, _summed)


decrypt, (_n1, _n2, _n12) = f(text, encrypt)
print('Original values: %s + %s = %s' % (n1, n2, n12))
print('Proposed values: %s + %s = %s' % (_n1, _n2, _n12))
print('Problem:', text)

reverse_decrypt = {val: key for key, val in decrypt.items()}
for number, letter in encrypt.items():
    print('encryption: %s = %s,  decryption: %s = %s' % 
          (letter, number, letter, decrypt[letter])
    )
```

    Original values: 478 + 530 = 1008
    Proposed values: 438 + 570 = 1008
    Problem: 
             SUW
             VYR
            ----
            ZRRW
        
    encryption: Y = 3,  decryption: Y = 7
    encryption: V = 5,  decryption: V = 5
    encryption: R = 0,  decryption: R = 0
    encryption: S = 4,  decryption: S = 4
    encryption: W = 8,  decryption: W = 8
    encryption: Z = 1,  decryption: Z = 1
    encryption: U = 7,  decryption: U = 3

