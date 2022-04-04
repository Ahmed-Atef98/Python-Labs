import webbrowser
import random

websites = ["google", "github", "amazon"]
website = websites[random.randrange(0, len(websites))]
webbrowser.open("https://" + website + ".com/")