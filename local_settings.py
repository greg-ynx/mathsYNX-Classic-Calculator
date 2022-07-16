import os

from config.definitions import style_path, img_dir

# This flag is used by the module confapp to set these settings as high priority.
SETTINGS_PRIORITY = 0

# The variable is used by pyforms to define the mode it will run.
# It can has the value 'GUI', 'WEB' or 'TERMINAL'.
PYFORMS_MODE = 'GUI'
PYFORMS_STYLESHEET = style_path
PYFORMS_MAIN_WINDOW_ICON_PATH = os.path.join(img_dir, 'mathsYNX-CC-icon.ico')