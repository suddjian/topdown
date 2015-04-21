
class KeyBinding:

    def __init__(self):
        self._bindings = {}

    def bind(self, key, function):
        """
        Maps a function to a key.
        Whenever the key is pressed, the function will be called.
        """

        # create a new list of functions bound to a key if there aren't any
        # functions bound to it yet
        if key in self._bindings:
            self._bindings[key].append(function)
        else:
            self._bindings[key] = [function]

    def call(self, key):
        """
        Calls any functions mapped to the given keys
        """
        bindlist = self._bindings.get(key, [])
        for f in bindlist:
            f()
