
import re

class URI:

    class Scheme:
        LOCAL           = 1
        SSH             = 2
        TELNET          = 3

    to_constants = {
        "ssh":      Scheme.SSH,
        "local":    Scheme.LOCAL,
        "telnet":   Scheme.TELNET,
    }

    to_ports = {
        "ssh":      22,
        "local":    0,
        "telnet":   23,
    }

    def __init__(self, uri):
        self.uri = uri

        if self.uri:
            pattern = re.compile("^([a-z]+)://([a-z0-9.]+)(:([\d]+))?$")
            match = pattern.match(self.uri)
            if match:
                self.const = self.to_constants[match.group(1)]
                self.host = match.group(2)
                if match.group(4) is not None:
                    self.port = int(match.group(4))
                else:
                    self.port = self.to_ports[match.group(1)]

    def getScheme(self, default=None):
        return getattr(self, "const", default)

    def getHost(self, default=None):
        return getattr(self, "host", default)

    def getPort(self, default=None):
        return getattr(self, "port", default)
