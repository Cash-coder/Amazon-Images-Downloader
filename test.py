import re

s = ''''colorImages': { 'initial': [{"hiRes":"https://m.media-amazon.com/images/I/51O0OFy6izL._AC_SL1200_.jpg","thumb":"https://m.media-amazon.com/images/I/31X8TijgJrL._AC_US40_.jpg","large":"https://m.media-amazon.com/images/I/31X8TijgJrL._AC_.jpg","main":{"https://m.media-amazon.com/images/I/51O0OFy6izL._AC_SY355_.jpg":[355,355],"https://m.media-amazon.com/images/I/51O0OFy6izL._AC_SY450_.jpg":[450,450],"https://m.media-amazon.com/images/I/51O0OFy6izL._AC_SX425_.jpg":[425,425],"https://m.media-amazon.com/images/I/51O0OFy6izL._AC_SX466_.jpg":[466,466],"https://m.media-amazon.com/images/I/51O0OFy6izL._AC_SX522_.jpg":[522,522],"https://m.media-amazon.com/images/I/51O0OFy6izL._AC_SX569_.jpg":[569,569],"https://m.media-amazon.com/images/I/51O0OFy6izL._AC_SX679_.jpg":[679,679]},"variant":"MAIN","lowRes":null,"shoppableScene":null},{"hiRes":"https://m.media-amazon.com/images/I/714FBXL+C0L._AC_SL1500_.jpg","thumb":"https://m.media-amazon.com/images/I/41rfkJ3wmjL._AC_US40_.jpg","large":"https://m.media-amazon.com/images/I/41rfkJ3wmjL._AC_.jpg","main":{"https://m.media-amazon.com/images/I/714FBXL+C0L._AC_SX355_.jpg":[253,355],"https://m.media-amazon.com/images/I/714FBXL+C0L._AC_SX450_.jpg":[321,450],"https://m.media-amazon.com/images/I/714FBXL+C0L._AC_SX425_.jpg":[303,425],"https://m.media-amazon.com/images/I/714FBXL+C0L._AC_SX466_.jpg":[333,466],"https://m.media-amazon.com/images/I/714FBXL+C0L._AC_SX522_.jpg":[373,522],"https://m.media-amazon.com/images/I/714FBXL+C0L._AC_SX569_.jpg":[406,569],"https://m.media-amazon.com/images/I/714FBXL+C0L._AC_SX679_.jpg":[485,679]},"variant":"PT01","lowRes":null,"shoppableScene":null},{"hiRes":"https://m.media-amazon.com/images/I/61O4tsbSJoL._AC_SL1200_.jpg","thumb":"https://m.media-amazon.com/images/I/41f7gpLSnbL._AC_US40_.jpg",'''

# m = re.search(r'hiRes(.*?).jpg',s).group(1)
# for e in m:
#     print(e)

a,b = s.find('hiRes'), s.find('.jpg')
e = s[a+6:b]
print(e)