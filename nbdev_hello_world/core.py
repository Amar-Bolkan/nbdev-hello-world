"""Fill in a module description here"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/core_utils.ipynb.

# %% auto 0
__all__ = ['foo', 'second_foo_same_cell', 'add', 'say_hello']

# %% ../nbs/core_utils.ipynb 3
def foo(): pass

#| export
def second_foo_same_cell(): pass

# %% ../nbs/core_utils.ipynb 4
def add(a,b): 
    "Returns a + b" 
    return a + b

# %% ../nbs/core_utils.ipynb 5
def say_hello(to):
    "Say hello to somebody"
    return f"Hello {to}!"

assert say_hello("Amar") == "Hello Amar!"
