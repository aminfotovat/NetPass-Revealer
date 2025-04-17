import subprocess ,re

def pass_finder(interface):
    pass_command = f"netsh wlan show profile name=\"{interface}\" key=clear"
    pass_result = subprocess.check_output(pass_command, shell=True).decode("utf-8")
    pass_filter = re.findall(r"(?:Key\sContent\s*:\s)(.*)", pass_result)
    return pass_filter

def wlan_finder():
    intf_command = "netsh wlan show profile"
    intf_result = subprocess.check_output(intf_command, shell=True).decode("utf-8")
    intf_filter = re.findall(r"(?:Profile\s*:\s)(.*)",intf_result)
    main_result = {}
    for intf in intf_filter:
        pas = pass_finder(intf)
        if pas != []:
            main_result.update({intf:pas[0]})
        else:
            continue
    return (main_result)

def show_password():
    for ky,val in wlan_finder().items():
        key = ky.replace("\r", "")
        value = val.replace("\r", "")
        print(f"{key} => Password: {value}")

if __name__ == "__main__":
    show_password()
    input('Press Enter to exit ...')


