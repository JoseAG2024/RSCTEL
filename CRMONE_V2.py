from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

import time


# Función para iniciar el navegador
class Navegador:
    def __init__(self, url):
        self.url = url
        self.driver = None

    def iniciar_navegador(self):
        opciones = webdriver.ChromeOptions()
        opciones.add_argument("--disable-extensions")
        opciones.add_argument("--headless=new")
        opciones.add_argument("--disable-gpu")
        opciones.add_argument("--disable-blink-features=AutomationControlled")
        opciones.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
        opciones.add_experimental_option("detach", True)
        # Se mantiene en modo normal (no headless)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opciones)

    def navegar(self):
        if self.driver is None:
            self.iniciar_navegador()
        self.driver.get(self.url)

    def cerrar_navegador(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
        
class LoginCRM:
    def __init__(self, driver):
        #restablecemos los valores de las variables
        #comenzamos con la url
        self.driver = driver
        
        #bajamos como si estuviesemos recorriendo el arbol del html
        #reiniciamos el nombre de usuario, su valor, su tipo de selector y su selector
        self.usuario_value=None
        self.usuario_selectorType=None
        self.usuario_selector = None
        #hacemos lo mismo pero para el campo contraseña
        self.contraseña_value=None
        self.contraseña_selectorType=None
        self.contraseña_selector = None
        
        #El boton solo necesitamos su tipo de selector y su selector
        self.btningresar_selectorType=None
        self.btningresar_selector=None
        
        #restablecemos el valor del estado del inicio de sesion.
        self.estado_login = None
        
    #Establecemos las propiedades referentes al USUARIO
    def usuario_edit(self, value, selectorType,selector):
        """
        Aqui establecemos todas las propiedades del objeto USUARIO
        
        value: Valor que se escribira en el TextEdit
        selectorType: Tipo de selector que se pasara como parametro para ser procesado el campo a trave
        de la biblioteca de Selenium
        selector: Selector que se usara para encontrare el control dentro de la pagina del CRM. Este esta ligado al tipo de selector
        que le envies a la funcion.
        
        VALORES VALIDOS PARA Selector Type:
        ID = "id"
        XPATH = "xpath"
        LINK_TEXT = "link text"
        PARTIAL_LINK_TEXT = "partial link text"
        NAME = "name"
        TAG_NAME = "tag name"
        CLASS_NAME = "class name"
        CSS_SELECTOR = "css selector"
        """
        self.usuario_value = value
        self.usuario_selectorType=selectorType
        self.usuario_selector=selector

    def contraseña_edit(self, value, selectorType, selector):
        """
        Aqui establecemos todas las propiedades del objeto CONTRASEÑA
        
        value: Valor que se escribira en el TextEdit
        selectorType: Tipo de selector que se pasara como parametro para ser procesado el campo a traves
        de la biblioteca de Selenium
        selector: Selector que se usara para encontrare el control dentro de la pagina del CRM. Este esta ligado al tipo de selector
        que le envies a la funcion.
        
        VALORES VALIDOS PARA Selector Type:
        ID = "id"
        XPATH = "xpath"
        LINK_TEXT = "link text"
        PARTIAL_LINK_TEXT = "partial link text"
        NAME = "name"
        TAG_NAME = "tag name"
        CLASS_NAME = "class name"
        CSS_SELECTOR = "css selector"
        """
        self.contraseña_value = value
        self.contraseña_selectorType=selectorType
        self.contraseña_selector=selector
    
    def ingresar_button(self,selectorType, selector ):
        """
        Aqui establecemos todas las propiedades del objeto CONTRASEÑA
        
        value: Valor que se escribira en el TextEdit
        selectorType: Tipo de selector que se pasara como parametro para ser procesado el campo a traves
        de la biblioteca de Selenium
        selector: Selector que se usara para encontrare el control dentro de la pagina del CRM. Este esta ligado al tipo de selector
        que le envies a la funcion.
        
        VALORES VALIDOS PARA Selector Type:
        ID = "id"
        XPATH = "xpath"
        LINK_TEXT = "link text"
        PARTIAL_LINK_TEXT = "partial link text"
        NAME = "name"
        TAG_NAME = "tag name"
        CLASS_NAME = "class name"
        CSS_SELECTOR = "css selector"
        """
        self.btningresar_selector=selector
        self.btningresar_selectorType=selectorType
    
    def etiqueta_Login_Incorrecto(self,selectorType, selector):
        self.etiqueta_Login_Incorrecto_selectorType=selectorType
        self.etiqueta_Login_Incorrecto_selector=selector


    def loguearse(self):
        # Esperar hasta que el campo de usuario esté presente
        # Realizar acciones como login
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.usuario_selectorType, self.usuario_selector))
        ).send_keys(self.usuario_value)
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.contraseña_selectorType, self.contraseña_selector))
        ).send_keys(self.contraseña_value)
        # Hacer clic en el botón de iniciar sesión esperar hasta que el boton desaparezca el boton mismo o aparexzca la etiqueta que me indica error de logon
        boton_login=WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.btningresar_selectorType, self.btningresar_selector))
        )
        boton_login.click()
        try:
            # Esperar hasta que el botón desaparezca o aparezca el mensaje de error
            WebDriverWait(self.driver, 10).until(
                EC.any_of(
                    EC.invisibility_of_element(boton_login),  # Espera que desaparezca el botón
                    EC.presence_of_element_located((self.etiqueta_Login_Incorrecto_selectorType, self.etiqueta_Login_Incorrecto_selector))  # Espera que aparezca el mensaje de error
                )
            )
            # Verifica cuál de las dos condiciones se cumplió
            if not self.driver.find_elements(self.btningresar_selectorType, self.btningresar_selector):
                return True  # El botón desapareció (inicio de sesión exitoso o en proceso)
            elif self.driver.find_elements(self.etiqueta_Login_Incorrecto_selectorType, self.etiqueta_Login_Incorrecto_selector):
                self.driver.quit()
                return False  # Apareció el mensaje de error (inicio de sesión fallido)
        except Exception as e:
            self.driver.quit()
            return False  # Apareció el mensaje de error (inicio de sesión fallido)
        
        
class ClientesCRM:
    def __init__(self,driver):
        
        #restablecemos los valores de las variables
        
        #comenzamos con la url
        self.driver= driver
        
        #bajamos como si estuviesemos recorriendo el arbol del html
        #reiniciamos el boton nuevo cliente su tipo de selector y su selector
        self.nuevoCliente_button_selector=None
        self.nuevoCliente_button_selectorType=None
        
        #Inicializamos el TextEdit CIF/DNI del cliente
        self.CIFNIF_value = None
        self.CIFNIF_selectorType=None
        self.CIFNIF_selector=None
        
        #Incializamos las variables relativas al formulario de la ficha cliente nuevo.
        self.fichaCliente_selector=None
        self.fichaCliente_selectorType=None
        
        
        self.iconoResultadoBusquedaCliente_i_selector=None
        self.iconoResultadoBusquedaCliente_i_selectortype=None
        self.resultadoBusquedaCliente_labelSeletor=None
        self.resultadoBusquedaCliente_labelSelectorType=None
        
        self.crearCliente_button_selector=None
        self.crearCliente_button_selectorType=None
        
        self.RAZON_SOCIAL_editSelectorType=None
        self.RAZON_SOCIAL_editSelector=None
        self.RAZON_SOCIAL_editValue=None
    
    def fichaCliente(self, selectorType, selector):
        self.fichaCliente_selector=selector
        self.fichaCliente_selectorType=selectorType
        
    def CIFNIF_edit(self, selectorType, selector, value):
        """
        Aqui establecemos todas las propiedades del objeto CIFNIF
        
        value: Valor que se escribira en el TextEdit
        selectorType: Tipo de selector que se pasara como parametro para ser procesado el campo a traves
        de la biblioteca de Selenium
        selector: Selector que se usara para encontrare el control dentro de la pagina del CRM. Este esta ligado al tipo de selector
        que le envies a la funcion.
        
        VALORES VALIDOS PARA Selector Type:
        ID = "id"
        XPATH = "xpath"
        LINK_TEXT = "link text"
        PARTIAL_LINK_TEXT = "partial link text"
        NAME = "name"
        TAG_NAME = "tag name"
        CLASS_NAME = "class name"
        CSS_SELECTOR = "css selector"
        """
        self.CIFNIF_value = value
        self.CIFNIF_selectorType=selectorType
        self.CIFNIF_selector=selector
    
    def RAZON_SOCIAL_edit(self,selectorType, selector, value):
        self.RAZON_SOCIAL_editSelectorType=selectorType
        self.RAZON_SOCIAL_editSelector=selector
        self.RAZON_SOCIAL_editValue=value
    
    def iconoResultadoBusquedaCliente_i(self, selectorType,selector):
        self.iconoResultadoBusquedaCliente_i_selector=selector
        self.iconoResultadoBusquedaCliente_i_selectortype=selectorType
    
    def resultadoBusquedaCliente_label(self, selectorType, selector):
        self.resultadoBusquedaCliente_labelSeletor=selector
        self.resultadoBusquedaCliente_labelSelectorType=selectorType
    
    def crearCliente_button(self, selectorType, selector):
        self.crearCliente_button_selector=selector
        self.crearCliente_button_selectorType=selectorType
    
    def nuevoCliente_button(self,selectorType, selector ):
        """
        Aqui establecemos todas las propiedades del objeto Nuevo Cliente
        
        selectorType: Tipo de selector que se pasara como parametro para ser procesado el campo a traves
        de la biblioteca de Selenium
        selector: Selector que se usara para encontrare el control dentro de la pagina del CRM. Este esta ligado al tipo de selector
        que le envies a la funcion.
        
        VALORES VALIDOS PARA Selector Type:
        ID = "id"
        XPATH = "xpath"
        LINK_TEXT = "link text"
        PARTIAL_LINK_TEXT = "partial link text"
        NAME = "name"
        TAG_NAME = "tag name"
        CLASS_NAME = "class name"
        CSS_SELECTOR = "css selector"
        """
        self.nuevoCliente_button_selector=selector
        self.nuevoCliente_button_selectorType=selectorType
        
    def btnAbrirFichaCliente_Click(self):
         # Esperar hasta que el boton este presente
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.nuevoCliente_button_selectorType, self.nuevoCliente_button_selector))
        ).click()
    
    def btnCrearCliente_Click(self):

        # Esperar hasta que el panel ficha clientes este cargado
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.fichaCliente_selectorType, self.fichaCliente_selector))
        )

        time.sleep(2)
        # Hacer clic en Campo "CIF" y llenar los datos del cliente
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.CIFNIF_selectorType, self.CIFNIF_selector))
        ).send_keys(self.CIFNIF_value)


        #**********************************************************
        #**********************************************************
        #**********************************************************
        #**********************************************************
        #AQUI TENGO UN ERROR QUE OCURRE OCASIONALMENTE, NO LO HE PODIDO CONTROLAR.

        
        #Esperamos que aparezca el control a validar
        
        time.sleep(2)
        # Antes de verificar la etiqueta, verificamos si existe
        if WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.resultadoBusquedaCliente_labelSelectorType, self.resultadoBusquedaCliente_labelSeletor))):
            print("Ficha Cliente Abierta4")
            try:
                # Esperar a que el texto cambie de "Comprobando si ya existe..." o que el elemento desaparezca
                WebDriverWait(self.driver, 10).until(
                    lambda driver: 
                       driver.find_element(self.resultadoBusquedaCliente_labelSelectorType, self.resultadoBusquedaCliente_labelSeletor).text != "Comprobando si ya existe..." or
                       not driver.find_element(self.resultadoBusquedaCliente_labelSelectorType, self.resultadoBusquedaCliente_labelSeletor)
                )
                
                # Intentar acceder al elemento después de la espera
                try:
                    # Obtener el texto del elemento, asegurándose des que no esté desactualizado
                    span_element = WebDriverWait(self.driver, 10).until(
                        lambda driver: driver.find_element(self.resultadoBusquedaCliente_labelSelectorType,self.resultadoBusquedaCliente_labelSeletor)
                    )
                    etiqueta_texto = span_element.text if span_element else ""
                except StaleElementReferenceException:
                    etiqueta_texto = ""
            except TimeoutException:
                etiqueta_texto = ""
        else:
            etiqueta_texto = ""
        

                    
        #Creare una variable de control que indique si el cliente ya esta registrado en
        #CRM, sea porque ya existia o porque se agrego en el script
        cliente_Registrado=False
         #Verificamos el resultado de la busqueda y en base a ello ejecutamos acciones
        if etiqueta_texto == "Identificación existente!":
            #El cliente ya existe, procedemos a agregar la oportunidad
            print("Cliente Existe")
            #Establezco la variable de ClienteRegistrado a True
            cliente_Registrado=True
        elif etiqueta_texto == "Identificación no válida!" or etiqueta_texto == "Debe ser de 9 dígitos!":
            #El CIF o DNI es erroneo segun el CRM, mandamos mensaje de error
            print("Error en la identidad")
        elif etiqueta_texto == "":
            #El cliente no existe, procedemos a agregarlo
            print("Cliente no encontrado")
            # Hacer clic en Campo "RAZON SOCIAL" y llenar los datos del cliente
            self.driver.find_element(self.RAZON_SOCIAL_editSelectorType,self.RAZON_SOCIAL_editSelector).send_keys(self.RAZON_SOCIAL_editValue)
            
            #HABILITARE ESTO HASTA QUE YA LIBERE EL SCRIPT PARA EVITAR AÑADIR CLIENTES POR ERROR O POR PRUEBA
            self.driver.find_element(self.crearCliente_button_selectorType ,self.crearCliente_button_selector).click()
            cliente_Registrado= True
            
        if cliente_Registrado == False:
            print("RSCTEL Bot - Error","Ha ocurrido un error no controlado referente al registro del cliente")
            # Liberar archivo de bloqueo al finalizar el script
            exit
            
class crmOportunidades:
    def __init__(self, driver):
        #restablecemos los valores de las variables
        #comenzamos con la url
        self.driver = driver
        
        self.abrirFichaOportunidad_button_selectorType=None
        self.abrirFichaOportunidad_button_selector=None
        
        self.clienteCIF_edit_selectorType=None
        self.clienteCIF_edit_selector=None
        self.clienteCIF_edit_value=None
        
        self.buscarCliente_button_selectorType=None
        self.buscarCliente_button_selector=None
        
        self.cancelarBuscarCliente_button_selectorType=None
        self.cancelarBuscarCliente_button_selector=None
        
        self.crearOportunidad_button_selectorType=None
        self.crearOportunidad_button_selector=None
        
        self.panelFichaOportunidad_selectorType=None
        self.panelFichaOportunidad_selector=None
        
        self.cancelarOportunidad_button_selectorType=None
        self.cancelarOportunidad_button_selector=None
        
        self.configuracionFichaCliente_button_selectorType=None
        self.configuracionFichaCliente_button_selector=None
        
        self.configuracionesOportunidad_button_selectorType=None
        self.configuracionesOportunidad_button_selector=None
        
        self.configuraciones_catalogo_select_selectorType=None
        self.configuraciones_catalogo_select_selector=None
        self.configuraciones_catalogo_select_value=None
        
        self.configuraciones_usuarioAsignado_select_selectorType=None
        self.configuraciones_usuarioAsignado_select_selector=None
        self.configuraciones_usuarioAsignado_select_value=None
        
        self.guardarConfiguracionesOportunidad_button_selectorType=None
        self.guardarConfiguracionesOportunidad_button_selector=None
        
        self.abrirPaginaDelPedido_button_selectorType=None
        self.abrirPaginaDelPedido_button_selector=None
        
        
        #La parte de duplicar ficha
        self.preclonarOportunidad_button_selectorType=None
        self.preclonarOportunidad_button_selector=None
        self.clonarOportunidad_button_selectorType=None
        self.clonarOportunidad_button_selector=None
        self.ofertas_TabPage_selectorType=None
        self.ofertas_TabPage_selector=None
        
    #OBJETOS EN LA PAGINA PRINCIPAL DE OPORTUNIDADES    
    def abrirFichaOportunidad_button(self,selectorType,selector):
        self.abrirFichaOportunidad_button_selectorType=selectorType
        self.abrirFichaOportunidad_button_selector=selector
    
    def configuracionFichaCliente_button(self, selectorType, selector):
        self.configuracionFichaCliente_button_selectorType=selectorType
        self.configuracionFichaCliente_button_selector=selector
    
    def configuracionesOportunidad_button(self, selectorType, selector):
        self.configuracionesOportunidad_button_selectorType=selectorType
        self.configuracionesOportunidad_button_selector=selector
    
    def abrirPaginaDelPedido_button(self,selectorType, selector):
        self.abrirPaginaDelPedido_button_selectorType=selectorType
        self.abrirPaginaDelPedido_button_selector=selector
    
    #A partir de aqui construimos los controles Y eventos del fomulario de la ficha Agregar Oportunidad
    def panelFichaOportunidad(self,selectorType, selector):
        self.panelFichaOportunidad_selectorType=selectorType
        self.panelFichaOportunidad_selector=selector
             
    def clienteCIF_edit(self,selectorType, selector, value):
        self.clienteCIF_edit_selectorType=selectorType
        self.clienteCIF_edit_selector=selector
        self.clienteCIF_edit_value=value
        
    def buscarCliente_button(self, selectorType, selector):
        self.buscarCliente_button_selectorType=selectorType
        self.buscarCliente_button_selector=selector
        
    def cancelarBuscarCliente_button(self, selectorType, selector):
        self.cancelarBuscarCliente_button_selectorType=selectorType
        self.cancelarBuscarCliente_button_selector=selector
        
    def crearOportunidad_button(self, selectorType, selector):
        self.crearOportunidad_button_selectorType=selectorType
        self.crearOportunidad_button_selector=selector
    
    def cancelarOportunidad_button(self, selectorType, selector):
        self.cancelarOportunidad_button_selectorType=selectorType
        self.cancelarOportunidad_button_selector=selector
        
    def cuadro_De_Busqueda_Cliente_select2(self,selectorType, selector):
        self.cuadro_De_Busqueda_Cliente_select2_SelectorType=selectorType
        self.cuadro_De_Busqueda_Cliente_select2_Selector=selector 

    def cuadro_De_Busqueda_Cliente_Opcion(self,selectorType, selector, value):
        self.cuadro_De_Busqueda_Cliente_Opcion_SelectorType=selectorType
        self.cuadro_De_Busqueda_Cliente_Opcion_Selector=selector
        self.cuadro_De_Busqueda_Cliente_Opcion_Value=value
        
    def abrirFichaOportunidad_button_click(self):
        #Esperamos a que cargue el formulario, MEDIANTE VERIFICAR EL BUTTON BUSCAR CLIENTE
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.abrirFichaOportunidad_button_selectorType,self.abrirFichaOportunidad_button_selector))
        ).click()
        
    def crearOportunidad_button_click(self):
        time.sleep(1)
        #Esperamos que aparezca el campo CIF del cliente
        #Escribimos el DNI del cliente en el campo CLiente de la ficha.
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.clienteCIF_edit_selectorType, self.clienteCIF_edit_selector))
        ).send_keys(self.clienteCIF_edit_value)
        

        
        #Pinchamos en el boton buscar cliente
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.buscarCliente_button_selectorType, self.buscarCliente_button_selector))
        ).click()
        
        #Esperamos a que el boton buscar desaparezca y sea reemplazado por el de cancelar
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((self.buscarCliente_button_selectorType, self.buscarCliente_button_selector))
        )
        #Uso PyAutoGUI para enviar pulsaciones de tecla hasta elegir el cliente
        #Luego, pincho en el boton crear oportunidad
        # Enviar Ctrl + Tab

        #Damos Clic en el select2 de _Clientes
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.cuadro_De_Busqueda_Cliente_select2_SelectorType, self.cuadro_De_Busqueda_Cliente_select2_Selector))
        ).click()
        time.sleep(1)
        #En el cuadro de busqueda enviamos el valor, y la tecla enter para elegir lo seleccionado.
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.cuadro_De_Busqueda_Cliente_Opcion_SelectorType, self.cuadro_De_Busqueda_Cliente_Opcion_Selector))
        ).send_keys(self.cuadro_De_Busqueda_Cliente_Opcion_Value + Keys.ENTER)
    
        
        # Ejecuta las acciones de PyAutoGUI aquí
        #pyautogui.hotkey('shift', 'tab')
        #pyautogui.press('enter')
        #pyautogui.write(self.clienteCIF_edit_value)
        #pyautogui.press('enter')
        
        #Ahora doy click en el boton Crear Oportunidad
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.crearOportunidad_button_selectorType, self.crearOportunidad_button_selector))
        ).click()
        #self.driver.find_element(self.cancelarOportunidad_button_selectorType, self.cancelarOportunidad_button_selector).click()
    
    #A partir de aqui contruimos los controles y eventos de la ficha configuracion de oportunidad
    def configuraciones_catalogo_select(self, selectorType, selector,value):
        self.configuraciones_catalogo_select_selectorType=selectorType
        self.configuraciones_catalogo_select_selector=selector
        self.configuraciones_catalogo_select_value=value
              
    def configuraciones_usuarioAsignado_select2(self, selectorType,selector):
        self.configuraciones_usuarioAsignado_Select2_Selector=selector
        self.configuraciones_usuarioAsignado_Select2_SelectorType=selectorType
        
    def configuraciones_usuarioAsignado_Opcion(self, selectorType,selector,value):
        self.configuraciones_usuarioAsignado_Opcion_Selector=selector
        self.configuraciones_usuarioAsignado_Opcion_SelectorType=selectorType
        self.configuraciones_usuarioAsignado_Opcion_Value=value
        
    def guardarConfiguracionesOportunidad_button(self,selectorType, selector):
        self.guardarConfiguracionesOportunidad_button_selectorType=selectorType
        self.guardarConfiguracionesOportunidad_button_selector=selector
    
    def configuracionFichaCliente_button_click(self):
        # Esperamos hasta que el panel de la ficha Agregar Oportunidad no esté visible
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((self.panelFichaOportunidad_selectorType, self.panelFichaOportunidad_selector))
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.configuracionFichaCliente_button_selectorType, self.configuracionFichaCliente_button_selector))
        ).click()
    
    def configuracionesOportunidad_button_click(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.configuracionesOportunidad_button_selectorType, self.configuracionesOportunidad_button_selector))
        ).click()
    
    def guardarConfiguracionesOportunidad_button_click(self):
        #Esperamos que aparezca el campo
        time.sleep(1)
        Select(WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.configuraciones_catalogo_select_selectorType, self.configuraciones_catalogo_select_selector))
        )).select_by_visible_text(self.configuraciones_catalogo_select_value)
         # Ejecuta las acciones de PyAutoGUI aquí porque el control es de tipo select2
        
        #Damos Clic en el select2 de Tipo de Internet
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.configuraciones_usuarioAsignado_Select2_SelectorType, self.configuraciones_usuarioAsignado_Select2_Selector))
        ).click()
        time.sleep(1)
        #En el cuadro de busqueda enviamos el valor, y la tecla enter para elegir lo seleccionado.
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.configuraciones_usuarioAsignado_Opcion_SelectorType, self.configuraciones_usuarioAsignado_Opcion_Selector))
        ).send_keys(self.configuraciones_usuarioAsignado_Opcion_Value + Keys.ENTER)
        
        
        #Damos el clic en Guardar
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.guardarConfiguracionesOportunidad_button_selectorType,self.guardarConfiguracionesOportunidad_button_selector))
        ).click()

    def abrirPaginaDelPedido_button_click(self):
        numeroPedido= self.func_Obtener_ID_Ultimo_Pedido()
        self.driver.get("https://rsctel.wikitic.es/index.php/pedidov2/n/"+str(numeroPedido))
        return numeroPedido
    
    def func_Obtener_ID_Ultimo_Pedido(self):
        """
        Obtiene el ID del último pedido disponible en la página.

        Proceso:
        1. Espera hasta que el panel de configuración de oportunidad desaparezca, lo cual se verifica 
        mediante la invisibilidad del elemento del catálogo de configuraciones.
        2. Una vez que el panel desaparece, espera hasta que el botón de abrir la página del pedido 
        esté presente en el DOM.
        3. Extrae el atributo "data-id" de dicho botón, que corresponde al ID del pedido.
        4. Retorna el ID del pedido como una cadena.

        Nota: 
        - Esta función debe ejecutarse antes de llamar a `abrirPaginaDelPedido_button_click`, 
        ya que este último botón se usa para abrir la página del pedido y podría cambiar el contexto.
        """

        # Esperamos hasta que el panel de configuración de oportunidad no esté visible, 
        # lo cual se verifica mediante la invisibilidad del elemento del catálogo de configuraciones.
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((self.configuraciones_catalogo_select_selectorType, 
                                                self.configuraciones_catalogo_select_selector))
        )

        # Esperamos hasta que el botón de abrir la página del pedido esté presente en el DOM
        numeroPedido = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.abrirPaginaDelPedido_button_selectorType, 
                                            self.abrirPaginaDelPedido_button_selector))
        ).get_attribute("data-id")  # Extraemos el atributo "data-id", que contiene el ID del pedido.

        return numeroPedido  # Retornamos el ID del último pedido.
        
    #Defino el boton de pre-clonar oportunidad
    def preclonarOportunidad_button(self,selectorType,selector):
        self.preclonarOportunidad_button_selectorType=selectorType
        self.preclonarOportunidad_button_selector=selector
        
    #Defino el boton de clonar oportunidad
    def clonarOportunidad_button(self,selectorType,selector):
        self.clonarOportunidad_button_selectorType=selectorType
        self.clonarOportunidad_button_selector=selector
    
        #Defino la pestaña de OFERTAS
   
    def ofertas_TabPage(self,selectorType,selector):
        self.ofertas_TabPage_selectorType=selectorType
        self.ofertas_TabPage_selector=selector
        
    def abrir_Ficha_Ultima_Oportunidad_Clonada(self,selectorType,selector):
        self.abrir_Ficha_Ultima_Oportunidad_Clonada_SelectorType=selectorType
        self.abrir_Ficha_Ultima_Oportunidad_Clonada_Selector=selector
    
    def clonarOportunidad_button_click(self):
        #LOGICA:
        #Ir a la pagina de pedidos
        #Elegir el ultimo pedido agregado en la tabla
        #Dar clic en configuraciones
        
        #dar clic en preclonar
        #dar clic en clonar
        #ir a la pestaña de Ofertas(que es donde se agrega la oportunidad duplicada)
        #Editar el ultimo pedido en la lista
        #Esperamos que aparezca el campo
        
        #Vamos a la pagina de pedidos
        self.driver.get("https://rsctel.wikitic.es/index.php/oportunidades")
        print("Entramos a Pedidos")
        #Elegir el ultimo pedido agregado en la tabla y dar en configuracion de la ficha           
        self.configuracionFichaCliente_button_click()
        print("Clic en Configuracion Ficha")
        self.configuracionesOportunidad_button_click()
        print("Clic en Configuracion Oportunidad")
        #HAsta aqui estamos en la ficha configuraciones de la oportunidad
        #Dar clic en pre- clonar (pregunta de confirmacion)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.preclonarOportunidad_button_selectorType,self.preclonarOportunidad_button_selector))
        ).click()        
        print("PreClonamos Oportunidad")
        #Dar clic en clonar(confirmacion)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.clonarOportunidad_button_selectorType,self.clonarOportunidad_button_selector))
        ).click()
        print("Clonamos Oportunidad")        
        # Esperamos hasta que el panel de la ficha configuracion de Oportunidad no esté visible, lo hago mediante la invisibilidad del select Catalago
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((self.configuraciones_catalogo_select_selectorType, self.configuraciones_catalogo_select_selector))
        )
        print("La ficha de configuraciones ya no esta visible")
        #Vamos a la pestaña ofertas    
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.ofertas_TabPage_selectorType,self.ofertas_TabPage_selector))
        ).click()
        print("Clic en Pestaña Ofertas")
        
    def editarAjustesFichaClonada(self):
            
            #Elegir el ultimo pedido agregado en la tabla y dar en configuracion de la ficha           
            self.configuracionFichaCliente_button_click()
            print("Clic en Configuracion Ficha")
            self.configuracionesOportunidad_button_click()
            print("Clic en Configuracion Oportunidad")
            #Hasta aqui estamos en la ficha configuraciones de la oportunidad
            #Establecemos el catalogo
            try:
                time.sleep(5)
                
                Select(WebDriverWait(self.driver , 10).until(
                    EC.visibility_of_element_located((self.configuraciones_catalogo_select_selectorType, self.configuraciones_catalogo_select_selector))
                )).select_by_visible_text(self.configuraciones_catalogo_select_value)
                
                #Damos el clic en Guardar
                
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((self.guardarConfiguracionesOportunidad_button_selectorType,self.guardarConfiguracionesOportunidad_button_selector))
                ).click()
                
            except Exception as e:
                print(f"Error en editando ajustes de ficha duplicada: {e}")

    def editarFichaOportunidadClonada(self):
        #Editar el ultimo pedido en la lista
        ultimaOportunidadClonada=WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.abrir_Ficha_Ultima_Oportunidad_Clonada_SelectorType, self.abrir_Ficha_Ultima_Oportunidad_Clonada_Selector))
        ).get_attribute("data-id")
        self.driver.get("https://rsctel.wikitic.es/index.php/pedidov2/n/"+str(ultimaOportunidadClonada))
              
class fichaEnergiaCRM:
    """
    COMENCE A CODIFICAR ESTA FICHA EL DIA VIERNES 24 DE ENERO DE 2025
    """
    
    
    def __init__(self,driver):
        self.driver=driver
        
        #Boton Luz
        self.añadirContratoLuz_button_selectorType=None
        self.añadirContratoLuz_button_selector=None
        #Boton Gas
        self.añadirContratoGas_button_selectorType=None
        self.añadirContratoGas_button_selector=None
        #Boton SVA
        self.añadirContratoSVA_button_selectorType=None
        self.añadirContratoSVA_button_selector=None
        
        #Botones dinamicos dentro de estos tres botones anteriores
        #Select Tarifa
        self.listadoTarifas_select_selectorType=None
        self.listadoTarifas_select_selector=None
        self.listadoTarifas_select_value=None
        #Boton Añadir Tarifa
        self.añadirTarifa_button_selectorType=None
        self.añadirTarifa_button_Selector=None
        #Boton Cancelar Agregar Tarifa
        self.cancelarAgregarTarifa_button_selectorType=None
        self.cancelarAgregarTarifa_button_Selector=None        
        
        
        #Agrego el ultimo elemento agregado a la lista de contratos
        #vendidos
        self.ultimoContratoAgregado_Span_selectorType=None
        self.ultimoContratoAgregado_Span_selector=None
        self.ultimoContratoAgregado_Span_value=None
        #dentro de este encontramos los siguientes objetos
        #Numero de CUPS del contrato de Luz o del Gas
        self.numeroCUPS_input_selectorType=None
        self.numeroCUPS_input_selector=None
        self.numeroCUPS_input_value=None
        #Boton Guardar CUPS del contrato
        self.guardarCUPS_button_selectorType=None
        self.guardarCUPS_button_selector=None
        #Boton Cancelar Guardar CUPS del contrato
        self.cancelarGuardarCUPS_button_selectorType=None
        self.cancelarGuardarCUPS_button_selector=None
        
        
        
        #Boton Editar Datos
        self.editarDatos_button_selectorType=None
        self.editarDatos_button_selector=None
        #Controles que estan dentro de EDITAR DATOS
        #Select que se llama segmento tiene que tener un value que siempre hasta esta version
        #lo eligen como PARTICULAR
        self.segmentoCliente_select_selectorType=None
        self.segmentoCliente_select_selector=None
        self.segmentoCliente_select_value=None        
        #Ahora un select que es donde se eleige la Operador del cliente:
        self.provinciaCliente_select_selectorType=None
        self.provinciaCliente_select_selector=None
        self.provinciaCliente_select_value=None        
        #Ahora un input que es donde va el numero de cuenta bancaria IBAN
        self.cuentaBancariaIBAN_input_selectorType=None
        self.cuentaBancariaIBAN_input_selector=None
        self.cuentaBancariaIBAN_input_value=None
        #Ahora un input que es donde va la entidad bancaria 
        self.entidadBancaria_input_selectorType=None
        self.entidadBancaria_input_selector=None
        self.entidadBancaria_input_value=None
        #Ahora un input que es donde va el CIF/NIF del cliente
        self.CIF_NIF_input_selectorType=None
        self.CIF_NIF_input_selector=None
        self.CIF_NIF_input_value=None
        #Ahora un input que es donde va el NOMBRE del cliente
        self.nombreCliente_input_selectorType=None
        self.nombreCliente_input_selector=None
        self.nombreCliente_input_value=None
        #Boton Guardar Datos Basicos
        self.guardarDatosBasicos_button_selectorType=None
        self.guardarDatosBasicos_button_selector=None
        #Boton Cancelar Guardar Datos Basicos
        self.cancelarGuardarDatosBasicos_button_selectorType=None
        self.cancelarGuardarDatosBasicos_button_selector=None
        
        
        #Boton añadir direccion
        self.añadirDireccion_button_selectorType=None
        self.añadirDireccion_button_selector=None
        #Controles que estan dentro de AGREGAR DIRECCION
        #Select que se llama TIPO tiene que tener un value que siempre hasta esta version
        #lo eligen como INSTALACION
        self.tipoDireccion_select_selectorType=None
        self.tipoDireccion_select_selector=None
        self.tipoDireccion_select_value=None
        #De momento solo copiare la direccion completa, sin validar ni nada en el 
        #input direccion, el resto lo tendran que hacer manualmente hasta que
        #pueda resolver como separar la direccion de una manera robusta
        self.direccion_input_selectorType=None
        self.direccion_input_selector=None
        self.direccion_input_value=None
        #Inicializamos ahora el input de la provincia del cliente, que perfectamente podria ser el mismo
        #que el select de datos basicos, pero lo asignaremos en tiempo de ejecucion
        self.provinciaCliente_input_selectorType=None
        self.provinciaCliente_input_selector=None
        self.provinciaCliente_input_value=None
        #Inicializamos el select de operadora
        self.operadora_select_selectorType=None
        self.operadora_select_selector=None
        self.operadora_select_value=None
        #Numero de calle
        self.numeroCalle_input_selectorType=None
        self.numeroCalle_input_selector=None
        self.numeroCalle_input_value=None
        #Planta Piso
        self.plantaPiso_input_selectorType=None
        self.plantaPiso_input_selector=None
        self.plantaPiso_input_value=None
        #Bloque Escalera
        self.bloqueEscalera_input_selectorType=None
        self.bloqueEscalera_input_selector=None
        self.bloqueEscalera_input_value=None
        #Inicializamos el municipio de la direccion
        self.municipioCliente_input_selectorType=None
        self.municipioCliente_input_selector=None
        self.municipioCliente_input_value=None
        #Inicializamos el codigo postal de la direccion
        self.codigoPostalCliente_input_selectorType=None
        self.codigoPostalCliente_input_selector=None
        self.codigoPostalCliente_input_value=None
        #Boton Guardar Datos Basicos
        self.guardarDatosDireccion_button_selectorType=None
        self.guardarDatosDireccion_button_selector=None
        #Boton Cancelar Guardar Datos Basicos
        self.cancelarGuardarDatosDireccion_button_selectorType=None
        self.cancelarGuardarDatosDireccion_button_selector=None
        
    #Boton Luz
    def añadirContratoLuz_button(self,selectorType,selector):
        self.añadirContratoLuz_button_selectorType=selectorType
        self.añadirContratoLuz_button_selector=selector
    
    #Boton Gas
    def añadirContratoGas_button(self,selectorType,selector):
        self.añadirContratoGas_button_selectorType=selectorType
        self.añadirContratoGas_button_selector=selector
        
    #Boton SVA
    def añadirContratoSVA_button(self,selectorType,selector):
        self.añadirContratoSVA_button_selectorType=selectorType
        self.añadirContratoSVA_button_selector=selector
    
    #Botones dinamicos dentro de estos tres botones anteriores
    #Select con listado de tarifas disponibles
    def listadoTarifas_select(self,selectorType, selector, value):
        self.listadoTarifas_select_selectorType=selectorType
        self.listadoTarifas_select_selector=selector
        self.listadoTarifas_select_value=value
    
    #Boton agregar tarifa seleccoinada
    def añadirTarifa_button(self, selectorType, selector):
        self.añadirTarifa_button_selectorType=selectorType
        self.añadirTarifa_button_Selector=selector
    
    #Boton cancelar agregar tarifa seleccoinada
    def cancelarAgregarTarifa_button(self, selectorType, selector):
        self.cancelarAgregarTarifa__button_selectorType=selectorType
        self.cancelarAgregarTarifa_button_Selector=selector
    
    #Ahora cuando se agrega un elemento de la lista de contratos disponibles
    #lo que sucede a continuacion es que se agrega un elemento a una tabla de items
    #lo que nos interesa es por lo unico que se diferencia cada control 
    #lo cual seria el nombre del producto, y este se encuentra dentro de un elemento
    #tipo span, que esta dentro de otro span que tiene como clase:"literal"
    def ultimoContratoAgregado_Span(self,selectorType, selector, value):
        self.ultimoContratoAgregado_Span_selectorType=selectorType
        self.ultimoContratoAgregado_Span_selector=selector
        self.ultimoContratoAgregado_Span_value=value
    
    #Ahora, dentro del ultimo contrato agregado al dar clic lo que me voy a encontrar es con
    #los siguientes controles que necesito manipular: input:CUPS, button: Guardar, Cancelar.
    #HAsta el momento solo manejare las variables que ya me da OCM, las actualizaciones vendran por estos
    #agregados.
    def numeroCUPS_input(self,selectorType, selector, value):
        self.numeroCUPS_input_selectorType=selectorType
        self.numeroCUPS_input_selector=selector
        self.numeroCUPS_input_value=value

    #Boton guardar cups del contrato
    def guardarCUPS_button(self,selectorType,selector):
        self.guardarCUPS_button_selectorType=selectorType
        self.guardarCUPS_button_selector=selector
        
    #Boton cancelar guardar cups del contrato
    def cancelarGuardarCUPS_button(self,selectorType,selector):
        self.cancelarGuardarCUPS_button_selectorType=selectorType
        self.cancelarGuardarCUPS_button_selector=selector
    
    #Boton Editar Datos    
    def editarDatos_button(self, selectorType, selector):
        self.editarDatos_button_selectorType=selectorType
        self.editarDatos_button_selector=selector
    #Controles que estan dentro de EDITAR DATOS
    #Select que se llama segmento tiene que tener un value que siempre hasta esta version
    #lo eligen como PARTICULAR
    def segmentoCliente_select(self, selectorType, selector, value):
        self.segmentoCliente_select_selectorType=selectorType
        self.segmentoCliente_select_selector=selector
        self.segmentoCliente_select_value=value
                
    #Ahora un select que es donde se elige la provincia del cliente:
    def provinciaCliente_select(self, selectorType, selector, value):
        self.provinciaCliente_select_selectorType=selectorType
        self.provinciaCliente_select_selector=selector
        self.provinciaCliente_select_value=value
                    
    #Ahora un input que es donde va el numero de cuenta bancaria IBAN
    def cuentaBancariaIBAN_input(self,selectorType,selector,value):
        self.cuentaBancariaIBAN_input_selectorType=selectorType
        self.cuentaBancariaIBAN_input_selector=selector
        self.cuentaBancariaIBAN_input_value=value
        
    #Ahora un input que es donde va el numero de cuenta bancaria IBAN
    def entidadBancaria_input(self,selectorType,selector,value):
        self.entidadBancaria_input_selectorType=selectorType
        self.entidadBancaria_input_selector=selector
        self.entidadBancaria_input_value=value
        
    #Ahora un input que es donde va el CIF/NIF del cliente
    def CIF_NIF_input(self,selectorType,selector,value):
        self.CIF_NIF_input_selectorType=selectorType
        self.CIF_NIF_input_selector=selector
        self.CIF_NIF_input_value=value
        
    #Ahora un input que es donde va el NOMBRE del cliente
    def nombreCliente_input(self,selectorType,selector,value):
        self.nombreCliente_input_selectorType=selectorType
        self.nombreCliente_input_selector=selector
        self.nombreCliente_input_value=value
        
    #Boton Guardar Datos Basicos
    def guardarDatosBasicos_button(self, selectorType, selector):
        self.guardarDatosBasicos_button_selectorType=selectorType
        self.guardarDatosBasicos_button_selector=selector
        
    #Boton Cancelar Guardar Datos Basicos
    def cancelarGuardarDatosBasicos_button(self, selectorType, selector):
        self.cancelarGuardarDatosBasicos_button_selectorType=selectorType
        self.cancelarGuardarDatosBasicos_button_selector=selector
    
    #Boton añadir direccion    
    def añadirDireccion_button(self,selectorType, selector):
        self.añadirDireccion_button_selectorType=selectorType
        self.añadirDireccion_button_selector=selector
        
    #Añado ahora los controles que se encuentran dentro de direcciones y contactos
    #Controles que estan dentro de AGREGAR DIRECCION
    #Select que se llama TIPO tiene que tener un value que siempre hasta esta version
    #lo eligen como INSTALACION
    def tipoDireccion_select(self, selectorType,selector, value):
        self.tipoDireccion_select_selectorType=selectorType
        self.tipoDireccion_select_selector=selector
        self.tipoDireccion_select_value=value
        
    #De momento solo copiare la direccion completa, sin validar ni nada en el 
    #input direccion, el resto lo tendran que hacer manualmente hasta que
    #pueda resolver como separar la direccion de una manera robusta
    def direccion_input(self, selectorType, selector, value):
        self.direccion_input_selectorType=selectorType
        self.direccion_input_selector=selector
        self.direccion_input_value=value
    
    #Al final creare los objetos, pero no los llamare hasta tener programada
    #el modulo de mapeo y manejo de direcciones.
    def numeroCalle_input(self, selectorType, selector, value):
        self.numeroCalle_input_selectorType=selectorType
        self.numeroCalle_input_selector=selector
        self.numeroCalle_input_value=value 
    
    def plantaPiso_input(self, selectorType, selector, value):
        self.plantaPiso_input_selectorType=selectorType
        self.plantaPiso_input_selector=selector
        self.plantaPiso_input_value=value
        
    def bloqueEscalera_input(self, selectorType, selector, value):
        self.bloqueEscalera_input_selectorType=selectorType
        self.bloqueEscalera_input_selector=selector
        self.bloqueEscalera_input_value=value
        
    #Inicializamos ahora el input de la provincia del cliente, que perfectamente podria ser el mismo
    #que el select de datos basicos, pero lo asignaremos en tiempo de ejecucion
    def provinciaCliente_input(self, selectorType, selector, value):
        self.provinciaCliente_input_selectorType=selectorType
        self.provinciaCliente_input_selector=selector
        self.provinciaCliente_input_value=value
        
    
    #Inicializamos ahora el select de OPERADORA que es obligatorio elegir algo distinto al "-",
    #la opcion que elegiré, sera vacio.
    def operadora_select(self, selectorType, selector, value):
        self.operadora_select_selectorType=selectorType
        self.operadora_select_selector=selector
        self.operadora_select_value=value
        
    #Inicializamos el municipio de la direccion
    def municipioCliente_input(self, selectorType, selector, value):
        self.municipioCliente_input_selectorType=selectorType
        self.municipioCliente_input_selector=selector
        self.municipioCliente_input_value=value
    
    #Inicializamos el codigo postal de la direccion
    def codigoPostalCliente_input(self, selectorType,selector,value):
        self.codigoPostalCliente_input_selectorType=selectorType
        self.codigoPostalCliente_input_selector=selector
        self.codigoPostalCliente_input_value=value
        
    #Boton Guardar Datos Basicos
    def guardarDatosDireccion_button(self,selectorType,selector):
        self.guardarDatosDireccion_button_selectorType=selectorType
        self.guardarDatosDireccion_button_selector=selector
        
    #Boton Cancelar Guardar Datos Basicos
    def cancelarGuardarDatosDireccion_button(self,selectorType,selector):
        self.cancelarGuardarDatosDireccion_button_selectorType=selectorType
        self.cancelarGuardarDatosDireccion_button_selector=selector
        
    #Ahora vamos a definir las acciones de cada boton
    #Comenzaremos de arriba hacia abajo.
    #boton LUZ
    def añadirContratoLuz_button_click(self):
        #Esperamos que aparezca el input CUPS
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.añadirContratoLuz_button_selectorType, self.añadirContratoLuz_button_selector))
        ).click()

    #Boton Gas
    def añadirContratoGas_button_click(self):
        #Esperamos que aparezca el input CUPS
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.añadirContratoGas_button_selectorType,self.añadirContratoGas_button_selector))
        ).click()
            
    #Programamos lo que hara el boton Añadir Tarifa al darle click
    def añadirTarifa_button_click(self):
        #Esperamos que aparezca el input CUPS
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.añadirTarifa_button_selectorType,self.añadirTarifa_button_Selector))
        )
        #Establecemos el valor del select TARIFA y se lo asignamos de paso al control
        #ultimo contrato agregado para luego poder dar clic y editar sus cups y eso
        #ESTO ULTIMO VERE SI QUEDA MEJOR EN LA LLAMADA A LAS CLASES
        
        Select(self.driver.find_element(self.listadoTarifas_select_selectorType,self.listadoTarifas_select_selector)).select_by_visible_text(self.listadoTarifas_select_value)        
        #Ahora damos click alboton añadir tarifa.
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.añadirTarifa_button_selectorType,self.añadirTarifa_button_Selector))
        ).click()

    #Programamos lo que hara el boton cancelar agregar Tarifa al darle click        
    def cancelarAgregarTarifa_button_click(self):
        #Esperamos que aparezca el input CUPS
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.cancelarAgregarTarifa_button_selectorType,self.cancelarAgregarTarifa_button_selector))
        ).click()
    
    #esto es lo que sucedera al darle click al span con el valor del ultimo contrato    
    def ultimoContratoAgregado_Span_click(self):
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.ultimoContratoAgregado_Span_selectorType, self.ultimoContratoAgregado_Span_selector))
        ).click()
        
        #Esperamos que aparezca el input CUPS
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.numeroCUPS_input_selectorType, self.numeroCUPS_input_selector))
        ).send_keys(self.numeroCUPS_input_value)
        #Ahora que estamos seguros de su presencia, procedemos a rellenar el campo.
          
    #Ahora definimos las acciones para el boton Guardar
    def guardarCUPS_button_click(self):
        self.driver.find_element(self.guardarCUPS_button_selectorType,self.guardarCUPS_button_selector).click()
        WebDriverWait(self.driver , 10).until(
            EC.invisibility_of_element_located((self.guardarCUPS_button_selectorType, self.guardarCUPS_button_selector))
        )
    """
    ESTE ES EL AVANCE QUE HE REALIZADO HASTA HOY DIA 27 DE ENERO DE 2025
    """
    
    #A PARTIR DE AQUI ES TRABAJO DEL DIA 28 DE ENERO PERO EN LA MADRUGADA A LAS 00:00
    def editarDatos_button_click(self):
        #Esperamos que aparezca el boton
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.editarDatos_button_selectorType,self.editarDatos_button_selector))
        ).click()
        
    #Ahora programamos el boton Guardar Datos Basicos
    def guardarDatosBasicos_button_click(self):
        #Rellenamos los select y los inputs
        #Segmento CLiente
        Select(self.driver.find_element(self.segmentoCliente_select_selectorType, self.segmentoCliente_select_selector)).select_by_visible_text(self.segmentoCliente_select_value)
        #Provincia del cliente
        Select(self.driver.find_element(self.provinciaCliente_select_selectorType, self.provinciaCliente_select_selector)).select_by_visible_text(self.provinciaCliente_select_value)
        
        #Operadora del cliente (obligatorio para guardar los datos basicos, elijo siempre el elemento vacio)
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.operadora_select_selectorType, self.operadora_select_selector))
        ).send_keys(Keys.DOWN)
        
        #No de Cuenta Bancaria del Cliente
        #Envio Ctrl+a para elegir el texto que exista(por si es duplicada la ficha)
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.cuentaBancariaIBAN_input_selectorType,self.cuentaBancariaIBAN_input_selector))
        ).send_keys(Keys.CONTROL + "A")
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.cuentaBancariaIBAN_input_selectorType,self.cuentaBancariaIBAN_input_selector))
        ).send_keys(self.cuentaBancariaIBAN_input_value)
        #Entidad Bancaria
        #Envio Ctrl+a para elegir el texto que exista(por si es duplicada la ficha) 
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.entidadBancaria_input_selectorType,self.entidadBancaria_input_selector))
        ).send_keys(Keys.CONTROL + "A")  
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.entidadBancaria_input_selectorType,self.entidadBancaria_input_selector))
        ).send_keys(self.entidadBancaria_input_value)
        #CIF/NIF DEL CLIENTE
        #Envio Ctrl+a para elegir el texto que exista(por si es duplicada la ficha)
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.CIF_NIF_input_selectorType,self.CIF_NIF_input_selector))
        ).send_keys(Keys.CONTROL + "A")  
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.CIF_NIF_input_selectorType,self.CIF_NIF_input_selector))
        ).send_keys(self.CIF_NIF_input_value)
        #NOMBRE DEL CLIENTE
        #Envio Ctrl+a para elegir el texto que exista(por si es duplicada la ficha)
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.nombreCliente_input_selectorType,self.nombreCliente_input_selector))
        ).send_keys(Keys.CONTROL + "A")
        self.driver.find_element(self.nombreCliente_input_selectorType,self.nombreCliente_input_selector).send_keys(self.nombreCliente_input_value)
                
        #Esperamos que aparezca el boton y guardar
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.guardarDatosBasicos_button_selectorType,self.guardarDatosBasicos_button_selector))
        ).click()
        
        
    def añadirDireccion_button_click(self):
        #Esperamos que aparezca el boton y damos clic en agregar direccion
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.añadirDireccion_button_selectorType,self.añadirDireccion_button_selector))
        ).click()
        
    def guardarDatosDireccion_button_click(self):
        #Rellenamos los select y los inputs
        #Tipo de Direccion
        Select(self.driver.find_element(self.tipoDireccion_select_selectorType, self.tipoDireccion_select_selector)).select_by_visible_text(self.tipoDireccion_select_value)
        
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.direccion_input_selectorType,self.direccion_input_selector))
        ).send_keys(self.direccion_input_value)
        #Aqui me falta agregar el numero de calle, piso puerta y bloque escalera.
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.numeroCalle_input_selectorType,self.numeroCalle_input_selector))
        ).send_keys(self.numeroCalle_input_value)
        
        #De momento solo agregamos de la provincia para adelante
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.provinciaCliente_input_selectorType,self.provinciaCliente_input_selector))
        ).send_keys(self.provinciaCliente_input_value)
        #Ahora agregamos el municipio del cliente
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.municipioCliente_input_selectorType, self.municipioCliente_input_selector))
        ).send_keys(self.municipioCliente_input_value)
        #Ahora añadimos el codigo postal.
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.codigoPostalCliente_input_selectorType,self.codigoPostalCliente_input_selector))
        ).send_keys(self.codigoPostalCliente_input_value)
        #Ahora añadimos la planta Piso
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.plantaPiso_input_selectorType,self.plantaPiso_input_selector))
        ).send_keys(self.plantaPiso_input_value)
        #Ahora añadimos Bloque Escalera
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.bloqueEscalera_input_selectorType,self.bloqueEscalera_input_selector))
        ).send_keys(self.bloqueEscalera_input_value)
        
        #Una vez llenos los datos dariamos click en GUARDAR, pero
        #Al no llenar el numero de calle no me dejara, asi que lo dejo deshabilitado.
        WebDriverWait(self.driver , 10).until(
            EC.presence_of_element_located((self.guardarDatosDireccion_button_selectorType, self.guardarDatosDireccion_button_selector))
        ).click()
 
class fichaTelefonia:
    def __init__(self,driver):
        self.driver=driver
        #Objetos dentro de la caja de oferta Basica: Tipo CLiente, Escenario, Campos Extras (Provincia, Operador)
        #Objeto: Select
        #Label: Tipo Cliente
        self.tipoCliente_Select_Selector=None
        self.tipoCliente_Select_SelectorType=None
        self.tipoCliente_Select_Value=None
        
        #Objeto:Select
        #Label:Escenario
        self.escenario_Select_Selector=None
        self.escenario_Select_SelectorType=None
        self.escenario_Select_Value=None
        
        #Objeto:Select2
        #Label:Campos Extras - Provincia
        self.campos_Extras_Provincia_Select2_Selector=None
        self.campos_Extras_Provincia_Select2_SelectorType=None
        
        #Objeto:opcion de Select2
        #Label: - Seleccionar Provincia -
        self.campos_Extras_Opcion_Provincia_Selector=None
        self.campos_Extras_Opcion_Provincia_SelectorType=None
        self.campos_Extras_Opcion_Provincia_Value=None
        
        #Objeto:Select2
        #Label:Campos Extras - Operador
        self.campos_Extras_Operador_Select2_Selector=None
        self.campos_Extras_Operador_Select2_SelectorType=None
        
        #Objeto:opcion de Select2
        #Label: - Seleccionar Operador -
        self.campos_Extras_Opcion_Operador_Selector=None
        self.campos_Extras_Opcion_Operador_SelectorType=None
        self.campos_Extras_Opcion_Operador_Value=None
        
        #Objeto:Div
        #Label: Ir a oferta Basica
        self.div_Ir_A_Oferta_Basica_Selector=None
        self.div_Ir_A_Oferta_Basica_SelectorType=None
        
        #Objeto:Div Item Oferta
        #Label: Fijo
        self.div_Oferta_Fijo_Selector=None
        self.div_Oferta_Fijo_SelectorType=None
        
        #Objeto:Div Item Oferta
        #Label: Movil
        self.div_Oferta_Movil_Selector=None
        self.div_Oferta_Movil_SelectorType=None
        
        #Objeto:Div Item Oferta
        #Label: Centralita
        self.div_Oferta_Centralita_Selector=None
        self.div_Oferta_Centralita_SelectorType=None
        
        #Objeto:Div Item Oferta
        #Label: Otros
        self.div_Oferta_Otros_Selector=None
        self.div_Oferta_Otros_SelectorType=None
        
        #Objeto:Div Item Oferta
        #Label: Lineas Adicionales
        self.div_Oferta_Lineas_Adicionales_Selector=None
        self.div_Oferta_Lineas_Adicionales_SelectorType=None
        
        #Objeto:Div Item Oferta
        #Label: Lineas Extra
        self.div_Oferta_Lineas_Extra_Selector=None
        self.div_Oferta_Lineas_Extra_SelectorType=None
        
        #Objeto:Div Item Oferta
        #Label: Televisión
        self.div_Oferta_Television_Selector=None
        self.div_Oferta_Television_SelectorType=None
        
        #Objeto:Div Item Oferta
        #Label: SVA
        self.div_Oferta_SVA_Selector=None
        self.div_Oferta_SVA_SelectorType=None
        
        #Objeto:button  
        #Label: Detalle de Productos
        self.button_Detalle_De_Productos_Selector=None
        self.button_Detalle_De_Productos_SelectorType=None 
        
        
        #PESTAÑA FICHA DE OFERTA BASICA FIJO
        #Objetos aqui en esta pestaña: Tipo de Línea(Nueva, Portada),
        #Internet.
        self.tab_Fijo_Selector=None
        self.tab_Fijo_SelectorType=None
        self.opt_Tipo_Linea_Fijo_Selector=None
        self.opt_Tipo_Linea_Fijo_SelectorType=None
        self.selec_Internet_Selector=None
        self.select_Internet_SelectorType=None
        
        #PESTAÑA FICHA DE OFERTA BASICA MOVIL
        #Objetos aqui en esta pestaña: Tipo de Línea(Nueva, Postpago, Portada (origen prepago)),
        #Producto.
        self.tab_Movil_Selector=None
        self.tab_Movil_SelectorType=None
        self.opt_Tipo_Linea_Movil_Selector=None
        self.opt_Tipo_Linea_Movil_SelectorType=None
        self.oferta_Basica_Movil_Producto_select2_Selector=None
        self.oferta_Basica_Movil_Producto_select2_SelectorType=None
        self.oferta_Basica_Movil_Producto_Opcion_Selector=None
        self.oferta_Basica_Movil_Producto_Opcion_SelectorType=None
        self.oferta_Basica_Movil_Producto_Opcion_Value=None

    def tipoCliente_Select(self, selectorType,selector,value):
        self.tipoCliente_Select_Selector=selector
        self.tipoCliente_Select_SelectorType=selectorType
        self.tipoCliente_Select_Value=value
        
    def escenario_Select(self, selectorType,selector,value):
        self.escenario_Select_Selector=selector
        self.escenario_Select_SelectorType=selectorType
        self.escenario_Select_Value=value
    
    def campos_Extras_Provincia_select2(self, selectorType,selector):
        self.campos_Extras_Provincia_Select2_Selector=selector
        self.campos_Extras_Provincia_Select2_SelectorType=selectorType
        
    def campos_Extras_Opcion_Provincia(self, selectorType,selector,value):
        self.campos_Extras_Opcion_Provincia_Selector=selector
        self.campos_Extras_Opcion_Provincia_SelectorType=selectorType
        self.campos_Extras_Opcion_Provincia_Value=value
        
    def campos_Extras_Operador_select2(self, selectorType,selector):
        self.campos_Extras_Operador_Select2_Selector=selector
        self.campos_Extras_Operador_Select2_SelectorType=selectorType
        
    def campos_Extras_Opcion_Operador(self, selectorType,selector,value):
        self.campos_Extras_Opcion_Operador_Selector=selector
        self.campos_Extras_Opcion_Operador_SelectorType=selectorType
        self.campos_Extras_Opcion_Operador_Value=value
        
    def div_Ir_A_Oferta_Basica(self, selectorType,selector):
        self.div_Ir_A_Oferta_Basica_Selector=selector
        self.div_Ir_A_Oferta_Basica_SelectorType=selectorType
        
    def div_Oferta_Fijo(self, selectorType,selector):
        self.div_Oferta_Fijo_Selector=selector
        self.div_Oferta_Fijo_SelectorType=selectorType    
    
    def div_Oferta_Movil(self, selectorType,selector):
        self.div_Oferta_Movil_Selector=selector
        self.div_Oferta_Movil_SelectorType=selectorType  
    
    def div_Oferta_Centralita(self, selectorType,selector):
        self.div_Oferta_Centralita_Selector=selector
        self.div_Oferta_Centralita_SelectorType=selectorType
    
    def div_Oferta_Otros(self, selectorType,selector):
        self.div_Oferta_Otros_Selector=selector
        self.div_Oferta_Otros_SelectorType=selectorType
        
    def div_Oferta_Lineas_Adicionales(self, selectorType,selector):
        self.div_Oferta_Lineas_Adicionales_Selector=selector
        self.div_Oferta_Lineas_Adicionales_SelectorType=selectorType        
    
    def div_Oferta_Lineas_Extra(self, selectorType,selector):
        self.div_Oferta_Lineas_Extra_Selector=selector
        self.div_Oferta_Lineas_Extra_SelectorType=selectorType      
    
    def div_Oferta_Television(self, selectorType,selector):
        self.div_Oferta_Television_Selector=selector
        self.div_Oferta_Television_SelectorType=selectorType
        
    def div_Oferta_SVA(self, selectorType,selector):
        self.div_Oferta_SVA_Selector=selector
        self.div_Oferta_SVA_SelectorType=selectorType      

    def button_Detalle_De_Productos(self, selectorType,selector):
        self.button_Detalle_De_Productos_Selector=selector
        self.button_Detalle_De_Productos_SelectorType=selectorType 

    def llenar_Vista_Oferta_Basica(self):
        print("")
        #Seleccionamos el valor de Autonomo en el select Tipo de Cliente
        # Espera a que el elemento esté presente
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((self.tipoCliente_Select_SelectorType, self.tipoCliente_Select_Selector))
        )
        # Interactúa con el <select>
        Select(element).select_by_visible_text(self.tipoCliente_Select_Value)
        #Seleccionamos el valor de Nuevo Cliente
        # Espera a que el elemento esté presente
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((self.escenario_Select_SelectorType, self.escenario_Select_Selector))
        )
        # Interactúa con el <select>
        Select(element).select_by_visible_text(self.escenario_Select_Value)
        
        #Damos Clic en el select Provincia para que muestre el cuadro de busqueda
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((self.campos_Extras_Provincia_Select2_SelectorType, self.campos_Extras_Provincia_Select2_Selector))
        ).click()
        #En el cuadro de busqueda enviamos el valor, y la tecla enter para elegir lo seleccionado.
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((self.campos_Extras_Opcion_Provincia_SelectorType, self.campos_Extras_Opcion_Provincia_Selector))
        ).send_keys(self.campos_Extras_Opcion_Provincia_Value + Keys.ENTER)
        #Damos Clic en el select Operador para que muestre el cuadro de busqueda
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((self.campos_Extras_Operador_Select2_SelectorType, self.campos_Extras_Operador_Select2_Selector))
        ).click()
        #En el cuadro de busqueda enviamos el valor, y la tecla enter para elegir lo seleccionado.
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((self.campos_Extras_Opcion_Operador_SelectorType, self.campos_Extras_Opcion_Operador_Selector))
        ).send_keys(self.campos_Extras_Opcion_Operador_Value + Keys.ENTER)
        #Ahora damos clic en Ofertas Basicas
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((self.div_Ir_A_Oferta_Basica_SelectorType,self.div_Ir_A_Oferta_Basica_Selector))
        ).click()
        #Ahora marco el ITEM FIJO o cualquier otro item que este inicializado en la pestaña
        #Oferta Basica de Fijo
        if self.div_Oferta_Fijo_Selector!=None:
            self.driver.find_element(self.div_Oferta_Fijo_SelectorType,self.div_Oferta_Fijo_Selector).click()
        #Oferta Basica de Móvil
        if self.div_Oferta_Movil_Selector!=None:
            self.driver.find_element(self.div_Oferta_Movil_SelectorType,self.div_Oferta_Movil_Selector).click()    
        #Oferta Basica de Centralita
        if self.div_Oferta_Centralita_Selector!=None:
            self.driver.find_element(self.div_Oferta_Centralita_SelectorType,self.div_Oferta_Centralita_Selector).click()  
        #Oferta Basica de Otros
        if self.div_Oferta_Otros_Selector!=None:
            self.driver.find_element(self.div_Oferta_Otros_SelectorType,self.div_Oferta_Otros_Selector).click()       
        #Oferta Basica de Lineas_Adicionales
        if self.div_Oferta_Lineas_Adicionales_Selector!=None:
            self.driver.find_element(self.div_Oferta_Lineas_Adicionales_SelectorType,self.div_Oferta_Lineas_Adicionales_Selector).click()                 
        #Oferta Basica de Lineas_Extra
        if self.div_Oferta_Lineas_Extra_Selector!=None:
            self.driver.find_element(self.div_Oferta_Lineas_Extra_SelectorType,self.div_Oferta_Lineas_Extra_Selector).click()
        #Oferta Basica de Television
        if self.div_Oferta_Television_Selector!=None:
            self.driver.find_element(self.div_Oferta_Television_SelectorType,self.div_Oferta_Television_Selector).click()    
        #Oferta Basica de SVA
        if self.div_Oferta_SVA_Selector!=None:
            self.driver.find_element(self.div_Oferta_SVA_SelectorType,self.div_Oferta_SVA_Selector).click()  
        
        #Damos click en el boton ir a detalles de productos, aqui finalizamos esta funcion
   
    #RELACIONADO A LA FICHA DE OFERTA BASICA FIJO   
    def tab_Fijo(self,selectorType,selector):
        self.tab_Fijo_SelectorType=selectorType
        self.tab_Fijo_Selector=selector
      
    def opt_Tipo_Linea_Fijo(self,selectorType,selector):
        self.opt_Tipo_Linea_Fijo_Selector=selector
        self.opt_Tipo_Linea_Fijo_SelectorType=selectorType
    
    def oferta_Basica_Fijo_Internet_select2(self, selectorType,selector):
        self.oferta_Basica_Fijo_Internet_select2_Selector=selector
        self.oferta_Basica_Fijo_Internet_select2_SelectorType=selectorType
        
    def oferta_Basica_Fijo_Internet_Opcion(self, selectorType,selector,value):
        self.oferta_Basica_Fijo_Internet_Opcion_Selector=selector
        self.oferta_Basica_Fijo_Internet_Opcion_SelectorType=selectorType
        self.oferta_Basica_Fijo_Internet_Opcion_Value=value
        
    def llenar_Oferta_Basica_Fijo(self):
        #Damos clic en la pestaña para mostrar los controles
        if self.tab_Fijo_Selector != None:
            WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((self.tab_Fijo_SelectorType,self.tab_Fijo_Selector))
                ).click()
        #Damos Clic en el opt que el usuario elija dependiendo si su valor de Selector esta definido o no
        if self.opt_Tipo_Linea_Fijo_Selector != None:
           WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.opt_Tipo_Linea_Fijo_SelectorType,self.opt_Tipo_Linea_Fijo_Selector ))
            ).click()
        #Damos Clic en el select2 de Tipo de Internet
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((self.oferta_Basica_Fijo_Internet_select2_SelectorType, self.oferta_Basica_Fijo_Internet_select2_Selector))
        ).click()
        #En el cuadro de busqueda enviamos el valor, y la tecla enter para elegir lo seleccionado.
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((self.oferta_Basica_Fijo_Internet_Opcion_SelectorType, self.oferta_Basica_Fijo_Internet_Opcion_Selector))
        ).send_keys(self.oferta_Basica_Fijo_Internet_Opcion_Value + Keys.ENTER)
    
    #RELACIONADO A LA FICHA DE OFERTA BASICA MOVIL     
    def tab_Movil(self,selectorType,selector):
        self.tab_Movil_SelectorType=selectorType
        self.tab_Movil_Selector=selector
    
    def opt_Tipo_Linea_Movil(self,selectorType,selector):
        self.opt_Tipo_Linea_Movil_Selector=selector
        self.opt_Tipo_Linea_Movil_SelectorType=selectorType
    
    def oferta_Basica_Movil_Producto_select2(self, selectorType,selector):
        self.oferta_Basica_Movil_Producto_select2_Selector=selector
        self.oferta_Basica_Movil_Producto_select2_SelectorType=selectorType
        
    def oferta_Basica_Movil_Producto_Opcion(self, selectorType,selector,value):
        self.oferta_Basica_Movil_Producto_Opcion_Selector=selector
        self.oferta_Basica_Movil_Producto_Opcion_SelectorType=selectorType
        self.oferta_Basica_Movil_Producto_Opcion_Value=value
        
    def llenar_Oferta_Basica_Movil(self):
        #Damos clic en la pestaña para mostrar los controles
        WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.tab_Movil_SelectorType,self.tab_Movil_Selector))
            ).click()
        #Damos Clic en el opt que el usuario elija dependiendo si su valor de Selector esta definido o no
        if self.opt_Tipo_Linea_Movil_Selector != None:
           WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.opt_Tipo_Linea_Movil_SelectorType,self.opt_Tipo_Linea_Movil_Selector ))
            ).click()
            
        #Damos Clic en el select2 de Movil_Producto
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((self.oferta_Basica_Movil_Producto_select2_SelectorType, self.oferta_Basica_Movil_Producto_select2_Selector))
        ).click()
        #En el cuadro de busqueda enviamos el valor, y la tecla enter para elegir lo seleccionado.
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((self.oferta_Basica_Movil_Producto_Opcion_SelectorType, self.oferta_Basica_Movil_Producto_Opcion_Selector))
        ).send_keys(self.oferta_Basica_Movil_Producto_Opcion_Value + Keys.ENTER)
    
    #RELACIONADO A LA FICHA DE OFERTA BASICA LINEAS ADICIONALES Y LINEAS EXTRAS
    #Este codigo es el mismo para las dos fichas de lineas adicionales y lineas extras.   
    def tab_Lineas_Adicionales_Extras(self,selectorType,selector):
        self.tab_Lineas_Adicionales_Extras_SelectorType=selectorType
        self.tab_Lineas_Adicionales_Extras_Selector=selector
    
    def button_Agregar_Lineas_Adicionales_Extras(self,selectorType,selector):
        self.button_Agregar_Lineas_Adicionales_Extras_SelectorType=selectorType
        self.button_Agregar_Lineas_Adicionales_Extras_Selector=selector
    
    def opt_Tipo_Lineas_Adicionales_Extras(self,selectorType,selector):
        self.opt_Tipo_Lineas_Adicionales_Extras_Selector=selector
        self.opt_Tipo_Lineas_Adicionales_Extras_SelectorType=selectorType
    
    def oferta_Basica_Lineas_Adicionales_Extras_Producto_select2(self, selectorType,selector):
        self.oferta_Basica_Lineas_Adicionales_Extras_Producto_select2_Selector=selector
        self.oferta_Basica_Lineas_Adicionales_Extras_Producto_select2_SelectorType=selectorType
        
    def oferta_Basica_Lineas_Adicionales_Extras_Producto_Opcion(self, selectorType,selector,value):
        self.oferta_Basica_Lineas_Adicionales_Extras_Producto_Opcion_Selector=selector
        self.oferta_Basica_Lineas_Adicionales_Extras_Producto_Opcion_SelectorType=selectorType
        self.oferta_Basica_Lineas_Adicionales_Extras_Producto_Opcion_Value=value
        
    def llenar_Oferta_Basica_Lineas_Adicionales_Extras(self):
        #Damos clic en la pestaña para mostrar los controles
        WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.tab_Lineas_Adicionales_Extras_SelectorType,self.tab_Lineas_Adicionales_Extras_Selector))
            ).click()
        #Damos Clic en el opt que el usuario elija dependiendo si su valor de Selector esta definido o no
        
        if self.button_Agregar_Lineas_Adicionales_Extras_Selector != None:
           WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.button_Agregar_Lineas_Adicionales_Extras_SelectorType,self.button_Agregar_Lineas_Adicionales_Extras_Selector ))
            ).click()
        
        if self.opt_Tipo_Lineas_Adicionales_Extras_Selector != None:
           WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.opt_Tipo_Lineas_Adicionales_Extras_SelectorType,self.opt_Tipo_Lineas_Adicionales_Extras_Selector ))
            ).click()
            
        #Damos Clic en el select2 de _Lineas_Adicionales_Extras
        print("Paso1")
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((self.oferta_Basica_Lineas_Adicionales_Extras_Producto_select2_SelectorType, self.oferta_Basica_Lineas_Adicionales_Extras_Producto_select2_Selector))
        ).click()
        print("Paso2")
        #En el cuadro de busqueda enviamos el valor, y la tecla enter para elegir lo seleccionado.
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((self.oferta_Basica_Lineas_Adicionales_Extras_Producto_Opcion_SelectorType, self.oferta_Basica_Lineas_Adicionales_Extras_Producto_Opcion_Selector))
        ).send_keys(self.oferta_Basica_Lineas_Adicionales_Extras_Producto_Opcion_Value + Keys.ENTER)
    