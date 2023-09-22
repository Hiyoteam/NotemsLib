# NotemsLib
Use simple Python3 API interface to operate Note.ms pages.

# Table of Contents
 - [Install](#install)
 - [Import](#import)
 - [APIs](#apis)
   - [notemslib.NoteMS](##notemslibnotems)
   - [NoteMS.write](##notemswrite)
   - [NoteMS.load](##notemsload)
   - [NoteMS.close](##notemsclose)

# Install
As this project depends on selenium, you need to install selenium and webdriver first.
Then, you can clone our repository.
```
git clone https://github.com/Hiyoteam/NotemsLib.git notemslib
```
Next, copy the `notemslib.py` file from `notemslib` to the root of your project.
We may upload the package to PyPI later, but for now this is the only way you can install it.

# Import
After completing [the previous step](#install), you can import the package by `import notemslib`.

# APIs

## notemslib.NoteMS
Initialize a Note.ms client.

The default is to use Chrome webdriver and Chrome options, but if you want to use another browser, you can do these steps following (using Microsoft Edge as an example)

1. Write the following lines in the header of your file
```
from selenium import webdriver
from selenium.webdriver.edge.options import Options
```

2. Initialize the client with the following parameters
```
client = notemslib.NoteMS(driver=webdriver.Edge, options=Options)
```

## NoteMS.write
Write the content to a Note.ms page.

As an example, if I want to write "Hello, World" to [note.ms/test](https://note.ms/test), I need to call it like this.

```
client=notemslib.NoteMS()
client.write("test", "Hello, World")
```

To prevent the write operation from starting before the page is loaded, so there may be a delay ranging from 0.2 to 2 seconds.

## NoteMS.load
Load the content of the Note.ms page.
If the content of [note.ms/test](https://note.ms/test) is "Hello, World", then running the following code will give you "Hello, World".
```
client=notemslib.NoteMS()
result = client.load("test")
print( result )
```

## NoteMS.close
Release all resources.
This operation does not require any parameters and is typically executed when the client is no longer needed.
The client will not be available after this function is executed.
Example: Free all resources of the client
```
client.close()
```
