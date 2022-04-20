import os

from dlgo.agent.naive import RandomBot
from dlgo.httpfrontend.server import get_web_app

random_agent = RandomBot()
web_app = get_web_app({'random': random_agent})
port = int(os.environ.get('PORT', 5000))
web_app.run(host='0.0.0.0', port=port)
