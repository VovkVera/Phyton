import inspect
import functools

def tag(name_tag):

    def content(msg):
        return f'<{name_tag}>{msg}</{name_tag}>'
    return content


h1 = tag("h1")
h2 = tag("h2")

print(h1("Header h1"))
print(h2("Header h2"))
print(inspect.getclosurevars(h1))
print(inspect.getclosurevars(h2))



def tag(name_tag, msg):
    print(f'<{name_tag}>{msg}</{name_tag}>')

# h1 = tag('h1')
# h2 = tag('h2')
h1 = functools.partial(tag, name_tag='h1')
h2 = functools.partial(tag, name_tag='h2')

print(h1, h2)

h1(msg='Hello')
h2(msg='World')
