# A simple tool to extract tweets from a public Twitter profile
# Modules: twint
# pip install twint

import twint

# configure twint object
t = twint.Config()

t.Username = "billycodes"
twint.run.Followers(t)

