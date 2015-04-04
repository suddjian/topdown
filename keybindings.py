
class KeyBinding:

    def __init__(self):
        self._bindings = {}

    ### maps a function to a key. The function must take a key as a parameter.
    ### Whenever the key is pressed, the function will be called.
    def bind(self, key, function):
        # create a new list of functions bound to a key if there aren't any
        # functions bound to it yet
        if key in self._bindings:
            self._bindings[key].append(function)
        else:
            self._bindings[key] = [function]

    ### calls any functions mapped to the given keys
    def call(self, key):
        bindlist = self._bindings.get(key, [])
        for f in bindlist:
            f()
