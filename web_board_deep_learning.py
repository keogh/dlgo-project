import os
import h5py

from dlgo.agent.predict import load_prediction_agent
from dlgo.httpfrontend.server import get_web_app

model_file = h5py.File("./agents/deep_bot.h5", "r")
bot_from_file = load_prediction_agent(model_file)

port = int(os.environ.get('PORT', 5000))
web_app = get_web_app({'predict': bot_from_file})
web_app.run(host='0.0.0.0', port=port)