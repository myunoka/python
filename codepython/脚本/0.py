import re

xx = 'PythonPythonPython'
s = re.findall('(Python){1,2}', xx)
print(s)