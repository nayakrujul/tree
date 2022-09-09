# tree
View your directory structure more easily!

## Example

This is a folder structure

<img width="173" alt="Folder Structure" src="https://user-images.githubusercontent.com/55329600/189335278-d14713d2-ec59-423a-a5a1-4c3b7b0c9fbb.png">

Using the `tree` command, you get this:

```zsh
$ tree
|- MyFolder
  |- .DS_Store
  |- SubfolderA
    |- .DS_Store
    |- SubSubfolder1
      |- __init__.py
      |- main.py
    |- SubSubfolder2
      |- __init__.py
      |- main.py
    |- SubSubfolder3
      |- __init__.py
      |- main.py
  |- SubfolderB
    |- .DS_Store
    |- SubSubfolder1
      |- __init__.py
      |- main.py
    |- SubSubfolder2
      |- __init__.py
      |- main.py
    |- SubSubfolder3
      |- __init__.py
      |- main.py
```

## Installation

From PyPI:

```zsh
$ pip install tree-directory
```

## Commands

There are three commands that come with this package. All of them print the structure of the directory, but with different orders:

### 1. `tree`

Ordered by last accessed.

### 2. `tree2`

Ordered by filename (alphabetical order)

### 3. `tree3`

Ordered by file extension (alphabetical order, folders first)

Just type the command and it will output the directory stucture.
