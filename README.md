# pathlib_additions
I create workflows that involve a huge number of file operations. For doing file operations I strongly recommend the built-in ``pathlib`` library. Before ``pathlib`` to work with files you had to deal with methods in three different libraries (at least) that were designed around the C/UNIX approach to file handling. Not Pythonic, to say the least.

In Python 2 I used a third party libary called [Unipath](https://pypi.org/project/Unipath/) that put almost all the functionality I wanted in a ``Path`` object. In Python 3.4, the ``pathlib`` library was provided, which mostly mirrors ``Unipath``, but left a few things out.

So ``pathlib_additions`` are my additions to ``pathlib`` to make it do everything I want. You are welcome to use this and submit patches/requests/bugs.

To use it, do these imports:

    from pathlib import Path
    import pathlib_additions

``pathlib_additions`` adds a number of methods to the Path object.

## write_content()
``write_content(content, encoding='utf-8', errors=None)``

pathlib's ``write_text()`` method requires the destination directory to exist. ``write_content()`` creates the directory if necessary then uses ``write_text()`` to write out the text.

## directories()
The ``directories()`` method returns an iterator of directories in the Path.

## files()
The ``files()`` method returns an iterator of files in the Path.

## copy()

``copy(destination)``

Copies this path to the destination, which can be a Path object or string. Creates the destination directory if necessary.

## walk()

``walk(path_filter=None)``

Returns an iterator of all Paths in this path's directory structure.
If a ``path_filter`` function is specified, it is called for each item.

## rmtree()
Removes all items under this path, including the path itself. Does *not* raise an exception if the path doesn't exist.

*Library created by Ronald Hayden of [Conquer Programming](http://conquerprogramming.com)*
