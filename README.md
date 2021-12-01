# show-ip-arp-mac-lookup
Searches for MAC addresses in a text file of a Cisco "show IP arp" in any address format
## What it does:
* Takes a text file with the output of a Cisco ```#sh ip arp``` and searches for a given MAC address in any format, outputs the results to a file
## Why?
* Cisco puts MAC addresses in a unique format that can lead to not finding an existing MAC due to typos, this eliminates this risk
* Easy to use, and highly portable -- I dumped the ```sh ip arp``` results to my cell for a quick lookup if out in the field
## Output:
![image](https://user-images.githubusercontent.com/48565067/144312863-859ca369-2a51-4a62-98f5-75557bd097a5.png)
