from pathlib import Path

def write_content(self, content, encoding='utf-8', errors=None):
    ''' Writes content to the Path's path, creating any parent directories as necessary.
        This method is added to the Path class by the pathlib_additions module.'''
    self.parent.mkdir(parents=True, exist_ok=True)
    self.write_text(content, encoding, errors)

def directories(self):
    ''' Returns an iterator of directories in this path.
        This method is added to the Path class by the pathlib_additions module.'''
    return filter(Path.is_dir, self.iterdir())

def files(self):
    ''' Returns a list of files in this path.
        This method is added to the Path class by the pathlib_additions module.'''
    return filter(Path.is_file, self.iterdir())

def copy(self, destination):
    ''' Copies this path to the destination, which can be a Path object or string.
        Creates the destination directory if necessary.
        This method is added to the Path class by the pathlib_additions module.'''
    import shutil
    if isinstance(destination, str):
        output = Path(destination)
    elif isinstance(destination, Path):
        output = destination
    else:
        raise ValueError('Expected string or Path as destination')
    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(self.absolute(), output.absolute())
        
def walk(self, path_filter=None):
    ''' Returns an iterator of Paths in this path.
        If a path_filter function is specified, it is called for each item.
        This method is added to the Path class by the pathlib_additions module.'''
    return filter(path_filter, self.glob('**/*'))

def rmtree(self):
    ''' Removes all items under this path, including the path itself.
        Does *not* raise an exception if the path doesn't exist.
        This method is added to the Path class by the utilities module.'''
    # Directories must be empty to delete, so first delete all files.
    for item in self.glob('**/*'):
        if not item.is_dir():
            item.unlink()

    dirs = list(self.glob('**/*'))
    dirs.sort(key=lambda item: len(str(item.absolute())), reverse=True)
    for item in dirs:
        item.rmdir()
    try:
        self.rmdir()
    except:
        pass

Path.write_content = write_content
Path.directories = directories
Path.files = files
Path.copy = copy
Path.walk = walk
Path.rmtree = rmtree

def main():
    print(dir(Path))

if __name__ == '__main__':
    main()