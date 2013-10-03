I use that simple plugin on each line of my code written in Sublime Text.

That plugin finishes regular line/block endings and moves cursor out of it. 
Can be used for C-style language syntaxes: C, C++, Java, Javascript.

It jumps out of () or {} brackets and adds semicolon if required.

Example of usage
================

Having code:
```
    bar() {
      foo(param1, param2, param3<cursor here>)
    }
```

note, that ")" bracket is added by sublime once you wrote "foo("

press ctrl-enter and get to:
```
    bar() {
      foo(param1, param2, param3);
      <cursor here>
    }
```

press ctrl-enter once more and get to:
```
    bar() {
      foo(param1, param2, param3);
    }
    <cursor>
```

Out of block
------------
```
    if (a > b) {
      do1();
      do2();
      <cursor here>
      do3();
    }
```

(yes, ive just used ctrl-enters to complement do1, do2, do3 calls with semicolon)

ctrl-enter and get to:
```
    if (a > b) {
      do1();
      do2();
      do3();
    }
    <cursor here>
```

Out of functor
--------------
```
    event.on('error', function(message) {
      show(message<cursor>)
    })
```
")" after cursor and ""})"" below are written by sublime itself

ctrl-enter and get:
```
    event.on('error', function() {
      show(message);
      <cursor>
    })
```
ctrl-enter and get:
```
    event.on('error', function() {
      show(message);
    });
    <cursor>
```

Installation
============

1. Copy .py file to your plugins folder (~/.config/sublime-text-2/Packages/User) or use Tools -> New Plugin...
and copy-paste content of .py file there.

2. Map hot-key to the command. Menu Preferences -> Key binding - User and add e.g. hotkey for CTRL-Enter:
```
    [
	      {"keys": ["ctrl+enter"], "command": "out_of_brackets", "args": {}}
    ]
```
