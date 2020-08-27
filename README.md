# My Python (`my_py`) Modules

This is a collection of Python modules used in my other projects, maintained in one place for convenience. This should not be confused with the static type checking tool, `mypy` (<https://github.com/python/mypy>). I just couldn't think of a better name.

## Contents

* `my_ip` - methods to determine the IP address of a system
	- Relies on the `netifaces` module
	- Prefers the interface that can reach the outside world
	- `public_ip` attempts to query 3rd party servers to obtain the public facing IP address
	- `local_ip` attempts to determine the interface that routes to the public Internet and returns the address of that interface
	- `local_mac` returns the MAC address of the interface above
