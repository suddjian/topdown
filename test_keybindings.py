from controls import *


kb = KeyBinding()

assert len(kb._bindings) == 0
print("BINDING A LAMBDA...")
kb.bind(2, function = lambda: print("lambda params"))
kb.call(2)
print("BINDING MULTIPLE...")
kb.bind(42, function = lambda: print("multiple"))
kb.bind(42, function = lambda: print("bindings"))
kb.call(42)
print("PRINTING DATA STRUCTURE...")
print(kb._bindings)
'''
for k in range(0, 50):
    bindlist = kb._bindings.get(k, [])
    for f in bindlist:
        f()
        '''
print("CALLING A RANGE...")
for k in range(50):
    kb.call(k)
assert len(kb._bindings) == 2
