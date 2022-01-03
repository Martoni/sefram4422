# sefram4422
Python module to drive Sefram 4422 DDS by RS232

# Install

sefram4422 require python > 3.7  and pyserial module.

Program can be installed in developpement mode with following commands:

```shell
$ git clone https://github.com/Martoni/sefram4422.git
$ cd sefram4422
$ python -m pip install -e .
```

A binary script named sf4422 is installed on system:

```shell

$ sf4422 -h
sf4422 [options]
-h, --help             print this message
-s, --speed=[baudrate] set baudrate (default 19200)
-d, --ttydev=[devname] set uart device (default /dev/ttyUSB0
-v, --verbose          print some verbose messages
-f, --freq=[frequency] set frequency
-x, --debug            print some informations
```

but sefram4422 can be used as python module too:

```Python
from sf4422 import Sefram4422
```

# Ressources

- [Sefram4422 datasheet](http://www.farnell.com/datasheets/78647.pdf)

