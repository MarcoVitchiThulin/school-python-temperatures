import re # Importera modul för RegEx

scale = "C" # Sätt default skala

pattern = re.compile(r'^\d+$') # Definiera RegEx pattern för tal

ce = 1
ke = 273.15
fa = 33.8

def convert(temp):
    global scale # Använd global variabel
    match scale: # Inte särskilt välskriven, men gör sitt jobb
        case "C":
            temp_c = temp
            temp_k = temp * ke
            temp_f = temp * fa
        case "K":
            temp_c = temp - ke
            temp_k = temp
            temp_f = temp_c * fa
        case "F":
            temp_c = 5/9*(temp-32)
            temp_k = temp_c * ke
            temp_f = temp
    return str(temp_c), str(temp_k), str(temp_f)

def main():
    global scale
    while True:
        command = input("C/K/F eller temperatur: ")
        match command:  # Byt skala
            case "C":
                print("Byter till Celsius.")
                scale = "C"
            case "K":
                print("Byter till Kelvin.")
                scale = "K"
            case "F":
                print("Byter till Farenheit")
                scale = "F"
            case _:
                if pattern.findall(command): # Använd RegEx för att kolla om command är ett tal
                    c, k, f = convert(float(command))
                    print("Celsius: "+c)
                    print("Kelvin: "+k)
                    print("Farenheit: "+f)
                else:   # Är command inte ett alias för en skala, eller ett tal, så är det inte giltligt.
                    print("Ogiltligt kommando.")

if __name__ == "__main__":
    main()