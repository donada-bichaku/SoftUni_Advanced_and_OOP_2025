# Create the service manager
from project.tech_service_manager import TechServiceManager

manager = TechServiceManager()

# Add devices
print(manager.add_device("Laptop", "LPT1234A", 40, True))
print(manager.add_device("Laptop", "LPT5678B", 1, True))
print(manager.add_device("Laptop", "LZT5678B", 2, True))
print(manager.add_device("Smartphone", "SPH0001X", 10, False))
print(manager.add_device("Smartphone", "SPH0002Y", 80, True))
print(manager.add_device("Smartphone", "SYH0002Y", 1, True))
print(manager.add_device("Smartwatch", "SZT3009Z", 5, False))
print(manager.add_device("Smartwatch", "SWT3009Z", 5, False))
print()

# Add repair shops
print(manager.add_repair_shop("BFixIt Center", ("Desktop", "Laptop", "Smartphone", "Smartwatch")))
print(manager.add_repair_shop("AQuickFix", ("HomeAI", "Smartwatch")))
print()

# Send devices for repair
print(manager.send_for_repair("BFixIt Center", "Laptop"))
print(manager.send_for_repair("BFixIt Center", "Smartphone"))
print(manager.send_for_repair("BFixIt Center", "Smartwatch"))
print(manager.send_for_repair("BFixIt Center", "Laptop"))
print(manager.send_for_repair("AQuickFix", "Smartphone"))
print(manager.send_for_repair("AQuickFix", "Smartwatch"))
print()

# Process repairs at first shop
print(manager.process_repairs(manager.repair_shops[0]))
print(manager.process_repairs(manager.repair_shops[0]))
print()

# Display current service status
print(manager.tech_service_status())
print()

# Receive repaired devices
print(manager.receive_repaired_devices(manager.repair_shops[0]))
print(manager.receive_repaired_devices(manager.repair_shops[1]))
print()

# Display final service status
print(manager.tech_service_status())
