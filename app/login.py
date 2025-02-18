import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time


options = Options()
options.add_argument('--headless') 
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=Service (ChromeDriverManager().install()), options=options)


load_dotenv()


# Obtiene ambas credenciales de Instagram desde las variables de entorno
user = os.getenv('USER')
password = os.getenv('PASSWORD')

# Verificar que se hayan cargado correctamente las credenciales
if not user or not password:
    print("Error: Las credenciales de Instagram no están configuradas correctamente en el archivo .env.")
    exit()

# Configura el navegador Chrome con Selenium y ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


url = 'https://www.instagram.com/accounts/login/'
driver.get(url)

# Espera a que los elementos se carguen....
time.sleep(3)

# Localiza los campos de usuario y contraseña
username_field = driver.find_element(By.NAME, 'username')
password_field = driver.find_element(By.NAME, 'password')

# Completa los campos de usuario y contraseña
username_field.send_keys(user)
password_field.send_keys(password)

# Envía el formulario
password_field.send_keys(Keys.RETURN)

# Espera a que la página de inicio se cargue
time.sleep(40)

# Después de iniciar sesión y esperar a que la página cargue
try:
    # Buscar el icono del perfil por texto
    profile_icon = driver.find_element(By.XPATH, '//span[text()="Perfil"]')
    # O bien buscarlo por el atributo aria-label (si el texto no funciona)
    # profile_icon = driver.find_element(By.XPATH, '//span[@aria-label="Perfil"]')
    
    # Hacer clic en el perfil
    profile_icon.click()
    print("Accediendo al perfil...")
    
    # Espera unos segundos para asegurarse de que se ha accedido al perfil
    time.sleep(5)
    
    # Verifica que estás en la página de perfil
    print(f"Estás en: {driver.current_url}")
    
except Exception as e:
    print(f"Error al intentar acceder al perfil: {e}")



# Espera algunos segundos antes de cerrar el navegador
time.sleep(5)
input("Presiona Enter para cerrar el navegador...")

# Cerrar el navegador
driver.quit()
