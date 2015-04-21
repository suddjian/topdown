from controls import *


def test():
    kb = KeyBinding()
    assert len(kb._bindings) == 0
    print("BINDING A LAMBDA...")
    kb.bind(2, lambda: print("lambda params"))
    kb.call(2)
    print("BINDING MULTIPLE...")
    kb.bind(42, lambda: print("multiple"))
    kb.bind(42, lambda: print("bindings"))
    kb.call(42)
    print("PRINTING DATA STRUCTURE...")
    print(kb._bindings)
    print("CALLING A RANGE...")
    for k in range(50):
        kb.call(k)
    assert len(kb._bindings) == 2

if __name__ = "__main__":
    test()
