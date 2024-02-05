import sys
import datetime

# Help function
def help():
    sa = """Usage :-
$ ./todo add "todo item" [priority]  # Add a new todo with optional priority (default is 1)
$ ./todo ls                          # Show remaining todos
$ ./todo del NUMBER                  # Delete a todo
$ ./todo done NUMBER                 # Complete a todo
$ ./todo help                        # Show usage
$ ./todo report                      # Statistics"""
    sys.stdout.buffer.write(sa.encode('utf8'))

# Function to add item in todo list
def add(s, priority=1):
    try:
        priority = int(priority)
        if priority < 1 or priority > 3:
            raise ValueError("Priority should be between 1 and 3.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    f = open('todo.txt', 'a')
    st = f"{s} | Priority: {priority}"
    f.write(st)
    f.write("\n")
    f.close()
    s = '"' + s + '"'
    print(f"Added todo: {s} with Priority: {priority}")

# Function to print the todo list items
def ls():
    try:
        nec()
        l = len(d)
        k = l

        for i in d:
            sys.stdout.buffer.write(f"[{l}] {d[l]}".encode('utf8'))
            sys.stdout.buffer.write("\n".encode('utf8'))
            l = l - 1

    except Exception as e:
        raise e

# Function to complete a todo
def done(no):
    try:
        nec()
        no = int(no)
        f = open('done.txt', 'a')
        st = 'x ' + str(datetime.datetime.today()).split()[0] + ' ' + d[no]

        f.write(st)
        f.write("\n")
        f.close()
        print(f"Marked todo #{no} as done.")

        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)

            for i in lines:
                if i.strip('\n') != d[no]:
                    f.write(i)
            f.truncate()
    except:
        print(f"Error: todo #{no} does not exist.")

# Function to show report/statistics of todo list
def report():
    nec()
    try:
        nf = open('done.txt', 'r')
        c = 1

        for line in nf:
            line = line.strip('\n')
            don.update({c: line})
            c = c + 1
        print(f'{str(datetime.datetime.today()).split()[0]} Pending : {len(d)} Completed : {len(don)}')

    except:
        print(f'{str(datetime.datetime.today()).split()[0]} Pending : {len(d)} Completed : {len(don)}')

# Function to delete a todo
def deL(no):
    try:
        no = int(no)
        nec()

        # Utility function defined in main
        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)

            for i in lines:
                if i.strip('\n') != d[no]:
                    f.write(i)
            f.truncate()
        print(f"Deleted todo #{no}")

    except Exception as e:
        print(f"Error: todo #{no} does not exist. Nothing deleted.")

# Utility function used in done and report function
def nec():
    try:
        f = open('todo.txt', 'r')
        c = 1
        for line in f:
            line = line.strip('\n')
            d.update({c: line})
            c = c + 1
    except:
        sys.stdout.buffer.write("There are no pending todos!".encode('utf8'))

# Main program
def get_user_input():
    return input("\n\nType './todo help' to see commands, Enter a command or 'q' to exit: ")

# Main program
if __name__ == '__main__':
    try:
        d = {}
        don = {}

        while True:
            user_input = get_user_input()
            args = user_input.split()

            if args[0] == './todo':
                args = args[1:]

            if args[0] == 'del':
                args[0] = 'deL'

            if args[0] == 'add' and len(args[1:]) == 0:
                print("Error: Missing todo string. Nothing added!")
            elif args[0] == 'done' and len(args[1:]) == 0:
                print("Error: Missing NUMBER for marking todo as done.")
            elif args[0] == 'deL' and len(args[1:]) == 0:
                print("Error: Missing NUMBER for deleting todo.")
            elif args[0] == 'q':
                sys.exit()  # Exit the program
            else:
                if args[0] == 'add':
                    add(*args[1:])
                else:
                    globals()[args[0]](*args[1:])

    except KeyboardInterrupt:
        print("\nExiting...")
