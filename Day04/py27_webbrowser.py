import webbrowser

print(webbrowser.get())

# 크롬 브라우저로 네이버 띄우기
url = 'http://www.naver.com'
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)
# webbrowser.open(url) # 원래 이거만 해도 떠야하는데 실습 때는 안뜸 !!