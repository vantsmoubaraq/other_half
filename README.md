![](devtools://devtools/bundled/devtools_app.html?remoteBase=https://devtools.azureedge.net/serve_file/@5ed2a3ace08d6077024f01e03930c3504cbb4e4c/&can_dock=true&panel=elements&isFeedbackEnabled=true&enabledExperiments=keyboardShortcutEditor;msEdgeVSCodeThemes#:~:text=https%3A//s3.amazonaws.com/alx%2Dintranet.hbtn.io/uplo%E2%80%A60351a8a793fcb7107f52ff1b7e12d1daadd8a173c33cbc74c)
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uplo…0351a8a793fcb7107f52ff1b7e12d1daadd8a173c33cbc74c)

# 0x00. AirBnB clone - The console
## Description of the project.
The [Airbnb](https://www.airbnb.com/) Clone: The console. This repository holds a command interpreter and classes (such as; BaseModel classand other classes that inherit from BaseModel: Amenity, City, State, Place, Review), and a command interpreterlike a shell

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uplo…6240154edbf3a113e87aa8df9792c9cf9b3af76c4cc51c32c)

### Command interpreter functionalities.
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

### File Storage Engine:
* /models/engine/file_storage.py

## Execution
Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode: 
``$ echo "python3 -m unittest discover tests" | bash```
---
# Author
## 1. [Mugabi Joseph](https://twitter.com/joseph_mugabi "@twitter.com")
## 2. [Mubarak Wantimba](https://github.com/vantsmoubaraq "@github.com")
