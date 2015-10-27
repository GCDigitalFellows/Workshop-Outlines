# Let's pull together some of what we've learned



while 1:
    weather = raw_input("What's the weather today? ")
    if weather == "cloudy":
        print("You don't need a hat")
    elif weather == "sunny":
        print("Wear shades")
    elif weather == "rainy":
        print("Bring an umbrella")
    elif weather == "snowy":
        print("Wear your wolly muffler")
    else:
        print("I don't know what you should do today...")
