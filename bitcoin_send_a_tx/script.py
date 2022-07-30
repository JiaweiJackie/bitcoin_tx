from requests_html import HTMLSession

session = HTMLSession()

response = session.get('https://www.blockchain.com/btc/tx/4645603184e112828bf9a52275deb01e501635589ea02af8e3c4e12fbff9e16c')

with open("parse result.txt","w") as f:
    f.write(response.html.full_text)
