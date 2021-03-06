3. Build-in Contants (内置常数)
 

A small number of constants live in the built-in namespace, They are:

内置的命名空间中有少量常数(constants), 它们是:


- False  bool type


- True  bool type

- None  NoneType type

>The sole value of the type NoneType. None is frequently used to represent the absence of a value, as when default arguments are not passed to a function

- NotImplemented  

>Special value which should be returned by the binary special methods (e.g. __eq__(), __lt__(), __add__(), __rsub__(), etc.) to indicate that the operation is not implemented with respect to the other type; may be returned by the in-place binary special methods (e.g. __imul__(), __iand__(), etc.) for the same purpose. Its truth value is true.

Ellipsis

>The same as .... Special value used mostly in conjunction with extended slicing syntax for user-defined container data types.

__debug__

>This constant is true if Python was not started with an -O option

```bash
The names None, False, True and __debug__ cannot be reassigned (assignments to them, even as an attribute name, raise SyntaxError), so they can be considered "true" constants.
```

3.1 Constants added by the site module

The site module (which is imported automatically during startup, except if the -S command-line option is given) adds several constants to the built-in namespace. They are useful for the interactive interpreter shell and should not be used in programs.

quit(code=None)
exit(code=None)
Objects that when printed, print a message like “Use quit() or Ctrl-D (i.e. EOF) to exit”, and when called, raise SystemExit with the specified exit code.

copyright
license
credits
Objects that when printed, print a message like “Type license() to see the full license text”, and when called, display the corresponding text in a pager-like fashion (one screen at a time).


