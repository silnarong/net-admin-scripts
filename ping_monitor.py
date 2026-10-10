import os
import platform

def check_server_status(hostname):
    """
    Simple cross-platform script to check if a server is online.
    Useful for basic network monitoring.
    """
    parameter = '-n' if platform.system().lower() == 'windows' else '-c'
    # Execute the ping command
    response = os.system(f"ping {parameter} 1 {hostname} > nul 2>&1")
    
    if response == 0:
        print(f"[SUCCESS] {hostname} is UP and responding.")
    else:
        print(f"[ALERT] {hostname} is DOWN or unreachable.")

if __name__ == "__main__":
    # Test with public DNS servers
    target_servers = ["8.8.8.8", "1.1.1.1"]
    
    print("Starting Network Monitor...")
    for server in target_servers:
        check_server_status(server)
