def getFollowing(user):
    driver.get("https://twitter.com/"+user+"/following")
    time.sleep(2)
    notfollowing = []
    notfollowing.append(driver.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[5]/aside/div[2]/div[1]/div/div[2]/div/div[1]/a/div/div[2]/div/span").text)
    notfollowing.append(driver.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[5]/aside/div[2]/div[2]/div/div[2]/div/div[1]/a/div/div[2]/div/span").text)
    notfollowing.append(driver.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[5]/aside/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div/span").text)
  

    following = []
    temp = driver.find_elements_by_xpath("//div[@data-testid='UserCell']//div/div[2]/div/div[1]/a/div/div[2]/div")
    time.sleep(1)
  
    for i in temp:
        if i.text not in following and i.text != "Follows you" and i.text not in notfollowing:
            following.append(i.text)

    count = 0 
    last_y = len(following)
    while True:
        driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
        time.sleep(2)

        temp = driver.find_elements_by_xpath("//div[@data-testid='UserCell']//div/div[2]/div/div[1]/a/div/div[2]/div")
        time.sleep(2)

        for i in temp:
            if i.text not in following and i.text != "Follows you" and i.text not in notfollowing:
                following.append(i.text)
        new_y = len(following)

        count +=1
        if count == 5:
            count = 0
            if last_y == new_y:
                break
            else:
                last_y=new_y
                print(last_y)

    return following
