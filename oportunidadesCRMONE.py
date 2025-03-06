import CRMONE_V2
import time
from PySide6.QtWidgets import QMessageBox as msg

class oportunidadesCRMONE:
    def __init__(self, qwidget,driver):
        self.controlPadre=qwidget
        self.driver=driver
        
    def abrirFichaOportunidad(self):
        #Voy a la pagina de Oportunidades en el CRM
        self.crmOportunidades=CRMONE_V2.crmOportunidades(self.driver)
        print("Dentro de AbririFichaOportunidad")
        self.crmOportunidades.driver.get('https://rsctel.wikitic.es/index.php/oportunidades')
        self.crmOportunidades.panelFichaOportunidad("css selector",'#panel_estados_oportunidades')
        self.crmOportunidades.abrirFichaOportunidad_button("css selector",'#bt_abrir_pedido')
        self.crmOportunidades.abrirFichaOportunidad_button_click()
    
    def crearOportunidad(self, DNI_NIE):
        #Creamos los objetos de la ficha nueva oportunidad
        self.crmOportunidades.clienteCIF_edit("css selector",'#fo-input-cliente', DNI_NIE)
        self.crmOportunidades.panelFichaOportunidad("xpath","//div[@id='panel_estados_oportunidades']")
        self.crmOportunidades.buscarCliente_button("css selector",'#fo-btn-buscar-cliente')
        self.crmOportunidades.cancelarBuscarCliente_button("css selector",'#bt-cancelar-oportunidad')
        self.crmOportunidades.crearOportunidad_button("css selector",'#bt-crear-oportunidad')
        self.crmOportunidades.cancelarOportunidad_button("css selector",'#bt-cancelar-oportunidad')
        self.crmOportunidades.cuadro_De_Busqueda_Cliente_select2("xpath","//span[@id='select2-fo-select-cliente-container']")
        self.crmOportunidades.cuadro_De_Busqueda_Cliente_Opcion("xpath","//input[@class='select2-search__field']",DNI_NIE)
        self.crmOportunidades.crearOportunidad_button_click()
        
    def duplicar_editarFicha(self,catalogo,usuarioCRM):
        
        self.crmOportunidades.preclonarOportunidad_button("xpath","//button[@id='bt_pre_clonar_oportunidad']")
        self.crmOportunidades.clonarOportunidad_button("xpath","//button[@id='bt_clonar_oportunidad']")
        self.crmOportunidades.ofertas_TabPage("xpath","//a[@href='#tab_oferta']")
        #ahora procedemos a editar los ajustes de la oportunidad
        self.crmOportunidades.configuracionFichaCliente_button("xpath", "(//button[@type='button'])[1]")
        self.crmOportunidades.configuracionesOportunidad_button("xpath","//div[@class='btn-group open']//a[@class='bt_opciones'][normalize-space()='Configuración']")
        self.crmOportunidades.abrir_Ficha_Ultima_Oportunidad_Clonada("xpath","//div[@id='tab_oferta']//table[@id='table_oportunidades_oferta']/tbody/tr[1]//button[@title='Pedido']")
        self.crmOportunidades.configuraciones_catalogo_select("xpath","//select[@id='filtro_select_catalogo']",catalogo)
        self.crmOportunidades.clonarOportunidad_button_click()
        
        self.crmOportunidades.configuracionFichaCliente_button("xpath", "//div[@id='tab_oferta']//table[@id='table_oportunidades_oferta']/tbody/tr[1]//button[@type='button'][1]")
        self.crmOportunidades.configuracionesOportunidad_button("xpath","//div[@class='btn-group open']//a[@class='bt_opciones'][normalize-space()='Configuración']")
        
        self.crmOportunidades.abrir_Ficha_Ultima_Oportunidad_Clonada("xpath","//div[@id='tab_oferta']//table[@id='table_oportunidades_oferta']/tbody/tr[1]//button[@title='Pedido']")
        self.crmOportunidades.configuraciones_catalogo_select("xpath","//select[@id='filtro_select_catalogo']",catalogo)
        self.crmOportunidades.guardarConfiguracionesOportunidad_button("xpath","//button[@id='bt_guardar_opciones']")
        self.crmOportunidades.editarAjustesFichaClonada()
        self.crmOportunidades.editarFichaOportunidadClonada()
    
    def editarAjustesOportunidad(self, catalogo, usuarioCRM):
        #volvemos a la pantalla principal de Oportunidades, ya con la oportunidad agregada.
        #ahora procedemos a editar los ajustes de la oportunidad
        self.crmOportunidades.configuracionFichaCliente_button("xpath", "(//button[@type='button'])[1]")
        self.crmOportunidades.configuracionesOportunidad_button("xpath","//div[@class='btn-group open']//a[@class='bt_opciones'][normalize-space()='Configuración']")

        self.crmOportunidades.configuracionFichaCliente_button_click()
        self.crmOportunidades.configuracionesOportunidad_button_click()
        #hasta este punto ya tengo abierta la ficha de configuracion de la oportunidad
        self.crmOportunidades.configuraciones_catalogo_select("xpath","//select[@id='filtro_select_catalogo']",catalogo)
        self.crmOportunidades.configuraciones_usuarioAsignado_select2("xpath","//span[@aria-labelledby='select2-filtro_usuarios_asignado-container']")
        self.crmOportunidades.configuraciones_usuarioAsignado_Opcion("xpath","//input[@class='select2-search__field']",usuarioCRM)
        self.crmOportunidades.guardarConfiguracionesOportunidad_button("xpath","//button[@id='bt_guardar_opciones']")
        self.crmOportunidades.guardarConfiguracionesOportunidad_button_click()

    def clicEditarPedido(self):
        #Ahora doy clic en editar pedido
        
        self.crmOportunidades.abrirPaginaDelPedido_button("xpath","(//button[@title='Pedido'])[1]")
        return self.crmOportunidades.abrirPaginaDelPedido_button_click()
        #En este punto del codigo, ya estamos en la pagina de edicion del pedido, osea procedemos a llenar los datos.
        #pero hay que controlar cuando hay varios pedidos, asi que primero que copie una venta.
        #Ahora estamos ya en la pagina de edicion del pedido, aqui sucede una condicion,
        #depende el programa, usaremos un codigo u otro... definimos clases por cada tipo
        #de programa