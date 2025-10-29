def find_zone(zipcode):
    if zipcode <1 or zipcode >99999:
        return 'Invalid Zip'
    elif zipcode >=1 and zipcode <=6999:
        return 1
    elif zipcode >=7000 and zipcode <=19999:
        return 2
    elif zipcode >=20000 and zipcode <=35999:
        return 3
    elif zipcode >=36000 and zipcode <=62999:
        return 4
    elif zipcode >=63000 and zipcode <=84999:
        return 5
    elif zipcode >=85000 and zipcode <=99999:
        return 6
    
def find_distance(end_zip, start_zip):
    end_zone = find_zone(end_zip)
    start_zone = find_zone(start_zip)

    if end_zone == 'Invalid Zip' or start_zone == 'Invalid Zip':
        return "UNMAILABLE"
    return abs(end_zone-start_zone)

def postage_type(length, height, thickness): #determine package type, based on package type, run function (ex. Large_Envelope()), pull the total_zones, add price based on package type and distance traveled.
    perim = length + 2*(height + thickness)

    if 3.5<=length<=4.25 and 3.5<=height<=6 and .007<=thickness<=.016:
        return "Regular Post Card"
    elif 4.25<length<6 and 6<height<11.5 and .007<=thickness<=.015:
        return "Large Post Card"
    elif 3.5<=length<=6.125 and 5<=height<=11.5 and .016<thickness<.25:
        return "Envelope"
    elif 6.125<length<24 and 11<=height<=18 and .25<=thickness<=.5:
        return "Large Envelope"
    elif perim<=84 and length>=24 or height>18 or thickness>.5:
        return "Package"
    elif 84<perim>=130 and length>=24 or height>18 or thickness>.5:
        return "Large Package"
    else:
        return "UNMAILABLE"

def interpret_info (info):
    info=info.split (",")
    length=float(info[0])
    height=float(info[1])
    thickness=float(info[2])
    start_zip=int(info[3])
    end_zip=int(info[4])
    return length, height, thickness, start_zip, end_zip

def find_price(postage, total_zones):
    if postage == "Regular Post Card":
        return .2 + .03*total_zones
    elif postage == "Large Post Card":
        return .37 + .03*total_zones
    elif postage == "Envelope":
        return .37 + .04*total_zones
    elif postage == "Large Envelope":
        return .6 + .05*total_zones
    elif postage == "Package":
        return 2.95 + .25*total_zones
    elif postage == "Large Package":
        return 3.95 + .35*total_zones
    else:
        return "UNMAILABLE"
    
def format (cost):
    if cost == "UNMAILABLE":
        return "UNMAILABLE"
    final_price = (f'{cost:.2f}')

    if final_price[0] == "0":
        final_price = final_price[1:]
    return final_price
    
def main():
    info = input ("What is the Length, Height, Thickness, Start zip code, and End zip code")
    length, height, thickness, start_zip, end_zip = interpret_info(info)
    card_type = postage_type(length, height, thickness)
    total_zones = find_distance(end_zip, start_zip)
    cost = find_price(card_type, total_zones)
    print(format(cost))
main()
