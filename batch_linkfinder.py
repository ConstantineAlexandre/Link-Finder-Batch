import subprocess
import os
from colorama import Fore, Style, init

init(autoreset=True)

def run_linkfinder(url):
    try:
        print(f"{Fore.CYAN}Processing: {url}")
        
        result = subprocess.run(['python3', 'linkfinder.py', '-i', url, '-o', 'cli'], 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            print(f"{Fore.GREEN}Results for {url}:\n{Fore.YELLOW}{result.stdout}\n")
        else:
            print(f"{Fore.RED}Error processing {url}: {result.stderr}")
    
    except Exception as e:
        print(f"{Fore.RED}Exception occurred while processing {url}: {str(e)}")

def process_urls(file_path):
    if not os.path.exists(file_path):
        print(f"{Fore.RED}File {file_path} does not exist.")
        return
    
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines()]
    
    for url in urls:
        run_linkfinder(url)

url_file = input(f"{Fore.CYAN}Enter the path to the file containing URLs: ").strip()

process_urls(url_file)
