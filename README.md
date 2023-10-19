# Agiltron-SelfAlign
Python interface for the [Agiltron SelfAlign](https://agiltron.com/product/selfalign-series-1xn-switch-box/) fiber switch.

## Install
```
pip install git+https://github.com/ograsdijk/Agiltron-SelfAlign.git
```

## Code Example
```Python
from agiltron_selfalign import AgiltronSelfAlign

resource_name = "COM8"
switch = AgiltronSelfAlign(resource_name, number_of_ports = 16)

# change port to port 14
switch.set_fiber_port(14)

# home switch to port 1
switch.home()
```