from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    # Nu se poate face pentru ca https://www.crunchbase.com/ detecteaza selenium si nu te lasa sa faci scrapping
    # Nu merge nici cu schimbat de User_Agent
    # Articol care descrie ce au facut baietii:
    # https://resources.distilnetworks.com/bot-defense-for-digital-publishing/online-directory-cuts-pageviews-in-half-by-blocking-bots-crunchbase-case-study

    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      "Chrome/66.0.3359.139 Safari/537.36")
    driver = webdriver.Chrome(options=opts)
    driver.set_window_position(0, 0)
    driver.set_window_size(100, 400)
    driver.get("https://www.crunchbase.com/organization/netflix")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    name = driver.find_elements_by_xpath("//*[@id='section-overview']/mat-card/div[2]/div/image-with-fields-card/image-with-text-card/div/div/div[2]/div[1]/field-formatter/blob-formatter/span")

    print(name)
    driver.quit()


if __name__ == '__main__':
    main()
