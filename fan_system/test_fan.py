from fan import Fan

fan1 = Fan(Fan.FAST, 10, "yellow", True)
fan2 = Fan(Fan.MEDIUM, 5, "blue", False)

print("Fan 1:", fan1.display())
print("Fan 2:", fan2.display())