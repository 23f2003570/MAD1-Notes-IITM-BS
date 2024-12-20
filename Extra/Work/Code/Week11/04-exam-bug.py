import sys
from jinja2 import Template

vars = sys.argv

print (vars[0])

course_technologies = {'python': 'backend', 'javascript': 'frontend'}
template = Template('This course focusses on {{technology}} development')

if len(vars) > 2 and vars[2] in course_technologies:
    course = vars[1]
    technology = course_technologies[course]
    print (template.render(technology=technology))
else:
    print ("Please specify a valid course name")