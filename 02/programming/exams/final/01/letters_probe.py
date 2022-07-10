# cmu 15-122

from letters import First

from letters import Second

alpha1 = First("miraculously")  # First's constructor takes	variable of	arguments
assert alpha1.consonants == [
    "m",
    "r",
    "c",
    "l",
    "s",
    "l",
]  # consonants are in the original order
assert alpha1.vowels == [
    "i",
    "a",
    "u",
    "o",
    "u",
    "y",
]  # but vowels are in the original order
assert (
    str(First("miraculous"))
    == "First(consonants=['m', 'r', 'c', 'l', 's'], vowels=['i', 'a', 'u', 'o', 'u'])"
)

# Two First's are equal if their consonants are equal.
assert First("myricyl") == First("miracle")
assert First("miraculously") != First("miraculous")
assert First("miraculously") != "don't	crash	here!"

# clear_vowels and cleared_vowels are different methods (one is	destructive)
alpha2 = First("miraculous")
alpha2.clear_vowels()
assert str(alpha2) == "First(consonants=['m', 'r', 'c', 'l', 's'], vowels=[])"
alpha3 = First("miraculous")
alpha4 = alpha3.cleared_vowels()
assert isinstance(alpha4, First)
assert (
    str(alpha3)
    == "First(consonants=['m', 'r', 'c', 'l', 's'], vowels=['i', 'a', 'u', 'o', 'u'])"
)
assert str(alpha4) == "First(consonants=['m', 'r', 'c', 'l', 's'], vowels=[])"

s = []
assert First("myricyl") not in s
s.append(First("myricyl"))
assert First("myricyl") in s
assert First("miracle") in s

beta1 = Second("miracle", 5)  # creates	an First with 5 as shift
assert isinstance(beta1, First)
assert (
    str(beta1) == "First(consonants=['m', 'r', 'c', 'l'], vowels=['i', 'a', 'e'])"
)  # use __class__, __bases__, __name__ attribute

# only Second's object can call encoder:
beta2 = beta1.encoder()  # so	instead	of 'miracle' it's now "rnwfhqj" by shift using
assert str(beta2) == "First(consonants=['r', 'w', 'h', 'q', 'n', 'f', 'j'], vowels=[])"
# encoding consonants then vowels
assert isinstance(beta2, Second)

crashed = False
try:
    alpha = First("abc").encoder()
except:
    crashed = True
    assert crashed == True

print("Passed!")
