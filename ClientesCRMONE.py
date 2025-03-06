import CRMONE_V2
from PySide6.QtWidgets import QMessageBox as msg

class ClientesCRMONE:
    def __init__(self, qwidget):
        self.controlPadre=qwidget
        self.navegador=CRMONE_V2.Navegador('https://rsctel.wikitic.es/login.php')
        
    def IniciarSesionCRMONE(self,usuarioCRM,passCRM):
        self.usuarioCRM=usuarioCRM
        self.passCRM=passCRM
        #Primero arrancamos con la parte de verificar si el cliente existe o lo registramos
        #COmenzamos:
        #Navegamos hasta la pagina de Login de CRM
        self.navegador.navegar()
        crmLogin=CRMONE_V2.LoginCRM(self.navegador.driver)
        crmLogin.usuario_edit(usuarioCRM,"name","inp_usuario")
        crmLogin.contraseña_edit(passCRM,"name","inp_pass")
        crmLogin.etiqueta_Login_Incorrecto("xpath","//div[@class='text-danger']")
        crmLogin.ingresar_button("css selector",'button[type="submit"]')
        return crmLogin.loguearse()
     
    def crear_Verificar_Cliente(self,DNI_NIE,nombreCliente):
        print("Verificando Cliente")
        #Ingresar el DNI del cliente y esperar a obtener una respuesta de si existe o no.
        #dependiendo de eso se agrega el cliente o la oportunidad
        self.crmClientes.fichaCliente("xpath","//body/div[@class='wrapper']/div[@class='content-wrapper']/div[@id='panel_ficha_clientes']/div[@id='main-tipificacion-2']/div/div[@role='document']/div[@class='modal-content modal-lg']/div/div[@class='modal-body']/div[1]")
        self.crmClientes.CIFNIF_edit("css selector", 'input[placeholder="CIF"]',DNI_NIE)
        self.crmClientes.RAZON_SOCIAL_edit("css selector",'input[placeholder="Razón Social"]',nombreCliente)
        self.crmClientes.iconoResultadoBusquedaCliente_i("xpath","//i[@class='fa fa-ban']")
        self.crmClientes.resultadoBusquedaCliente_label("css selector",'div[class="campo-contenido form-group"] p span')
        self.crmClientes.crearCliente_button("css selector",'button[class="btn btn-primary"]')
        self.crmClientes.btnCrearCliente_Click()
        print("Cliente Verificado y registrado")         
        
    def AbrirFichaCliente(self):
        try:
            # Voy a la pagina de Clientes en el CRM
            # Hacer clic en el botón "+ Añadir o Buscar Cliente"
            self.crmClientes=CRMONE_V2.ClientesCRM(self.navegador.driver)
            self.crmClientes.driver.get("https://rsctel.wikitic.es/index.php/potenciales")
            self.crmClientes.nuevoCliente_button("css selector",'#bt_nuevo_cliente_nuevo')
            self.crmClientes.btnAbrirFichaCliente_Click()
            return True
        except Exception as e:
            return f"Ha ocurrido el siguiente error al intentar abrir la ficha de cliente: {e}"
