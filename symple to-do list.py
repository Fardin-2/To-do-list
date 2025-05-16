tasks = []

while True:
    print('----My To-Do List----')
    print('1. New Task Add')
    print('2. View All Task')
    print('3. Delete Task')
    print('4. Exit')

    choice = int(input('Enter your choice(1-4): '))
    
    if choice == 1:
        task = input('Enter your Task: ')
        tasks.append(task)
        print('Task added successfully.')
    elif choice == 2:
        for inx, t in enumerate(tasks, start=1):
            print(f"{inx}. {t}")
    elif choice == 3:
        delete_num = int(input('Enter the task number of the task you want to delete: ')) -1
        if not tasks:
            print('Task not found!!')
        if 0 <= delete_num < len(tasks):
            deleted = tasks.pop(delete_num)
            print(f"{delete_num} deleted successfully.")
        else:
            print(f"{delete_num} was not found.")
    elif choice == 4:
        print('Exited..')
        break
    else:
        print('Invaled input.Pleace choces (1-3).')

