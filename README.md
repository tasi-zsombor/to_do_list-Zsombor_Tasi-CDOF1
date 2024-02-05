# to_do_list-Zsombor_Tasi-CDOF1

Console-based application that helps you keep track of the tasks you need to do. It can perform the following functions: 
* add and delete tasks
* listing tasks
* tasks have two statuses: todo and done.

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

You can contribute to the application in numerous ways.
Here is a guide on how to setup your contributions.

### 1. Fork the Repository

Click on the "Fork" button on the top right of this repository's page to create your own copy of the project.

### 2. Clone Your Fork

Clone your forked repository to your local machine.

```bash
git clone https://github.com/tasi-zsombor/to_do_list-Zsombor_Tasi-CDOF1.git
```

### 3. Create a new branch for your contribution. 

Use a descriptive name that summarizes the purpose of your changes.

```bash
git checkout -b feature/new-feature
```

### 4. Make changes

Make your desired changes to the code, documentation, or any other relevant files. Implement new features or fix bugs, issues.

### 5. Test your changes

Make sure that your changes are viable and are working as intended. Run tests if available.

### 6. Commit Your Changes

Commit your changes and add a relevant commit message.

```bash
git commit -m "Add new feature"
```

### 7. Push Your Changes

Push your changes to your forked repository on GitHub.

```bash
git push origin feature/new-feature
```

### 8. Create a Pull Request

Open your forked repository in GitHub and click on the "New Pull Request" button. Provide a detailed description about the changes and submit the pull request.

You succesfully made a pull request for an improvement!

## Authors

* **Zsombor Tasi** - *Initial work*

See also the list of [contributors](https://github.com/tasi-zsombor/to_do_list-Zsombor_Tasi-CDOF1/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
>>>>>>> zsombor
