# lib/helpers.py

from models.store import Store
from models.instrument import Instrument
from models.inventory import Inventory
from models.seeds import seeds_database  

def exit_program():
    print("Exiting program. Goodbye!")
    exit()


def add_store():
    name = input("Enter store name: ")
    location = input("Enter store location: ")
    store = Store.create(name, location)
    print(f"Added store: {store}")

def update_store():
    store_id = input("Enter store ID to update: ")
    store = Store.find_by_id(store_id)
    if store:
        store.name = input(f"Enter new name ({store.name}): ") or store.name
        store.location = input(f"Enter new location ({store.location}): ") or store.location
        store.save()
        print(f"Updated store: {store}")
    else:
        print("Store not found.")

def delete_store():
    store_id = input("Enter store ID to delete: ")
    store = Store.find_by_id(store_id)
    if store:
        store.delete()
        print(f"Deleted store: {store}")
    else:
        print("Store not found.")

def view_all_stores():
    stores = Store.get_all_stores()
    for store in stores:
        print(store)

def view_store():
    store_id = input("Enter store ID to view: ")
    store = Store.find_by_id(store_id)
    if store:
        print(store)
    else:
        print("Store not found.")






def add_instrument():
    type = input("Enter instrument type: ")
    model = input("Enter instrument model: ")
    price = int(input("Enter instrument price: "))
    instrument = Instrument.create(type, model, price)
    print(f"Added instrument: {instrument}")

def update_instrument():
    instrument_id = input("Enter instrument ID to update: ")
    instrument = Instrument.find_by_id(instrument_id)
    if instrument:
        instrument.type = input(f"Enter new type ({instrument.type}): ") or instrument.type
        instrument.model = input(f"Enter new model ({instrument.model}): ") or instrument.model
        instrument.price = int(input(f"Enter new price ({instrument.price}): ")) or instrument.price
        instrument.save()
        print(f"Updated instrument: {instrument}")
    else:
        print("Instrument not found.")

def delete_instrument():
    instrument_id = input("Enter instrument ID to delete: ")
    instrument = Instrument.find_by_id(instrument_id)
    if instrument:
        instrument.delete()
        print(f"Deleted instrument: {instrument}")
    else:
        print("Instrument not found.")

def view_all_instruments():
    instruments = Instrument.get_all_instruments()
    for instrument in instruments:
        print(instrument)

def view_instrument():
    instrument_id = input("Enter instrument ID to view: ")
    instrument = Instrument.find_by_id(instrument_id)
    if instrument:
        print(instrument)
    else:
        print("Instrument not found.")







def add_inventory():
    instrument_id = input("Enter instrument ID: ")
    store_id = input("Enter store ID: ")
    stock = int(input("Enter stock: "))
    inventory = Inventory.create(int(instrument_id), int(store_id), stock)
    print(f"Added inventory: {inventory}")

def update_inventory():
    inventory_id = input("Enter inventory ID to update: ")
    inventory = Inventory.find_by_id(inventory_id)
    if inventory:
        inventory.instrument_id = int(input(f"Enter new instrument ID ({inventory.instrument_id}): ")) or inventory.instrument_id
        inventory.store_id = int(input(f"Enter new store ID ({inventory.store_id}): ")) or inventory.store_id
        inventory.stock = int(input(f"Enter new stock ({inventory.stock}): ")) or inventory.stock
        inventory.save()
        print(f"Updated inventory: {inventory}")
    else:
        print("Inventory not found.")

def delete_inventory():
    inventory_id = input("Enter inventory ID to delete: ")
    inventory = Inventory.find_by_id(inventory_id)
    if inventory:
        inventory.delete()
        print(f"Deleted inventory: {inventory}")
    else:
        print("Inventory not found.")

def view_all_inventorys():
    inventories = Inventory.get_all_inventorys()
    for inventory in inventories:  
        print(inventory)

def view_inventory():
    inventory_id = input("Enter inventory ID to view: ")
    inventory = Inventory.find_by_id(inventory_id)
    if inventory:
        print(inventory)
    else:
        print("Inventory not found.")
