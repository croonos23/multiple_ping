import subprocess

def ping_ip(ip):
    result = subprocess.run(['ping', '-c', '1', ip], capture_output=True)
    if result.returncode == 0:
        return True
    else:
        return False

archivo_ips = 'ips.txt'
archivo_resultados = 'resultados.csv'

with open(archivo_ips, 'r') as file:
    ips = file.read().splitlines()

with open(archivo_resultados, 'w') as file:
    for ip in ips:
        if ping_ip(ip):
            file.write(f'{ip}; OK\n')
        else:
            file.write(f'{ip}; NOK\n')
