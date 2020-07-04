from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# Check if given XPATH exists
def check_fail(x_path):
    try:
        driver.find_element_by_xpath(x_path)
        return True
    except:
        return False

# Follow XPATH naming convention, function of #paragraph and whether button clicked
def getREV_ID_P(rev_id,j,button_cond):

    # If this is the first paragraph of the review
    if j==1:
        # First assume there is a single p
        rev_id_p = rev_id + '/div/div[2]/p'
        single_p = check_fail(rev_id_p)

        # if there is more than 1 p, name accordingly
        if not single_p:
            # Clicking the expand button changes syntax
            if button_cond:
                rev_id_p = rev_id + '/div/div[2]/p[1]'
            else:
                rev_id_p = rev_id + '/div/div[2]/div/p[1]'
    else:
        # Clicking the expand button changes syntax
        if button_cond:
            rev_id_p = rev_id + '/div/div[2]/p[' + str(j) + ']'
        else:
            rev_id_p = rev_id + '/div/div[2]/div/p[' + str(j) + ']'
    return rev_id_p


def getReviews(film_url,page_max):

    driver.get(film_url + "reviews/by/activity/")

    page_count = 1

    while page_count < page_max:

        # Wait for first review to load
        WebDriverWait(driver, 250).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content"]/div/div/section/section/ul/li[1]/div/div[2]')))
        

        rev_cond = True
        i = 1
        rev_id = '//*[@id="content"]/div/div/section/section/ul/li[' + str(i) + ']'
        
        review_list = ['1']
        
        while rev_cond:
            
            j = 1
            par_cond = True     # Assume there exists a first paragraph
            button_cond = False  # Assume there is no button
        
            review_temp = ['1']
        
            rev_id_p = getREV_ID_P(rev_id,j,button_cond)
        
            while par_cond:
            
                # If the button has not been pressed yet,
                if not button_cond:
                    # check if it exists in this paragraph.
                    button_cond = check_fail(rev_id_p + '/a')
                    # If the button exists here,
                    if button_cond:
                        # then press it.
                        button_txt = driver.find_element_by_xpath(rev_id_p + '/a').text
        
                        if (button_txt=='more') or (button_txt=='I can handle the truth.'):
                            driver.find_element_by_xpath(rev_id_p + '/a').click()
                            rev_id_p = getREV_ID_P(rev_id,j,button_cond)
                        else:
                            button_cond = False
        
        
                # Now, add the current paragraph to this review
                if j==1:
                    WebDriverWait(driver, 250).until(EC.presence_of_element_located((By.XPATH,rev_id_p)))
                    review_temp[0] = driver.find_element_by_xpath(rev_id_p).text
                else:
                    WebDriverWait(driver, 250).until(EC.presence_of_element_located((By.XPATH,rev_id_p)))
                    review_temp.append(driver.find_element_by_xpath(rev_id_p).text)
        
                # Now, check that the nExt paragraph exists
                j += 1
                rev_id_p = getREV_ID_P(rev_id,j,button_cond)
                par_cond = check_fail(rev_id_p)
                        
            # Add the gathered review to our database
            if i==1:
                review_list[0] = review_temp
            else:
                review_list.append(review_temp)
        
            # Check if there is a next review on this page
            i += 1
            rev_id = '//*[@id="content"]/div/div/section/section/ul/li[' + str(i) + ']'
            rev_cond = check_fail(rev_id)

        # Click to the next page of reviews
        next = '//*[@id="content"]/div/div/section/section/div/div[2]/a'
        driver.find_element_by_xpath(next).click()
        page_count += 1

    # Close the browser and return the list of reviews
    driver.quit()
    return review_list