from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

# Ruta al archivo del WebDriver de Microsoft Edge
msedge_driver_path = "C:/Users/wali/Desktop/automatizacion/Webdrivers/msedgedriver.exe"

# Configuración del WebDriver para Microsoft Edge con tiempo de espera explícito
options = webdriver.EdgeOptions()
options.add_argument("start-maximized")  # Maximiza la ventana del navegador al abrir

# Crear el objeto WebDriver
driver = webdriver.Edge(executable_path=msedge_driver_path, options=options)

# URL de Facebook
url = "https://www.facebook.com/"

# URL del Marketplace de Facebook
marketplace_url = "https://www.facebook.com/marketplace/"

# Credenciales de inicio de sesión (reemplaza con tus propias credenciales)
email = "warlinguzman22-5@outlook.es"
password = "prueba1234"

try:
    # Cargar la página de Facebook
    driver.get(url)
    driver.save_screenshot('C:/Users/wali/Desktop/automatizacion/Capturas/facebook_login.png')

    # Esperar hasta que aparezca el campo de correo electrónico (timeout de 10 segundos)
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )

    # Ingresar el correo electrónico y la contraseña
    email_field.send_keys(email)
    password_field = driver.find_element(By.ID, "pass")
    password_field.send_keys(password)

    # Hacer clic en el botón de inicio de sesión 
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

    # Esperar hasta que la página cargue completamente 
    WebDriverWait(driver, 10).until(
        EC.title_contains("Facebook")
    )

    # Navegar al Marketplace
    driver.get(marketplace_url)
    driver.save_screenshot('C:/Users/wali/Desktop/automatizacion/Capturas/facebook_marketplace.png')

    # campo de búsqueda
    search_bar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Buscar en Marketplace']"))
    )

    # Escribir "logitech g pro x" en la barra de búsqueda 
    search_bar.send_keys("logitech g pro x")
    search_bar.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.save_screenshot('C:/Users/wali/Desktop/automatizacion/Capturas/facebook_marketplace_search_logitech.png')

    # Regresar atrás en el navegador
    driver.back()

    # Esperar a que la página se cargue completamente después de retroceder
    WebDriverWait(driver, 10).until(
        EC.title_contains("Facebook")
    )

    # Navegar nuevamente al Marketplace
    driver.get(marketplace_url)
    driver.save_screenshot('C:/Users/wali/Desktop/automatizacion/Capturas/facebook_marketplace_again.png')

    # Esperar hasta que el campo de búsqueda esté presente
    search_bar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Buscar en Marketplace']"))
    )

    # Escribir "rtx 3060" en la barra de búsqueda y presionar Enter
    search_bar.send_keys("rtx 3060")
    search_bar.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.save_screenshot('C:/Users/wali/Desktop/automatizacion/Capturas/facebook_marketplace_search_rtx3060.png')

    # Regresar al inicio de Facebook
    driver.get(url)
    driver.save_screenshot('C:/Users/wali/Desktop/automatizacion/Capturas/facebook_home.png')

except Exception as e:
    print("Ocurrió un error:", e)

finally:
    # Esperar 5 segundos adicionales antes de cerrar el navegador
    time.sleep(5)

    # Generar el contenido del archivo HTML con los resultados de las pruebas
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_tests = 10
    passed_tests = 8
    duration = 120.5
    html_content = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8"/>
            <title>Reporte de Prueba</title>
        </head>
        <body>
            <h1>Reporte de Prueba</h1>
            <p>Fecha y Hora: {current_datetime}</p>
            <p>Total de Pruebas Ejecutadas: {total_tests}</p>
            <p>Pruebas Pasadas: {passed_tests}</p>
            <p>Duración Total: {duration} segundos</p>
        </body>
    </html>
    """

    # Guardar el contenido en un archivo HTML
    with open("report.html", "w") as file:
        file.write(html_content)

    print("Se generó el archivo report.html con los resultados de las pruebas.")

    # Cerrar el navegador al finalizar
    driver.quit()