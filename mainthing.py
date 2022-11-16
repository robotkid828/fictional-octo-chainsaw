__version__ = 'dev'
def DoTheThing():
  GameID = input("Game ID?\n")
  Username = input("Username?\n")

  from selenium import webdriver
  from selenium.webdriver.chrome.options import Options
  from selenium.webdriver.common.keys import Keys
  import time

  Router = "213.32.112.122:8080"
  chrome_options = Options()
  chrome_options.add_argument("--no-sandbox")
  chrome_options.add_argument(f"--proxy-server={Router}")

  driver = webdriver.Chrome(options=chrome_options)
  driver.get('https://play.blooket.com/play')

  GameIDXPath = '//*[@id="app"]/div/div/div[2]/div/form/div[2]/div[1]/input'
  NextXPath = '//*[@id="app"]/div/div/div[2]/div/form/div[2]/div[2]/i'
  driver.find_element("xpath", GameIDXPath).send_keys(GameID)
  driver.find_element("xpath", NextXPath).click()

  UsernameXPath = '//*[@id="app"]/div/div/div[2]/div/form/div[2]/input'
  NextXPath = '//*[@id="app"]/div/div/div[2]/div/form/div[2]/div/i'
  driver.find_element("xpath", UsernameXPath).send_keys(Username)
  driver.find_element("xpath", NextXPath).click()

  Start = input("Please press enter when the game starts. (After instructions.)\n")
  time.sleep(15)

  PasswordXPath = '//*[@id="app"]/div/div/div[2]/div[3]/div[3]/div[1]'
  driver.find_element("xpath", PasswordXPath).click()
  time.sleep(8)

  Answers = {}

  while True:
    QuestionXPath = '//*[@id="app"]/div/div/div[3]/div/div[2]/div/div'
    Answer1XPath = '//*[@id="answer0"]/div/div/div'
    Answer2XPath = '//*[@id="answer1"]/div/div/div'
    Answer3XPath = '//*[@id="answer2"]/div/div/div'
    Answer4XPath = '//*[@id="answer3"]/div/div/div'
    Question = driver.find_element("xpath", QuestionXpath)
    Answer1 = driver.find_element("xpath", Answer1XPath)
    Answer2 = driver.find_element("xpath", Answer2XPath)
    Answer3 = driver.find_element("xpath", Answer3XPath)
    Answer4 = driver.find_element("xpath", Answer4XPath)
    if Question in Answers:
      if Answer1 == Answers[Question]:
        Answer1XPath.click()
      if Answer2 == Answers[Question]:
        Answer2XPath.click()
      if Answer3 == Answers[Question]:
        Answer3XPath.click()
      if Answer4 == Answers[Question]:
        Answer4XPath.click()
      time.sleep(1)
      Correct = True
    else:
      Answer1XPath.click()
      time.sleep(1)
      if driver.find_element("xpath", '//*[@id="feedbackButton"]/div[2]') == "CORRECT":
        Answers[Question] = driver.find_element("xpath", Answer1)
        time.sleep(1)
        Correct = True
      else:
        time.sleep(2)
        Answers[Question] = driver.find_element("xpath", '//*[@id="feedbackButton"]/div[4]/div/span')
        time.sleep(2)
        Correct = False
    driver.find_element("xpath", '//*[@id="feedbackButton"]').click()
    if Correct:
      driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/div[3]/div[2]/div').click()
      time.sleep(1)
      driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/div[3]')
