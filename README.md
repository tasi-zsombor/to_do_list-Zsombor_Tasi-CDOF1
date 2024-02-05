# to_do_list-Zsombor_Tasi-CDOF1

Console-based application that helps you keep track of the tasks you need to do. It can perform the following functions: 
* add and delete tasks
* listing tasks
* tasks have two statuses: todo and done. 

<<<<<<< HEAD
A console based application to help keep track of tasks. You should be able to add, delete, complete tasks.
Konzol alapú alkalmazás, amely segít nyomon követni a feladatokat. A következő funkciókat tudja ellátni: 
- feladatok hozzáadása, törlése
- feladatok listázása
- feladatoknak két állapota van: todo és done. Amikor hozáadtuk a feladatot, az a todo listába kerül. Amiután elvégeztük és beállítottuk
=======
When a task is added, it is added to the todo.txt.  After it is done, it is in the done.txt.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Make sure you have the following installed on your machine:

* Python: [Python dowload](https://www.python.org/downloads/)

### Installing

Clone the repository to your local machine:
```
git clone https://github.com/tasi-zsombor/to_do_list-Zsombor_Tasi-CDOF1
```

Navigate to the project directory:
```
cd to_do_list-Zsombor_Tasi-CDOF1
```

### Usage:
* After running a program, you will see the following text displayed: "Type './todo help' to see commands, Enter a command or 'q' to exit"
* You then have three options:
    - type './todo help' to see commands
    - type one of the commands
    - press 'q' to exit

### Examples

Add a Task:
```
Type './todo help' to see commands, Enter a command or 'q' to exit: ./todo add homework
Added todo: "homework"
```

Show Tasks:
```
Type './todo help' to see commands, Enter a command or 'q' to exit: ./todo ls          
[6] homework
[5] "homework"
[4] "jkl"
[3] xcvv
[2] homework
[1] "asd"
```

Delete Task:
```
Type './todo help' to see commands, Enter a command or 'q' to exit: ./todo del 3
Deleted todo #3
```

Complete Task:
```
Type './todo help' to see commands, Enter a command or 'q' to exit: ./todo done 1
Marked todo #1 as done.
```

Report:
```
Type './todo help' to see commands, Enter a command or 'q' to exit: ./todo report
2024-02-05 Pending : 4 Completed : 3
```

Show usage:
```
Type './todo help' to see commands, Enter a command or 'q' to exit: ./todo help
Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics
```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Zsombor Tasi** - *Initial work*

See also the list of [contributors](https://github.com/tasi-zsombor/to_do_list-Zsombor_Tasi-CDOF1/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
>>>>>>> zsombor
