
import sys

CONF_PATH = 1

options = {
        CONF_PATH: "conf_path",
    }

def get(opt):
    current_module = sys.modules[__name__]
    if opt not in current_module.options.keys():
        return ValueError("Unexpected option")

    option_key = current_module.options[opt]
    if hasattr(current_module, option_key):
        return getattr(current_module, option_key)
    else:
        return None

def set(opt, value):
    current_module = sys.modules[__name__]
    if opt not in current_module.options.keys():
        return ValueError("Unexpected option")

    option_key = current_module.options[opt]
    setattr(current_module, option_key, value)
