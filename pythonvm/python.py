import virtualbox
from virtualbox.library import StorageBus

def launchVmById(id):
    session = virtualbox.Session()
    name = vbox.machines[int(id)]