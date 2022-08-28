# nmap-inventory

Step 1: run an nmap ARP discovery scan:

```bash
nmap -sn 192.168.1.0/24 -oX inventory.xml
```

Step 2: run this script in the same dir.