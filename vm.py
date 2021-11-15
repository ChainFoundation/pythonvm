import virtualbox
from virtualbox.library import CleanupMode

vbox = virtualbox.VirtualBox()


def launchVm(name):
    print("launching")
    session = virtualbox.Session()
    machine = vbox.find_machine(name)
    progress = machine.launch_vm_process(session, "headless", [])
    progress.wait_for_completion()

def listMachines():
    print("Listing Available machines")
    for m in vbox.machines:
        print(m)

def createMachine():
    print("Creating a New VM \n ****************************** \n ")
    name = input("What is the new VM's name? \n")
    settings_file = str("") #E:VirtualBox VMs
    # print("settings file: " + settings_file)
    os_type = input("Which OS Type ID (eg: Linux, Windows) \n")
    machine = vbox.create_machine(settings_file, name, [], os_type, "")
    
    if(input("Are you sure you want to create this machine? (y/n)\n") == "y" ):
        print("Creating...")
        machine.save_settings()
        vbox.register_machine(machine)


def deleteMachine():   
    print("Delete a VM \n********************************* \n")
    listMachines()
    name = input("What is the VM you wish to delete name? \n")
    machine = vbox.find_machine(name)
    media = machine.unregister(CleanupMode(4))
    print(name + "contains the following media")
    if(input("do you wish to delete all the media files? (y/n) \n") == "y"):
        machine.delete_config(media)
        print("All media deleted")
    else:
        print("Media not deleted")

def start():
    opt = input("What do you wish to do? \n 1. Start an available vm \n 2. Create a new vm \n 3. Delete a vm \n")
    match opt:
        case "1":
            listMachines()
            name = input("Which machine do you wish to Launch? \n")
            launchVm(name)

        case "2":
            createMachine()

        case "3":
            deleteMachine()


start()

