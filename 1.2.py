# Unpacking Elements from Iterables of Arbitrary Length

def avg(num):
    return sum(num)/float(len(num))


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

avg_n = drop_first_last((10, 7, 6, 3, 0))
print(avg_n)


# phone_numbers always is list, even the count is zero.
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(phone_numbers)

# prefixing * also works
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing, current)

# use to string operation
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

# unpack and drop
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name, year)


# use * unpack to implement recursive function, just for demo
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum((1, 2, 3, 4, 5)))