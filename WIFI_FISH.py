import subprocess

def get_wifi_password():
    try:
        # Scan for Wi-Fi networks
        result = subprocess.check_output(['termux-wifi-scaninfo']).decode('utf-8').split('\n')
        networks = [line.split(",")[0] for line in result if line]

        if not networks:
            print("No Wi-Fi networks found.")
            return

        # Display available Wi-Fi networks
        print("Wi-Fi Networks:")
        for i, network in enumerate(networks, 1):
            print(f"{i}. {network}")

        # Ask the user to choose a Wi-Fi network
        choice = int(input("Enter the number of the Wi-Fi network to get the password: "))

        if 1 <= choice <= len(networks):
            network = networks[choice - 1]
            try:
                password = subprocess.check_output(['termux-wifi-get-psk', network]).decode('utf-8').strip()
                print(f"Password for {network}: {password}")
            except Exception as e:
                print(f"Failed to retrieve password for {network}: {e}")
        else:
            print("Invalid choice. Please enter a valid number.")
    except Exception as e:
        print(f"Failed to retrieve Wi-Fi networks: {e
