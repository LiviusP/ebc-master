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
    driver.get("http://www.metacritic.com/movie/inception")
    regizor = driver.find_elements_by_xpath("//*[@id='mantle_skin']/div[4]/div[1]/div/div[1]/div[2]/div[2]/div[5]/div[1]/a/span")
    durata = driver.find_elements_by_xpath("//*[@id='mantle_skin']/div[4]/div[1]/div/div[1]/div[2]/div[2]/div[5]/div[4]/span[2]")
    scorcritici = driver.find_elements_by_xpath("//*[@id='nav_to_metascore']/div[1]/div[2]/div[1]/a/div")
    scorutilizatori = driver.find_elements_by_xpath("//*[@id='nav_to_metascore']/div[2]/div[2]/div[1]/a/div")
    
    regizorText = [x.text for x in regizor]
    durataText = [x.text for x in durata]
    scorcriticiText = [x.text for x in scorcritici]
    scorutilizatoriText = [x.text for x in scorutilizatori]


    print("Regizor: {}, Durata: {}, Scorcritici {}, ScorUtilizatori {}".format(regizorText, durataText, scorcriticiText, scorutilizatoriText))
    driver.quit()


if __name__ == '__main__':
    main()
