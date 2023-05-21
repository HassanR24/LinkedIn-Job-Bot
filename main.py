import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

executable_path = "/Users/macintosh/Development/chromedriver"
#replace the path above with your own driver path
ser = Service(executable_path=executable_path)
options = webdriver.ChromeOptions()

USERNAME = ""       #insert your linkedin Email Address
PASSWORD = ""       #insert your linkedin Password

driver = webdriver.Chrome(service=ser)
url = "https://www.linkedin.com/jobs/search/?currentJobId=3490731593&f_AL=true&f_E=1%2C2%2C3&geoId=102105699" \
      "&keywords=python%20developer&location=Turkey&refresh=true&sortBy=R"
#change the above with the link according to your preferrences

driver.get(url)
time.sleep(5)


def login():

    driver.find_element(By.XPATH, '/html/body/div[3]/a[1]').click()
    driver.find_element(By.ID, "username").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "form div button").click()
    time.sleep(10)


def apply_jobs():

    job_listing = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")
    for job in job_listing:
        job.click()
        time.sleep(2)
        try:
            easy_apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
            easy_apply_button.click()
            time.sleep(2)
            next_button = driver.find_element(By.CSS_SELECTOR, "footer button")
            if next_button.get_attribute("aria-label") == "Submit application":
                close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
                close_button.click()
                time.sleep(2)
                discard_button = driver.find_elements(By.CSS_SELECTOR, ".artdeco-modal__actionbar--confirm-dialog button")[0]
                discard_button.click()
                pass
                time.sleep(2)
            else:
                next_button.click()
                time.sleep(2)
                choose_resume_button = driver.find_element(By.CSS_SELECTOR, ".jobs-resume-picker__resume-btn-container button")
                choose_resume_button.click()
                time.sleep(2)
                review_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
                if review_button.get_attribute("aria-label") != "Review your application":
                    print("Complex Application")
                    close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
                    close_button.click()
                    time.sleep(2)
                    discard_button = driver.find_element(By.CLASS_NAME, "artdeco-button--secondary")
                    discard_button.click()
                    time.sleep(2)
                else:
                    review_button.click()
                    time.sleep(2)
                    submit_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
                    submit_button.click()
                    print("Application Submitted")
                    time.sleep(5)
                    close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
                    close_button.click()
                    time.sleep(2)

        except selenium.common.exceptions.NoSuchElementException:
            pass


login()
apply_jobs()
