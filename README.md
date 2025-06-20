# Dweetme-python-client
This is a Python and Micropython client library for dweetme

## Installation 
``` zsh
pip3 install dweetme-client
```

## Example

``` python
import dweetme-client  
dweet = dweetme_client.DweetClient("http://dweet.me:3333")  
dweet.get_latest_dweet("demoESP32")
```
