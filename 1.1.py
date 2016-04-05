# Unpacking a Sequence into Separate Variables
p = (4, 5)
x, y = p

data = ['ACME', 50, 91.4, (2012, 12, 21)]
name, shares, price, date = data

x, y, z = p
# ValueError: not enough values to unpack (expected 3, got 2)

# Unpack assign works on string and more
s = 'Hello'
a, b, c, d, e = s

# use _ to take the position, then drop it.
data = ['ACME', 50, 91.4, (2012, 12, 21)]
_, shares, price, _ = data