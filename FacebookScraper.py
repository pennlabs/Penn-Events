from lxml import html
import requests

page = requests.get('https://www.facebook.com/events/271388601195325/?active_tab=about')
tree = html.fromstring(page.content)
