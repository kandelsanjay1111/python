from bs4 import BeautifulSoup
with open("home.html", "r") as html_file:
    html_text=html_file.read()
    soup = BeautifulSoup(html_text,'lxml')

    #find and find_all method

    # headings = soup.find_all("h5")
    # for heading in headings:
    #     print(heading.text)

    courses=soup.find_all("div",class_="card")
    for course in courses:
        title=course.h5.text
        price=course.a.text.split()[-1]
        print(title)
        print(price)

# https://www.youtube.com/watch?v=XVv6mJpFOb0&t=747s