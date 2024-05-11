import pytest 
from time import sleep 
import subprocess 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    # iniciar o streamlit em background 
    process = subprocess.Popen(['streamlit','run','src/app.py'])
    options = Options()
    # options.headless = True
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options = options)
    #iniciar o webdriver usando GeckoDriver
    driver.set_page_load_timeout(5)
    yield driver 

    # fechar o webdriver e o streamlit após o teste
    driver.quit()
    process.kill()


def test_app_opens(driver):
    # verificar se a página abre 
    driver.get('http://localhost:8501')
    sleep(5)


def test_check_title_sis(driver):
    #verificar se a página abre 
    driver.get('http://localhost:8501')
    sleep(2) 
    # titulo da página 
    page_title = driver.title

    # verificar se é o esperado
    expected_title = 'Validador de schema excel'
    assert page_title == expected_title


# def test_check_streamlit_h1(driver):
#     driver.get('http://localhost:8501')
#     sleep(2)
#     h1_element = driver.find_element(By.TAG_NAME,'h1')
#     expected_text = 'Carregue seu arquivo EXCEL aqui'
#     assert h1_element == expected_text

