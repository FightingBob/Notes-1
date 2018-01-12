1. Introduction

The “Python library” contains several different kinds of components.



It contains data types that would normally be considered part of the “core” of a language, such as numbers and lists. For these types, the Python language core defines the form of literals and places some constraints on their semantics, but does not fully define the semantics. (On the other hand, the language core does define syntactic properties like the spelling and priorities of operators.)

The library also contains built-in functions and exceptions — objects that can be used by all Python code without the need of an import statement. Some of these are defined by the core language, but many are not essential for the core semantics and are only described here.

The bulk of the library, however, consists of a collection of modules. There are many ways to dissect this collection. Some modules are written in C and built in to the Python interpreter; others are written in Python and imported in source form. Some modules provide interfaces that are highly specific to Python, like printing a stack trace; some provide interfaces that are specific to particular operating systems, such as access to specific hardware; others provide interfaces that are specific to a particular application domain, like the World Wide Web. Some modules are available in all versions and ports of Python; others are only available when the underlying system supports or requires them; yet others are available only when a particular configuration option was chosen at the time when Python was compiled and installed.

This manual is organized “from the inside out:” it first describes the built-in functions, data types and exceptions, and finally the modules, grouped in chapters of related modules.

This means that if you start reading this manual from the start, and skip to the next chapter when you get bored, you will get a reasonable overview of the available modules and application areas that are supported by the Python library. Of course, you don’t have to read it like a novel — you can also browse the table of contents (in front of the manual), or look for a specific function, module or term in the index (in the back). And finally, if you enjoy learning about random subjects, you choose a random page number (see module random) and read a section or two. Regardless of the order in which you read the sections of this manual, it helps to start with chapter Built-in Functions, as the remainder of the manual assumes familiarity with this material.

Let the show begin!


# tarnslation

1. 介绍

python 标准库包含(contains) 几个(several) 不同的 组件(commponents)

它包含通常被认为是这门语言核心(core)的一部分数据类型, 就像数字类型(numbers) 和 列表(lists).对于这些类型,python语言的核心定义为文字的形式(the form of literals)和对它的语法设置了一些约束, 但是并没有完全定义语法(semantics). {在另一方面,语言的核心定义了 语法特征 (syntactic properties) 比如 操作符优先 和拼写属性 }

这个标准库还包含(contains) 内建函数和例子--对象可以使用所有的python代码, 不需要导入语句, 其中一些是由核心语言定义的,但是大多数不是核心语句所必须的(essential)这里仅仅是描述.

标准库的大部分, 是由一组模块组成的. 有许多方法去剖析这个集合(collection), 一些模块是使用C语言编写的,内置于python 解释器(interpreter), 其他的模块是使用python写的,并使用python源代码的形式(form)导入. 一些模块提供对python非常特殊的接口, 比如 prining a stack trace,  一些提供特定于操作系统的接口(interface), 比如 访问特定的硬件, 其他的提供特定于应用程序的接口, 像万维网一样(World Wide Web),Python的所有版本和端口都有一些模块可以用, 其他的仅仅在底层系统支持或需要时才可以用