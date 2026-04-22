experiment = input("Which experiment are you interested in?").lower().strip()

if experiment == "lhc":
    print("Let's find the Higgs Bosson!")
elif experiment == "lhcb":  # a shortened version of `else if`
    print("That ones a beauty!")
elif experiment == "alice":
    print("I like ions.")
elif experiment.startswith("lhc"):
    print("Are we using the hadron collidor for something new?")
else:
    print("I don't that experiment.")


energy = float(input("Enter beam energy (GeV): "))

if energy < 0:
    print("Invalid energy")
elif energy == 0:
    print("No beam")
elif energy < 1000:
    print("Setup mode")
else:
    print("Physics run")