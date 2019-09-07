from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import itertools
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','UdemyFreeCourses.settings')

django.setup()


from blog.models import Course


url="https://www.udemy.com/courses/development/?"
second="price=price-free&sort=popularity"
driver = webdriver.Chrome("C:\\Users\\PRAJWAL\\Desktop\\Udemy_affiliate\\chromedriver.exe")
driver.maximize_window()

# driver.get(url+second)
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='list-view-course-card--course-card-wrapper--TJ6ET']>a>div>div>div>h4")));
#
# actions = ActionChains(driver)
# for _ in range(8):
#     actions.send_keys(Keys.SPACE).perform()
#     time.sleep(1)
#
# names = driver.find_elements_by_css_selector("div[class='list-view-course-card--course-card-wrapper--TJ6ET']>a>div>div>div>h4")
# links = driver.find_elements_by_css_selector("div[class='list-view-course-card--course-card-wrapper--TJ6ET']>a")
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='list-view-course-card--course-card-wrapper--TJ6ET']>a>div>div>img")));
# imgs = driver.find_elements_by_css_selector("div[class='list-view-course-card--course-card-wrapper--TJ6ET']>a>div>div>img")
#
# for (name,link,img) in itertools.zip_longest(names,links,imgs):
#     print(name.text,',',link.get_attribute('href'),',',img.get_attribute('srcset').split(',')[1].split(' ')[1])

for i in range(1,15):
    if i==0 or i==1:
        driver.get(url + second)
    else:
        driver.get(url+'p='+str(i)+'&' + second)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "div[class='list-view-course-card--course-card-wrapper--TJ6ET']>a>div>div>div>h4")));

    actions = ActionChains(driver)
    for _ in range(8):
        actions.send_keys(Keys.SPACE).perform()
        time.sleep(3)

    names = driver.find_elements_by_css_selector(
        "div[class='list-view-course-card--course-card-wrapper--TJ6ET']>a>div>div>div>h4")
    links = driver.find_elements_by_css_selector("div[class='list-view-course-card--course-card-wrapper--TJ6ET']>a")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='list-view-course-card--course-card-wrapper--TJ6ET']>a>div>div>img")));
    imgs = driver.find_elements_by_css_selector("div[class='list-view-course-card--course-card-wrapper--TJ6ET']>a>div>div>img")
    taglines = driver.find_elements_by_css_selector("div[class='list-view-course-card--headline-and-instructor--2nbyp']>span:first-of-type")
    authors = driver.find_elements_by_css_selector("div[class='list-view-course-card--headline-and-instructor--2nbyp']>span:nth-of-type(2)")
    for (name,link,img,tagline,author) in itertools.zip_longest(names,links,imgs,taglines,authors):
        print(name.text, ',', link.get_attribute('href'), ',', img.get_attribute('srcset').split(',')[1].split(' ')[1],',',tagline.text,',',author.text)
        # content=f"{name.text}, {link.get_attribute('href')},{img.get_attribute('srcset').split(',')[1].split(' ')[1]},{tagline.text},{author.text},\n"
        # f=open('udemy.txt','a')
        # f.writelines(content)
        # f.close()
        Course.objects.get_or_create(name=name.text,course_link=link.get_attribute('href'),img_link=img.get_attribute('srcset').split(',')[1].split(' ')[1],website="https://www.udemy.com/",course_content=tagline.text,author=author.text)




# try:
#     time.sleep(10)
#     driver.get(url + 'p='+str(i)+'&'+ second)
#     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='list-view-course-card--course-card-wrapper--TJ6ET']>a>div>div>div>h4")));
#     fastrack = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[class='pagination pagination-expanded']>li:last-of-type>a")));
#     fastrack.click()
#     driver.find_element_by_css_selector("ul[class='pagination pagination-expanded']>li:last-of-type>a").click()
# except:
#     print()


# fastrack = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//a[@data-tracking-id='0_Fastrack']")));
# fastrack.click()

# time.sleep(5)
# imgs = driver.find_elements_by_css_selector("div[class='list-view-course-card--course-card-wrapper--TJ6ET']>a>div>div>div>h4")
# for img in imgs:
#     print(img.text)

#
# imglist = driver.find_elements_by_css_selector('list-view-course-card--course-card-wrapper--TJ6ET')
#
# content = driver.page_source.encode('utf-8').strip()
# soup = BeautifulSoup(content,"html.parser")
# courseLink = soup.findAll("h4")

# for link in courseLink:
    # print(baseurl+link['href'])

driver.quit()

# with open('somefile.txt', 'w') as the_file:
#     the_file.write(courseLink)

#document.querySelectorAll('.list-view-course-card--course-card-wrapper--TJ6ET a img')[0].getAttribute('srcset').split(",")[1]

#document.querySelectorAll('h4')[0].innerText

#"https://www.udemy.com"+document.querySelectorAll('.list-view-course-card--course-card-wrapper--TJ6ET a')[0].getAttribute('href')
