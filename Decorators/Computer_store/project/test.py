from project.computer_store_app import ComputerStoreApp

computer_store = ComputerStoreApp()
print(computer_store.build_computer("Desktop Computer", "Apple", "Macbook", "Apple M1 Max", 64))
print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))
