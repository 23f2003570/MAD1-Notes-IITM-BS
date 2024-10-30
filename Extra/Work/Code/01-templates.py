from string import Template

b = dict(who='Tim')
s = Template('$who likes $what').safe_substitute(b)

print (s)

s = Template('$who likes $what').substitute(b)

print (s)