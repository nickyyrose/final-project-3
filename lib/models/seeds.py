from models.instrument import Instrument
from models.inventory import Inventory
from models.store import Store

def seeds_database():

    print("Resetting tables...")

    Instrument.drop_table()
    Inventory.drop_table()
    Store.drop_table()
    Instrument.create_table()
    Inventory.create_table()
    Store.create_table()
    
    print("Resetting complete...")
    print("Populating tables...")
     
    
    instruments = [
        Instrument.create("Guitar", "Fender Stratocaster", 1000),
        Instrument.create("Synthesizer", "Juno X", 2000),
        Instrument.create("Bass", "Fender Precision", 1200),
        Instrument.create("Drum Set", "Pearl Export", 3000),
        Instrument.create("Piano", "Roland RD88", 2000),
    ]

    
    stores = [
        Store.create("Guitar Freaks", "San Francisco"),
        Store.create("Drum Guys", "Los Angeles"),
        Store.create("Keyboard Crazy", "Berkeley"),
        Store.create("The Guitar Shop", "Oakland"),
        Store.create("Acoustic Central", "San Mateo"),
    ]

    
    inventory_entries = [
        Inventory.create(1, stores[0].id, instruments[0].id),
        Inventory.create(2, stores[1].id, instruments[1].id),
        Inventory.create(3, stores[2].id, instruments[2].id),
        Inventory.create(4, stores[3].id, instruments[3].id),
        Inventory.create(5, stores[4].id, instruments[4].id),
    ]

    print("Populating finished...")




seeds_database()
