
from app import app
from app.utils.conf_parse import get_config

c = get_config()
app.run(debug=False, host=c['l_addr'], port=c['l_port'])