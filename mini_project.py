class InvaidChaiError(Exception): pass

def bill(flavour,cups):
    menu = {"masala":20,"ginger":40}
    try:
        if flavour not in menu:
            raise InvaidChaiError("That chai is not available")
        if not isinstance(cups,int):
            raise TypeError("Number of cups must be an integer")
        total=menu[flavour]*cups
        print(f"your bill for {cups} of {flavour} chai: rupee {total}")
    except Exception as e:
        print("Error: ",e)
    finally:
        print("Thank you for visiting chai code")

bill("mint",2)
bill("masala","three")
bill("ginger",3)

