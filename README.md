# nmap-inventory

Step 1: run an nmap ARP discovery scan as root:

```bash
sudo nmap -sn 192.168.1.0/24 -oX arpscan.xml
```

Step 2: run this script in the same dir.