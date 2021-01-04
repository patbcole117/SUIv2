
from app import app
from app.utils.conf_parse import get_config

import os

app.run(debug=False, host=os.getenv('SUI_HOST'), port=os.getenv('SUI_PORT'))