import re # Importera modul för RegEx

scale = "C" # Sätt standardskala till celsius

pattern = re.compile(r'^\d+$') # Definiera RegEx pattern för att kolla tal

loop = True

def convert(temp):
    global scale # Använd global variabel
    match scale: # Inte särskilt välskriven, men gör sitt jobb
        case "C":
            temp_c = temp
            temp_k = temp + 273.15
            temp_f = (temp * 1.8) + 32
        case "K":
            temp_c = temp - 273.15
            temp_k = temp
            temp_f = 1.8 * (temp - 273) + 32
        case "F":
            temp_c = 5/9*(temp-32)
            temp_k = (temp + 459.67) * 5/9
            temp_f = temp
    return str(temp_c), str(temp_k), str(temp_f)

def main():
    global scale, loop
    while loop:
        command = input("C/K/F eller temperatur: ") # Ta input från användaren
        if command.isalpha(): command = command.upper()
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
            case "H":
                # Lång string som håller output för hjälpkommandot 
                print(" H/h skriver ut en hjälptext där alla kommandon visas.\n A/a avslutar programmet.\n F/f byter till att anta att alla temperaturer utgår från Farenheit\n C/c byter till att anta att alla temperaturer utgår från Celsius\n K/k byter till att anta att alla temperaturer utgår från Kelvin\n Ett tal - skriver ut temperaturen i de två andra skalorna som motsvarar angivna temperaturen.")
            case "A":
                print("Avslutar, hejdå!")
                loop = False
            case _:
                if pattern.findall(command): # Använd RegEx för att kolla om command är ett tal, endast för att visa att det går. Vanligtvis hade man använd .isnumeric().
                    c, k, f = convert(float(command))
                    print("Celsius: "+c)
                    print("Kelvin: "+k)
                    print("Farenheit: "+f)
                else:   # Är command inte ett alias för en skala, eller ett tal, så är det inte giltligt.
                    print("Ogiltligt kommando.")

if __name__ == "__main__":
    main()
