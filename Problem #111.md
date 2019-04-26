
# Problem #111

>This problem was asked by Google.
>
> Given a word W and a string S, find all starting indices in S which are anagrams of W.
>
> For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.


```python
import random

ALPHABET = list('abcdefghijklmnopqrstuvwxyz')

probs = [0.6, 0.3, 0.08, 0.02]

items_per_prob = len(ALPHABET) / len(probs)


def generate_letter_probability_distribution():
    scope = []
    _scope = []
    for letter in ALPHABET:
        _scope.append(letter)
        if len(_scope) == items_per_prob:
            scope.append((sum(probs[:len(scope) + 1]), _scope))
            _scope = []
    if len(scope) == len(probs):
        scope[-1] = (scope[-1][0], scope[-1][1] + _scope)
    else:
        scope.append((sum(probs[:len(scope) + 1]), _scope))
    return scope


def new_word(scope):
    
    def new_letter(scope):
        p = random.random()
        for i, (prob, letters) in enumerate(scope):
            #print ' ' * (i + 1), 1, p, prob, letters
            if prob > p:
                return random.choice(letters)
        return random.choice(letters)
    
    l = random.randrange(4, 18)
    letters = []
    while len(letters) < l:
        letter = new_letter(scope)
        letters.append(letter)
    return ''.join(letters)
    

scope = generate_letter_probability_distribution()
```


```python
space = [
    new_word(scope) for _ in range(100)
]

targets = []
while len(targets) < 100:
    w = random.choice(space)
    a, b = random.sample(list(range(len(w))), 2)
    if a < b:
        i, j = a, b
    else:
        i, j = b, a
    if j - i < 2:
        continue
    target = w[i:j]
    targets.append(target)
```


```python
def f(target, word):
    l_indexes = []
    r_indexes = []
    onset = 0

    rtarget = list(reversed(target))
    for i, char in enumerate(word):
        r_matches, l_matches = 0, 0

        for j, letter in enumerate(target):
            if i + j > len(word) - 1:
                r_matches = False
                break
#             print i, j, letter, word[i + j]
            if letter == word[i + j]:
                r_matches += 1
            if rtarget[j] == word[i + j]:
                l_matches += 1

        if r_matches == len(target):
            r_indexes.append(i)
        
        if l_matches == len(target):
            l_indexes.append(i)
    
    return sorted(set(l_indexes + r_indexes))


nnegatives = 0
for target in targets:
    indexes = []
    negatives = 0
    for word in space:
        indexes = f(target, word)
        if indexes:
            print '%15s%25s  ' % (target, word), indexes
        else:
            negatives += 1
    if negatives:
        nnegatives += 1

```

                flf        daeedifefeeflfnlf   [11]
                flf               dbajflffjh   [4]
                 ej             babljeqhdled   [4]
                 ej           ddechaktdejdcd   [9]
                 ej               jejgacflkc   [0, 1]
                 ej             ibjnqejcqcfc   [5]
                 ej              kchejddcefb   [3]
                 ej                 jjedidce   [1]
                 ej                  jejvcfe   [0, 1]
           dhedbhkc            dfdhedbhkcjle   [2]
             jaelka                fjaelkacl   [1]
                 da          gdbbadfodndehda   [4, 13]
                 da                eckdabdba   [3]
                 da                   dacjrb   [0]
                 da        daeedifefeeflfnlf   [0]
                 da                 ddbjkadi   [5]
                 da           kmfgbgaebcbcda   [12]
                 da        tmkjhieakckncdacr   [13]
                 da        bfpbjigdanaffgdgc   [7]
                 da               igdgdagclc   [4]
                 da               bfdaiealgf   [2]
                 da                    badel   [1]
                 da                 dbffladb   [5]
                 da              dagifcgebgi   [0]
                 da        dbgcdaefgbfbfkgie   [4]
                 da            fidbhegohfadc   [10]
             fdeffa         fdeffakekcqeglge   [0]
                blj             babljeqhdled   [2]
                 cc                  efkacce   [4]
                 cc         dcclghghffbtdhag   [1]
                 cc        leccdkabllceafafe   [2]
                 cc             bieenabccdeo   [7]
              fbflk                   fbflkd   [0]
               gddd            eggdddfjidjfj   [2]
                 ae                  aqaecbe   [2]
                 ae        daeedifefeeflfnlf   [1]
                 ae           kmfgbgaebcbcda   [6]
                 ae        leccdkabllceafafe   [11]
                 ae        tmkjhieakckncdacr   [6]
                 ae        caggfidlbgbfaedfe   [12]
                 ae               bfdaiealgf   [5]
                 ae                     aeef   [0]
                 ae                dlaegndri   [2]
                 ae        dbgcdaefgbfbfkgie   [5]
                 ae                fjaelkacl   [2]
                 ae         geaffcbmbgbfbfdd   [1]
                 ie             blkbdeiecbed   [5, 6]
                 ie                     biee   [1]
                 ie            deiackbomfdeh   [1]
                 ie        tmkjhieakckncdacr   [5]
                 ie               bfdaiealgf   [4]
                 ie         djiepedfhbbxrfle   [2]
                 ie                 gggueiak   [4]
                 ie        rdnalieecfhellfbj   [5]
                 ie        dbgcdaefgbfbfkgie   [15]
                 ie             bieenabccdeo   [1]
            deiackb            deiackbomfdeh   [0]
             eccdka        leccdkabllceafafe   [1]
             ddbjka                 ddbjkadi   [0]
          chaktdejd           ddechaktdejdcd   [3]
              elhfg                elhfgkhgg   [0]
               dbhk            dfdhedbhkcjle   [5]
              gbbjh             dqcagbbjhcbc   [4]
               coij                    coiji   [0]
                fad            fidbhegohfadc   [9]
              naffg        bfpbjigdanaffgdgc   [9]
               ebab               ebabdibufb   [0]
                fac          hhfacafhbffghfg   [2, 4]
                fac                    fcafe   [1]
            djieped         djiepedfhbbxrfle   [0]
             cfbdjl            cfbdjlilfcbnd   [0]
          dbhegohfa            fidbhegohfadc   [2]
             kchejd              kchejddcefb   [0]
                 na        concjhnakfedlkbfe   [6]
                 na        bfpbjigdanaffgdgc   [8, 9]
                 na        rdnalieecfhellfbj   [2]
                 na                eenaikcgl   [2]
                 na             bieenabccdeo   [4]
        kmfgbgaebcb           kmfgbgaebcbcda   [0]
                 eb         akbjkbefjdgeqegj   [5]
                 eb                  aqaecbe   [5]
                 eb           cacdgjkipfbbec   [11]
                 eb             blkbdeiecbed   [9]
                 eb           kmfgbgaebcbcda   [7]
                 eb                  kjnjbec   [4]
                 eb             ebfdjvjafgef   [0]
                 eb               ebabdibufb   [0]
                 eb              dagifcgebgi   [7]
                 eb              xgkrebfcpll   [4]
                 eb                    fkebq   [2]
                bko                 bkolemhe   [0]
               bflk                   fbflkd   [1]
                 co                    coiji   [0]
                 co        concjhnakfedlkbfe   [0]
                 co                 chcoqigi   [2]
                 fk                  efkacce   [1]
                 fk             edfkbafflidn   [2]
                 fk                   ighfkc   [3]
                 fk        concjhnakfedlkbfe   [8]
                 fk        dbgcdaefgbfbfkgie   [12]
                 fk             jdcipdlcdkfg   [9]
                 fk                 dicqcfkk   [5]
                 fk                    fkebq   [0]
                 fk             dcjgbafkblaa   [6]
                 fk               llkffdfkeh   [2, 6]
              bbxrf         djiepedfhbbxrfle   [9]
             cjgbaf             dcjgbafkblaa   [1]
          hkkcucfdh             pfhkkcucfdhb   [2]
                bad          gdbbadfodndehda   [3]
                bad                eckdabdba   [3]
                bad                    badel   [0]
             iackbo            deiackbomfdeh   [2]
                dgd               igdgdagclc   [2]
               hrrf           hdmajigfhrrfjg   [8]
               fcaf                    fcafe   [0]
                fke                    fkebq   [0]
                fke               llkffdfkeh   [6]
            fgbfbfk        dbgcdaefgbfbfkgie   [7]
                efk                  efkacce   [0]
                efk        concjhnakfedlkbfe   [8]
                 fl                dgralbflb   [6]
                 fl        daeedifefeeflfnlf   [11, 12, 15]
                 fl               jejgacflkc   [6]
                 fl             edfkbafflidn   [7]
                 fl                   lfafqf   [0]
                 fl                   fbflkd   [2]
                 fl                   aolfff   [2]
                 fl                 dbffladb   [3]
                 fl         djiepedfhbbxrfle   [13]
                 fl               dbajflffjh   [4, 5]
                 fl            cfbdjlilfcbnd   [7]
                 fl        rdnalieecfhellfbj   [13]
               ajbc                  ajbcgbp   [0]
           caggfidl        caggfidlbgbfaedfe   [0]
           igdgdagc               igdgdagclc   [0]
            bajflff               dbajflffjh   [1]
                 kg            ywefhbdgkcpdi   [7]
                 kg                elhfgkhgg   [4]
                 kg        dbgcdaefgbfbfkgie   [13]
                 kg              xgkrebfcpll   [1]
                 eg         akbjkbefjdgeqegj   [10, 13]
                 eg             ebfdjvjafgef   [9]
                 eg         fdeffakekcqeglge   [11, 14]
                 eg            eggdddfjidjfj   [0]
                 eg                dlaegndri   [3]
                 eg              dagifcgebgi   [6]
                 eg            fidbhegohfadc   [5]
                 eg         geaffcbmbgbfbfdd   [0]
             enaikc                eenaikcgl   [1]
                 fa                   nfafhm   [1, 2]
                 fa          hhfacafhbffghfg   [2, 5]
                 fa             edfkbafflidn   [5]
                 fa                   lfafqf   [1, 2]
                 fa                    fcafe   [2]
                 fa        leccdkabllceafafe   [12, 13, 14]
                 fa             ebfdjvjafgef   [7]
                 fa        caggfidlbgbfaedfe   [11]
                 fa        bfpbjigdanaffgdgc   [10]
                 fa         fdeffakekcqeglge   [4]
                 fa            fidbhegohfadc   [9]
                 fa              kefbgfaggbw   [5]
                 fa             dcjgbafkblaa   [5]
                 fa         geaffcbmbgbfbfdd   [2]
               dagc               igdgdagclc   [4]
               aelk                fjaelkacl   [2]
         fgddbhhckb        bfdbbfgddbhhckbke   [5]
          igdgdagcl               igdgdagclc   [0]
               ffla                 dbffladb   [2]
                njb                  kjnjbec   [2]
                njb             ibjnqejcqcfc   [1]
                 af                   nfafhm   [1, 2]
                 af          hhfacafhbffghfg   [2, 5]
                 af             edfkbafflidn   [5]
                 af                   lfafqf   [1, 2]
                 af                    fcafe   [2]
                 af        leccdkabllceafafe   [12, 13, 14]
                 af             ebfdjvjafgef   [7]
                 af        caggfidlbgbfaedfe   [11]
                 af        bfpbjigdanaffgdgc   [10]
                 af         fdeffakekcqeglge   [4]
                 af            fidbhegohfadc   [9]
                 af              kefbgfaggbw   [5]
                 af             dcjgbafkblaa   [5]
                 af         geaffcbmbgbfbfdd   [2]
                 rr           hdmajigfhrrfjg   [9]
                 hf                   nfafhm   [3]
                 hf            ywefhbdgkcpdi   [3]
                 hf          hhfacafhbffghfg   [1, 6, 12]
                 hf         dcclghghffbtdhag   [7]
                 hf                   ighfkc   [2]
                 hf             pfhkkcucfdhb   [1]
                 hf         djiepedfhbbxrfle   [7]
                 hf           hdmajigfhrrfjg   [7]
                 hf        rdnalieecfhellfbj   [9]
                 hf                elhfgkhgg   [2]
                 hf            fidbhegohfadc   [8]
           gdgdagcl               igdgdagclc   [1]
                 bk         akbjkbefjdgeqegj   [1, 4]
                 bk             edfkbafflidn   [3]
                 bk             blkbdeiecbed   [2]
                 bk            deiackbomfdeh   [5]
                 bk                kbchbjrkd   [0]
                 bk        concjhnakfedlkbfe   [13]
                 bk                 bkolemhe   [0]
                 bk        bfdbbfgddbhhckbke   [13, 14]
                 bk             dcjgbafkblaa   [7]
           dlaegndr                dlaegndri   [0]
              faggb              kefbgfaggbw   [5]
                dab          gdbbadfodndehda   [3]
                dab                eckdabdba   [3]
                dab                    badel   [0]
             epdkiq               dknepdkiqc   [3]
           aigbaibd               aaigbaibdj   [1]
           bajflffj               dbajflffjh   [1]
               bfda               bfdaiealgf   [0]
                 cb                  aqaecbe   [4]
                 cb              bcgchdbbcll   [0, 7]
                 cb             blkbdeiecbed   [8]
                 cb           kmfgbgaebcbcda   [8, 9, 10]
                 cb                kbchbjrkd   [1]
                 cb                  ajbcgbp   [2]
                 cb            ecbcakdcilecl   [1, 2]
                 cb                 cbolgcfc   [0]
                 cb            cfbdjlilfcbnd   [9]
                 cb             bieenabccdeo   [6]
                 cb             dqcagbbjhcbc   [9, 10]
                 cb                 lolecbgc   [4]
                 cb         geaffcbmbgbfbfdd   [5]
            djlilfc            cfbdjlilfcbnd   [3]
                 aj                     ffja   [2]
                 aj                  ajbcgbp   [0]
                 aj             ebfdjvjafgef   [6]
                 aj               dbajflffjh   [2]
                 aj           hdmajigfhrrfjg   [3]
                 aj                fjaelkacl   [1]
               oncj        concjhnakfedlkbfe   [1]
          cjgbafkbl             dcjgbafkblaa   [1]
               cgeb              dagifcgebgi   [5]
             eetbac                 deetbacn   [1]
                jwj                jrdjwjhbf   [3]
                jvj             ebfdjvjafgef   [4]
              efkac                  efkacce   [0]
               lecb                 lolecbgc   [2]
               bflk                   fbflkd   [1]
              ajflf               dbajflffjh   [2]
          dechaktde           ddechaktdejdcd   [1]
                jib                     jibd   [0]
               rrfj           hdmajigfhrrfjg   [9]
         ibjnqejcqc             ibjnqejcqcfc   [0]
                coq                 chcoqigi   [2]
              jhnak        concjhnakfedlkbfe   [4]
         ibjnqejcqc             ibjnqejcqcfc   [0]
            hdmajig           hdmajigfhrrfjg   [0]
                 nf                   nfafhm   [0]
                 nf        daeedifefeeflfnlf   [13]
                 fa                   nfafhm   [1, 2]
                 fa          hhfacafhbffghfg   [2, 5]
                 fa             edfkbafflidn   [5]
                 fa                   lfafqf   [1, 2]
                 fa                    fcafe   [2]
                 fa        leccdkabllceafafe   [12, 13, 14]
                 fa             ebfdjvjafgef   [7]
                 fa        caggfidlbgbfaedfe   [11]
                 fa        bfpbjigdanaffgdgc   [10]
                 fa         fdeffakekcqeglge   [4]
                 fa            fidbhegohfadc   [9]
                 fa              kefbgfaggbw   [5]
                 fa             dcjgbafkblaa   [5]
                 fa         geaffcbmbgbfbfdd   [2]
            cacdgjk           cacdgjkipfbbec   [0]
          dqcagbbjh             dqcagbbjhcbc   [0]
                 lk               jejgacflkc   [7]
                 lk             blkbdeiecbed   [1]
                 lk                   fbflkd   [3]
                 lk        concjhnakfedlkbfe   [12]
                 lk                   eelkhd   [2]
                 lk                fjaelkacl   [4]
                 lk               llkffdfkeh   [1]
                 qi                 chcoqigi   [4]
                 qi               dknepdkiqc   [7]

