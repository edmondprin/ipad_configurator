# iPad options available on apple.com on January 2026

# 1/ Single source of truth, defined once and re-used everywhere
ipad_models = {"iPad Pro": 749,
          "iPad Air": 449,
          "iPad": 262,
          "iPad Mini": 374}

tax_rate = 0.0825

# 2/ one-time model selection
def select_model():

    print(f"STEP 1: SELECT AN IPAD MODEL\n")
    print(f"Take a look at the list of Ipads below:\n")

    tuple_ipads = tuple(ipad_models.items())
   
    for i, model in enumerate(tuple_ipads, start=1):
        print(f"{i}: {model[0]}")
  
    while True:
        model_selection = input(f"\nPlease select one iPad from the list. You need to enter a number to make your choice, from 1 to {len(ipad_models)}: ")
        try:
            model_selection = int(model_selection)
            if model_selection < 1 or model_selection > len(ipad_models):
                continue
            model_selected = tuple_ipads[model_selection -1]
            return model_selected[0], model_selected[1]
        except ValueError:
            print(f"Make sure to enter a number between 1 and {len(ipad_models)}, then press ENTER")

# 3/ incremental configuration

def configure_storage():
    model, price = select_model()
    # return f"{price * 1 + tax_rate:.2f}"
    
    print(f"\nYou picked the {model}. Great choice! Let's move on with configuring it.\n")
    print(f"\nSTEP 2: SELECT OPTIONS AND/OR ACCESSORIES\n")
    ipad_pro_storage = (("256GB",0), ("512GB",150), ("1TB",450), ("2TB",750))
    ipad_air_storage = (("128GB",0), ("256GB",75), ("512GB",225), ("1TB",375))
    ipad_storage = (("128GB",0), ("256GB",75), ("512GB",225))
    ipad_mini_storage = (("128GB",0), ("256GB",75), ("512GB",225))

    if model == "iPad Pro":
        options = ipad_pro_storage
    elif model == "iPad Air":
        options = ipad_air_storage
    elif model == "iPad":
        options = ipad_storage
    else:
        options = ipad_mini_storage

    for index, value in enumerate(options, start=1):
        print(f"Option {index}: {value[0]} (${value[1]})")

    while True:
        storage_selection = input(f"\nPlease select one storage option from the list. You need to enter a number to make your choice, from 1 to {len(options)}: ")
        try:
            storage_selection = int(storage_selection)
            if storage_selection < 1 or storage_selection > len(options):
                continue
            storage_selected = options[storage_selection -1]
            storage_name_selected = storage_selected[0]
            price += storage_selected[1]
            return model, storage_name_selected, price
        except ValueError:
            print(f"Make sure to enter a number between 1 and {len(options)}, then press ENTER")





def pick_display_size():
    model, storage_name_selected, price = configure_storage()
    print(f"\nLet's move on with selecting a display size (on certain models only).\n")

    ipad_pro_display_size = ((11,0), (13,225))
    ipad_air_display_size = ((11,0), (13,150))
    ipad_display_size = ((11,0),)
    ipad_mini_display_size = ((8.3,0),)

    if model == "iPad Pro":
        options = ipad_pro_display_size
    elif model == "iPad Air":
        options = ipad_air_display_size
    elif model == "iPad":
        options = ipad_display_size
    else:
        options = ipad_mini_display_size

    if model == "iPad Pro" or model == "iPad Air":
        for index, value in enumerate(options, start=1):
            print(f"Option {index}: {value[0]} (${value[1]})")

        while True: # this one needs break to exit
            display_selection = input(f"\nPlease select one display size from the list. You need to enter a number to make your choice, from 1 to {len(options)}: ")
            try:
                display_selection = int(display_selection)
                if display_selection < 1 or display_selection > len(options):
                    continue
                display_selected = options[display_selection -1]
                display_size_selected = display_selected[0]
                price += display_selected[1]
                return model, storage_name_selected, price, display_size_selected
            except ValueError:
                print(f"Make sure to enter a number between 1 and {len(options)}, then press ENTER")

    else:
        print(f"There is only one display size available: {ipad_display_size[0] if model == 'iPad' else ipad_mini_display_size[0]} inches")
        display_size_selected = options[0][0]
        price += options[0][1]
        return model, storage_name_selected, price, display_size_selected

    
    


# print(pick_display_size())


def select_connectivity():
    model, storage_name_selected, price, display_size_selected = pick_display_size()
    print(f"\nLet's move on with choosing the connectivity.\n")

    ipad_pro_connect = (("Wi-Fi",0), ("Wi-Fi + Cellular",150))
    ipad_air_connect = (("Wi-Fi",0), ("Wi-Fi + Cellular",113))
    ipad_connect = (("Wi-Fi",0), ("Wi-Fi + Cellular",112))
    ipad_mini_connect = (("Wi-Fi",0), ("Wi-Fi + Cellular",113))

    if model == "iPad Pro":
        options = ipad_pro_connect
    elif model == "iPad Air":
        options = ipad_air_connect
    elif model == "iPad":
        options = ipad_connect
    else:
        options = ipad_mini_connect

    for index, value in enumerate(options, start=1):
        print(f"Option {index}: {value[0]} (${value[1]})")

    while True:
        connect_selection = input(f"\nPlease select one connectivity option from the list. You need to enter a number to make your choice, from 1 to {len(options)}: ")
        try:
            connect_selection = int(connect_selection)
            if connect_selection < 1 or connect_selection > len(options):
                continue
            connect_selected = options[connect_selection -1]
            connect_name_selected = connect_selected[0]
            price += connect_selected[1]
            return model, storage_name_selected, price, display_size_selected, connect_name_selected
            
        except ValueError:
            print(f"Make sure to enter a number between 1 and {len(options)}, then press ENTER")

        
 # print(tuple_ipads)
 # print(select_model()
print(select_connectivity())
