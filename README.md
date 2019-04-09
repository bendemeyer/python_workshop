# How to Python

## Resources

Official Documentation:
* Home: https://docs.python.org/3/index.html
* Tutorial: https://docs.python.org/3/tutorial/index.html
* Language Reference: https://docs.python.org/3/reference/index.html
* Standard Library: https://docs.python.org/3/library/index.html

Python Wiki:
* Moving to Python from other languages: https://wiki.python.org/moin/MovingToPythonFromOtherLanguages

## Basics

### Hello World

```python
print("Hello World!")
```

OK, that was too easy. How about a basic greeting:

```python
def show_greeting(name):
    print(f"Hello {name}")

show_greeting("Monty")
```

Right, so what do we see here?

1. Significant whitespace

	* Python has no brackets or `END` constructs to tell the interpreter where a function definition or `if` statement ends. Instead it relies on indentation level to determine what aspect of the code a particular line belongs to. For example, if we change the above to:

		```python
		def show_greeting(name):
            print(f"Hello {name}")

            show_greeting("Monty")
		```
		We'll enter a never-ending recursive loop, as Python will interpret the call to `show_greeting` on the last line to be within the function definition.

	* Note that the indented line is indented using spaces. This is the de facto standard for Python, although tabs can be used for indentation as well. However use of tabs and spaces for indentation absolutely CAN NOT be mixed within one file. Python2 attempts to support this behavior (but you still shouldn't try it because it's a bug magnet) and Python3 outright rejects it and will throw an error if you even try.

1. String interpolation
	* Starting with version 3.6, Python introduced the idea of the "f-string", or formatted string literals. From the official documentation:

		> A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'. These strings may contain replacement fields, which are expressions delimited by curly braces {}. While other string literals always have a constant value, formatted strings are really expressions evaluated at run time.

	* Prior to Python 3.6, string fomatting was accomplished most commonly using the string method `format`. Although f-strings are generally preferred now, you may still encounter some code that looks like this:

		```python
		def show_greeting(name):
            print("Hello {name}".format(name=name))
		```

### Importing from other files

Let's say we have a directory that looks like this:

```
Project Directory
├── __init__.py
├── greeting.py
└── importer.py
```

Where `greeting.py` contains the function defined in the section above, and `importer.py` wants to make use of that function. In `importer.py`, we simply include the line:

```python
from greeting import show_greeting

show_greeting()
```

or

```python
import greeting

greeting.show_greeting()
```

And now the function `show_greeting` is available in the current script! And if we have a more complex directory structure, like:

```
Project Directory
├── sub_directory
│   ├── __init__.py
│   ├── something.py
│   └── messages.py
├── __init__.py
├── greeting.py
└── importer.py
```

Then we could import functions from `messages.py` with this:

```python
from sub_directory.messages import some_func

some_func()
```

or

```python
import sub_directory.messages

sub_directory.messages.some_func()
```

Now let's explore how that works in a little more depth:

1. How does Python know where to look for the file we're referencing?
	* When the Python executable first starts up, it makes a map of all modules in the current working directory and subdirectories. Any file with a `.py` extension, and any directory containing an `__init__.py` file will be treated as modules.

	* Modules are accessible via their file/directory name, and dots are used to access child modules. So a file at `some/python/sub/directory/file.py` would be accessed as `some.python.sub.directory.file`.

1. How does a file in a subdirectory access modules defined in a parent directory?
	* All module paths should be given relative to the current working directory of the Python executable. This means that as long as Python is run from the root project directory, all modules should be referenced relative to that root. Say `something.py` needs to import from `greeting.py` and `messages.py`. Even though it is in the same directory as `messages.py`, the imports would look like this:

		```python
		from greeting import show_greeting
		from sub_directory.messages import some_func
		```

	* This can make direct execution of files within submodules a little tricky. For example, trying to run:

		```bash
		$ python sub_directory/something.py
		```
	
		Will fail becuase it will try run with the file's directory (in this case, `sub_directory`) as the current working directory, which means that file will be unable to access modules from parent directories. If you need to run a file like this directly, it can be invoked as a module by using the `-m` flag on the command line:

		```bash
		$ python -m sub_directory.something
		```

1. What's the deal with all the `__init__.py` files?
	* `__init__.py` files are what Python uses to determine if a given directory should be added to its module map or not. If you don't include an `__init__.py` in a directory, no python files from that directory will be importable by anything outside of that directory. In most cases these files are completely empty, the file only needs to exist for Python to handle it.
	* There's some interesting stuff you can do by adding code to `__init__.py`, but that's beyond the scope of this introduction to Python. You can find more in-depth information on Python modules and how they work here: https://docs.python.org/3/tutorial/modules.html


### Environment Setup

Python projects are generally built within a virtual environment for the purpose of sandboxing installed packages that the project relies on. Python3 includes a utility for creating a virtual environment. The following command will create a virtual environment and put all the associated files into a directory called `python_env`:

```bash
$ python3 -m venv ./python_env
```

Once your virtual environment is created, you still need to activate it before you'll see its effect. The virtual environment directory contains an activation script which can be read in using the `source` bash command.

```bash
$ source ./python_env/bin/activate
```

Once that's done, your working environment will be altered in several ways:

1. Calls to `python` will reference the Python executable included in the virtual environment. Since we started this virtual environment with Python3, that will be the version of Python called by default. So there's no need to specify `python3` when working within a virtual environment.

1. Any packages installed with `pip` will install locally within the virual environment, and will be inaccessible to globally installed Python. Also, any packages installed globally will not me accessible within the virtual environment.

1. A command line tool called `deactivate` is made available to deactivate the virtual environment

### Package Installation

Python packages are installed with a utility called `pip`. Individual packages can be installed easily by running:

```bash
$ pip install package_name
```

You can see everything installed in your current environment by running:

```bash
$ pip freeze
```

The convention for tracking installed packages within a project is to output the content of a `pip freeze` into a file named `requirements.txt`.

```bash
$ pip freeze > requirements.txt
```

And to install all packages from an existing `requirements.txt` file, run:

```bash
$ pip install -r ./requirements.txt
```

### The Python Interactive Shell

To access the Python interactive shell, simply run `python` (or `python3`) from a command prompt. This will drop you into the Python shell, where you can run arbitrary code, import modules, test functions, etc. A shell launched while a virtual environment is active will have access to all the packages installed within that virual environment.

If you find yourself frequently using the Python shell, consider installing the pip package `bpython` in your environment. Once installed, running `bpython` will drop you into an improved Python shell, including features like better history preservation and code completion assistance.

## Language Features

### "Batteries Included"

Documentation: https://docs.python.org/3/library/index.html

One of the most fun aspects of Python is how much it can do out-of-the box. The Python standard library has some fairly advanced algorithm implementations and abstractions around common activities, things that in other languages often necessitate installing external packages. Some examples:

* Binary search

	https://docs.python.org/3/library/bisect.html

	```python
	>>> import bisect
	>>> values = [2,3,3,5,6,8,10,17,18]
	>>> bisect.bisect_left(values, 3)
	1
	>>> bisect.bisect_right(values, 3)
	3
	```

* Embedded SQLite database

	https://docs.python.org/3/library/sqlite3.html

	```python
	import sqlite3

	# Will create a DB file if it doesn't already exist
	conn = sqlite3.connect('/path/to/db/file.db')
	conn.execute('CREATE TABLE IF NOT EXISTS logs (source text, message text)')
	conn.execute("INSERT INTO logs VALUES ('myapp', 'It is working!')")
	```

* Reading/writing CSV files

	https://docs.python.org/3/library/csv.html

	```python
	import csv

	with open('comma_separated.csv', 'r') as comma_file:
	    with open('tab_separated.csv', 'w') as tab_file:
	        reader = csv.DictReader(comma_file)
	        writer = csv.DictWriter(tab_file, reader.fieldnames, delimiter='\t')
            writer.writeheader()
	        for row in reader:
	            row['edit_count'] = int(row['edit_count']) + 1
	            writer.writerow(row)
	```

### Unit Testing

Documentation: https://docs.python.org/3/library/unittest.html

Python has a fairly comprehensive unit testing framework bundled as part of its standard library. A simple unit test file will look something like this:

```python
import unittest
from modules.messages import get_welcome_message

class TestMessages(unittest.TestCase):
    def test_get_welcome_message(self):
        self.assertEqual(get_welcome_message('Monty'), "Welcome, Monty!")

if __name__ == '__main__':
    unittest.main()
```

There's a few important elements to the above code, so let's cover them:

* `class TestMessages(unittest.TestCase)`

	In Python syntax, this means define a new class named `TestMessages`, inheriting from the existing class `unittest.TestCase`. We'll cover more on class definitions and inheritence later, but for now it's enough to know that unit tests should be defined within a class that inherits from `unittest.TestCase`.

* `def test_get_welcome_message(self):`

	Also important is that all functions/methods that will act as test cases are named with the prefix `test_`. Python will look for this when running unit tests.

* `if __name__ == '__main__':`

	Python files can be simultaneously scripts to execute directly and modules to import elsewhere. When Python modules are imported, the importing file executes all the code in the file it is importing. Because of this, we need some way to specify that certain code should only be executed if it is being run directly, and that's what this `if` check does. This prevents the code within the `if` block from being executed every time this module is imported elsewhere.

* `unittest.main()`

	This is what actually runs the tests in this file when the file is executed.

With a test file ready, run:

```bash
$ python -m unittest path/to/file.py
```

To run the tests. Additionally, you can run the same command without specifying a file to have Python auto-discover all tests files and run them:

```bash
$ python -m unittest
```

For more complex unit testing, Python offers patching and mocking. Let's say we alter `get_welcome_message` so that it uses the `requests` package to pull a greeting string from an HTTP endpoint. To mock that HTTP request so our test doesn't rely on it, we'd do something like:

```python
import unittest
import json
from unittest.mock import patch, Mock
from modules.messages import get_welcome_message

class TestMessages(unittest.TestCase):
    @patch('modules.messages.requests')
    def test_get_welcome_message(self, mock_requests):
        mock_requests.get = Mock()
        mock_requests.get.return_value = json.dumps({
            'status':200,
            'message': 'Howdy-doo'
        })
        self.assertEqual(get_welcome_message('Monty'), "Howdy-doo, Monty!")

if __name__ == '__main__':
    unittest.main()
```

Again, let's go through some important points in detail:

* `@patch(...`

	This is a function decorator, which is essentially shorthand for a wrapper function. When a function with the `@patch` decorator is invoked, Python creates a new `Mock` object that will be returned anytime the code tries to access the module described in the string passed to `@patch`. That mock object will then be added on to the end of the arguments list of the function that is being decorated. That function can then manipulate the mock object however necessary to facilitate testing.

* `...'modules.messages.requests')`

	It's important to patch modules based on both their name _and_ their location. If the patch were to reference just `requests`, it would be patching that name in the current context. The full string above will patch the name `requests` only within the module `modules.messages`.

* `mock_requests.get = Mock()`

	Thanks to the `@patch`, `mock_requests` is already a mock object. But the code we're testing calls `requests.get`, which still needs to be mocked. We can do that by simply assigning a new `Mock` object to the `get` property of our existing mocked module

* `mock_requests.get.return_value = ...`

	Python mocks treat `return_value` as a special property. Once it's defined, if the mock object that it's defined on is called as a function, that function call will return the value assigned to `return_value`.

Multiple patches can be added to a single function. Note that Python decorators are applied inside-out, meaning the last decorator in the list is applied to the function first. This means that the order of arguments passed to the function by decorators is the opposite of how the decorators are listed.

```python
import unittest
import json
from unittest.mock import patch, Mock
from modules.messages import get_welcome_message

class TestMessages(unittest.TestCase):
    @patch('modules.messages.datetime.datetime')
    @patch('modules.messages.requests')
    def test_get_welcome_message(self, mock_requests, mock_datetime):
        mock_requests.get = Mock()
        mock_requests.get.return_value = json.dumps({
            'status':200,
            'message': 'Howdy-doo'
        })
        mock_datetime.now = Mock()
        mock_datetime.now.return_value = 5
        self.assertEqual(get_welcome_message('Monty'), "Howdy-doo, Monty! The current time is 5")

if __name__ == '__main__':
    unittest.main()
```

Patches can also be applied by a context manager as opposed to a decorator, and the patch can specify a custom object type to use (in place of the default `MagicMock`)

```python
import unittest
import json
from unittest.mock import patch, Mock
from modules.messages import get_welcome_message

class TestMessages(unittest.TestCase):
    def test_get_welcome_message(self, mock_requests, mock_datetime):
        with patch('modules.messages.datetime.datetime') as mock_datetime:
            with patch('modules.messages.requests', new=CustomMock) as mock_requets:
                mock_requests.get.return_value = json.dumps({
                    'status':200,
                    'message': 'Howdy-doo'
                })
                mock_datetime.now = Mock()
                mock_datetime.now.return_value = 5
                self.assertEqual(get_welcome_message('Monty'), "Howdy-doo, Monty! The current time is 5")

if __name__ == '__main__':
    unittest.main()
```

### Classes

Documentation: https://docs.python.org/3/tutorial/classes.html

Python has classes much like any other language. However unlike many other languages, classes are not essential for creating clean, maintainable code. Code can be neatly organized simply as a collection of functions/variables within a module, so before creating a class take a moment to consider if you really need the advantages that a class brings, like creating multiple object instances, or altering instance state across multiple method calls.

Let's look at a basic example class to demonstrate how Python classes behave:

```python
class Incrementor(object):
    class_attribute = "Set at class level"
    shared_attribute = "Set at class level"

    def __init__(self):
        self.instance_attribute = "Set at instance level"
        self.shared_attribute = "Set at instance level"
        self._value = 0

    def _add(self, number):
        self._value += number

    def increment(self):
        self._add(1)

    @classmethod
    def incrementor_factory(cls, value):
        instance = cls()
        instance._value = value
        return instance

    @staticmethod
    def instance_is_value(incrementor, value):
        return incrementor._value == value
```

* `class Incrementor(object):`

	This is the class definition and inheritance statement. This defines a class called `Incrementor`, and sets it to inherit from `object`. Inheriting from `object` was an important and necessary step in Python 2, and though it's no longer needed in Python 3 it remains a common pattern that you're likely to see.

	If we wanted to create a class to inherit from this `Incrementor` class, we would simply do:

	```python
	class ChildIncrementor(Incrementor):
	```

* `class_attribute = "Set at class level"`

	Notice that this attribute (and the one below it) is set _outside_ of a method, not bound to any instance of this class. This means we can access the value both directly from the class itself and also from individual instances.

	```python
	>>> from classmodule import Incrementor
	>>> Incrementor.class_atrribute
	"Set at class level"
	>>> i = Incrementor()
	>>> i.class_atrribute
	"Set at class level"
	```

	Further, we can alter the value of that attribute on a given instance without impacting its value on the class definition.

	```python
	>>> i = Incrementor()
	>>> i.class_attribute
	"Set at class level"
	>>> i.class_attribute = 7
	>>> i.class_attribute
	7
	>>> Incrementor.class_attribute
	"Set at class level"
	```

	Still further (and dangerously), we can alter the value of the attribute at the _class_ level, which will change the value of that attribute not just for future instances of that class, but also for any _past_ instances that have not already overriden the value at the instance level.

	```python
	>>> i = Incrementor()
	>>> i.class_attribute = 7
	>>> ii = Incrementor()
	>>> Incrementor.class_attribute = None
	>>> iii = Incrementor
	>>> i.class_attribute
	7
	>>> ii.class_attribute
	None
	>>> iii.class_attribute
	None
	```

* `def __init__(self):`

	This is the class's constructor. It, like all instance methods, takes at least one argument that is by convention named `self`. In Python, there is no special keyword like `this` that always refers to the current object instance. Instead, when an instance method is called in Python the instance that did the calling is automatically passed in as the first argument to that function. This makes for some very easy object composition, which we'll cover more later

* `self.instance_attribute = "Set at instance level"`

	This sets an instance attribute. Since an attribute of the same name is not defined at the class level, trying to access it direclty from the class will fail. Notice that there's nothing special here that defines `instance_attribute` as an acceptable attribute to add to this class. In Python, for the most part, you can add any arbirary attribute to an object.

* `self._value = 0`

	Python does not make a distinction between public and private membership in a class. All class members, be they functions or attributes, are publicly accessible. To designate an attribute or function as something that is not a supported part of the class's public API, by convention an underscore is prepended to the name.

	Because these members are "private", it is generally a bad idea to rely on any attribute or function named using this convention. Adding an underscore to the beginning of the name is a developer's way of saying "I don't recommend using this, here be dragons"

* `def _add(self, number):`

	A "private" method. Similar to the warning above, this function should not be considered reliable for external use.

	This also demonstrates what we see when a instance method needs to take an argument. Note that even though the function definition shows two arguments, only the first will be given when this function is invoked from an instance, as the instance itself will be supplied as the first argument:

	```python
	>>> i = Instance()
	>>> i._value
	0
	>>> i._add(7)
	7
	```

* `def increment(self):`

	A "public" method. Much the same as above, but should be considered a reliable part of the class's API. If you maintain a library used by other projects and you make a change to an existing "public" method that is not fully backward-compatible, you should consider this a breaking change in your library and do full major version upgrade with your next release.

* `@classmethod`

	A function decorator. This decorator tells Python that when the following function is called it shouldn't pass in the object instance it was called from, but rather a reference to the object's class itself. These methods can be called either directly from the class or from individual instances. They are often used as factories for the class, or something similar.

* `@staticmethod`

	Another decorator. This time the decorator tells Python not to supply anything for the first argument, the function will only receive arguments that are supplied explicitly. Static methods are generally utility methods that could be defined entirely outside of the class, but are included with it mostly for organization's sake.

### Object composition

As mentioned above, Python's lack of a `this` keyword makes object composition extremely straightforward. You can simply define a function that expects an object instance as its first argument, then apply that function to as many classes or objects as you like, farily similar to how you might use a trait in another language. Example:

```python
def print_class_name(obj):
	print(obj.__class__.__name__)

class Dummy():
	print_class_name = print_class_name
```

Allows:

```python
>>> d = Dummy()
>>> d.print_class_name()
'Dummy'
```

### Named and Default Arguments

Python allows for naming arguments, which can make function calls much easier to read. Rather than needing to remember the order in which arguments are passed, we only have to remember their names (or read them if we're looking at existing code). Supplying the argument's name is not required, and if names are supplied for all arguments their position ceases to matter. For example, given the function:

```python
def are_factors(factor_a, factor_b, target):
	return factor_a * factor_b == target
```

We can invoke it in a variety of ways:

```python
>>> are_factors(2, 5, 12)
False
>>> are_factors(3, 9, target=27)
True
>>> are_factors(factor_a=5, factor_b=25, target=125)
True
>>> are_factors(target=4, factor_b=8, factor_a=32)
False
```

Arguments can also have default values which will be used if no other value is provided. Given the function:

```python
def add_one(number=1):
	return number + 1
```

We can do the following:

```python
>>> add_one(5)
6
>>> add_one()
2
```

Keep in mind that any arguments that have default values must be the last arguments positionally in the function signature. Otherwise it would be impossible to make use of the default argument while supplying the rest of the arguments positionally, which is why Python will throw an error if you try to do otherwise.

**<span style="color:red">IMPORTANT! This might be the single most frustrating thing about Python! Read this before you start going crazy with default arguments!</span>**

One thing to beware in Python is supplying anything _mutable_ as a default argument value. The reason for this is Python will only interpret the function definition once, when it first encounters it. For any values supplied as defualts, it stores them in memory and, importantly, uses _the same object reference_ for each time the function is invoked. This is not a problem for non-mutable types since they will never be changed, however any changes made to a mutable default argument will be picked up by the next invokation of that function! Example:

```python
# Strings are an immutable type, so writng a new value to a string variable simply creates a new string in memory.
def append_to_string(new_string, old_string=''):
	old_string = old_string + new_string
	return old_string

# Lists are a mutable type, so changes made to it will be picked up by future invokations
def append_to_list(elem, old_list=[])
	old_list.append(elem)
	return old_list
```

Results in the fairly unexpected:

```python
>>> append_to_string('hi')
'hi'
>>> append_to_string('hi again')
'hi again'
>>> append_to_list('hello')
['hello']
>>> append_to_list('hey')
['hello', 'hey']
```

If you're interested in the religious war behind what is (in your author's opinion) an obvious and horrible design flaw in the language, check out this StackOverflow thread: https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument

The recommended way to handle cases where you'd want to supply a mutable value as a default is to follow this pattern instead:

```python
def append_to_list(elem, old_list=None)
	if old_list == None:
		old_list = []
	old_list.append(elem)
	return old_list
```

## Syntax

For the most part, Python syntax should be easy to pick up. Here's a couple of things that might be a little more complicated:

### Comprehensions

Comprehesions are a quick way to do something like a filter or map action on an iterable (like a list or dictionary). They can be a bit tricky to grasp at first, but tend to be quite useful and readable once you're used to them.

```python
import transformer

base_list = [1, 3, 4, 6, 7, 8, 8, 8, 3, 5, 4, 10]

# Run each list element through a transformer
transformed_list = [transform(elem) for elem in base_list]

# Remove all list elements that are < 6
less_than_six = [elem for elem in base_list if elem < 6]

# Map the list to a dictionary where the keys are the unique list elements and the values are those elements * 2
mapped_dict = {elem:(elem * 2) for elem in base_list}
```

### Slice Notation

In addition to accessing individual list elements by their integer index, Python lists (and strings! And other iterables) can return sub-lists (and sub-strings, etc!) via slice notation. The notation is simple, `[start:stop]`, where `start` is inclusive and `stop` is exclusive. If either are not supplied, then the entirety of the list in that direction will be used. Examples:

```python
>>> base_list = [1, 3, 4, 6, 7, 8, 8, 8, 3, 5, 4, 10]
>>> base_list[2:5]
[4, 6, 7]
>>> base_list[:2]
[1, 3]
>>> base_list[7:]
[8, 3, 5, 4, 10]
>>> 'strings too!'[2:6]
'ring'
```

Negative numbers can also be used, and will step backward from the end of the iterable:

```python
>>> base_list = [1, 3, 4, 6, 7, 8, 8, 8, 3, 5, 4, 10]
>>> base_list[:-1]
[1, 3, 4, 6, 7, 8, 8, 8, 3, 5, 4]
>>> base_list[:-7]
[1, 3, 4, 6, 7]
>>> base_list[-7:]
[8, 8, 8, 3, 5, 4, 10]
>>> base_list[-7:-1]
[8, 8, 8, 3, 5, 4]
```

### Data Types

Python data types are quite straighforward, but the terminology might differ somewhat from other languages, so this will be a quick rundown to capture what these words mean in the context of Python.

#### List

Described with square brackets, elements separated by commas:

`[1, 2, ...]`

A basic collection, a list behaves essentially like an indexed array (not like PHP's associative array!) in most dynamic languages. Lists are not of a fixed size, so in languages that require arrays to have fixed size lists behave more like a higher-level type, usually called a `List`. Since Python is dynamically typed, there is no restriction preventing lists from containing more than one type of data.

#### Dictionary

Described by curly braces, keys and values separated by colons, entries separated by commas:

`{'a': 1, 'b': 2, ...}`

Elsewhere known as a hashmap, hashtable, associative array, or even an object thanks to JavaScript, a dictionary is a basic key:value data type. Dictionaries can take any date type as their value, but require a hashable type (generally immutables) for its keys.

#### Tuple

Described by standard parenthese, elements separated by commas. In the case of a single-element tuple, a trailing comma must be added:

`(1, 2, ...)`

`(1,)`

Similar to a list, but immutable: elements cannot be added or removed from a tuple once it is created, and elements within the tuple cannot be switched out for others. However, mutable objects stored in a tuple can still be updated. Example:

```python
>>> t = (1, 2)
>>> t[0] = 3
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t = ([],)
>>> t[0].append(1)
([1],)
```

#### Set

A collection of unique values with a lookup time of O(1). Sets behave essentially like a dictionary with keys only, no values. Similar to dictionary keys, sets only accept elements that are of a hashable data type.