![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221122%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221122T102240Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4c125d66747f0dba6f708b56b3122239170a8a4f061ff8b9816f6dac02e98029)
# 0x00. AirBnB clone - The console
## Description of the project.
The [Airbnb](https://www.airbnb.com/) Clone: The console. This repository holds a command interpreter and classes (such as; BaseModel classand other classes that inherit from BaseModel: Amenity, City, State, Place, Review), and a command interpreterlike a shell

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221124%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221124T105516Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a8d41e4aab51c916240154edbf3a113e87aa8df9792c9cf9b3af76c4cc51c32c)

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
