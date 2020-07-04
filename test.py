from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

def check_fail(x_path):
    try:
        driver.find_element_by_xpath(x_path)
        return True
    except:
        return False

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


def getReviews(reviewPage_url):

    driver.get(reviewPage_url)

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
                review_temp[0] = driver.find_element_by_xpath(rev_id_p).text
            else:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,rev_id_p)))
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