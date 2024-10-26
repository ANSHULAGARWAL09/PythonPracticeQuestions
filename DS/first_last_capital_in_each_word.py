from selenium.webdriver.chrome.service import service
from pytest_bdd import

s = "welcome to geeksforgeeks"



splito = s.split()
list = []

for i in splito:
    end = i[0].capitalize() + i[1:-1]+i[-1].capitalize()
    o = list.append(end)

print(" ".join(list))