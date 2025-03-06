import json
import os
import re
import CRMONE_V2

class fichaEnergiaCRM:
    def __init__(self, driver):
        self.driver=driver
        self.crmFichaEnergia=CRMONE_V2.fichaEnergiaCRM(driver)
        
    def llenarContratoLuz(self, Contrato, CUPS):
        #Inicializo todas las variables y metodos de la clase Ficha de Energia
        
        #Aqui es donde establecemos los valores de referencia para los objetos
        #que se encuentran dentro de la estrcutura del boton LUZ, lo hacemos solo si el valor del
        #Contrato LUZ no es vacio., verificando que su longitud sea mayor a 0 caracteres
        #Se ha elegido un contrato de luz, procedemos a agregarlo y editar su CUPS
        self.crmFichaEnergia.añadirContratoLuz_button("xpath","//button[normalize-space()='LUZ']")
        self.crmFichaEnergia.listadoTarifas_select("xpath","(//select[@class='form-control'])[1]",Contrato)
        self.crmFichaEnergia.añadirTarifa_button("xpath","(//button[@class='hp-button btn btn-primary sombra-josu2 btn-sm'][normalize-space()='AÑADIR'])[1]")
        self.crmFichaEnergia.añadirContratoLuz_button_click()
        self.crmFichaEnergia.añadirTarifa_button_click()
        #Ahora que hemos añadido el contrato procedemos a actualizar sus valores de CUPS
        self.crmFichaEnergia.ultimoContratoAgregado_Span("xpath","//span[@class='literal' and contains(text(), '" + Contrato + "')]",Contrato)
        self.crmFichaEnergia.numeroCUPS_input("xpath","//div[@class='col-sm-4']//input[@type='text']",CUPS)
        self.crmFichaEnergia.ultimoContratoAgregado_Span_click()
        self.crmFichaEnergia.guardarCUPS_button("xpath","//button[@class='hp-button btn btn-sm btn-primary sombra-josu2']")
        self.crmFichaEnergia.guardarCUPS_button_click()
        print("El contrato de LUZ se ha agregado correctamente")

    def llenarContratoGas(self,Contrato, CUPS):        
        #Agregamos el contrato de Gas si es que se eligio alguno
        self.crmFichaEnergia.añadirContratoGas_button("xpath","//button[normalize-space()='GAS']")    
        self.crmFichaEnergia.listadoTarifas_select("xpath","(//select[@class='form-control'])[1]",Contrato)
        self.crmFichaEnergia.añadirTarifa_button("xpath","(//button[@class='hp-button btn btn-primary sombra-josu2 btn-sm'][normalize-space()='AÑADIR'])[1]")
        self.crmFichaEnergia.añadirContratoGas_button_click()
        self.crmFichaEnergia.añadirTarifa_button_click()
        #Ahora que hemos añadido el contrato procedemos a actualizar sus valores de CUPS
        self.crmFichaEnergia.ultimoContratoAgregado_Span("xpath","//span[@class='literal' and contains(text(), '" + Contrato + "')]",Contrato)
        self.crmFichaEnergia.numeroCUPS_input("xpath","//div[@class='col-sm-4']//input[@type='text']",CUPS)
        self.crmFichaEnergia.ultimoContratoAgregado_Span_click()        
        self.crmFichaEnergia.guardarCUPS_button("xpath","//button[@class='hp-button btn btn-sm btn-primary sombra-josu2']")
        self.crmFichaEnergia.guardarCUPS_button_click()
        print("El contrato de GAS se ha agregado correctamente")
        
    def llenarDatosBasicos(self,Provincia,IBAN, Entidad_Bancaria,DNI_NIE, nombreCliente):      
        #Una vez hemos agregado los contratos, procedemos a editar los datos basicos
        self.crmFichaEnergia.editarDatos_button("xpath","//button[normalize-space()='EDITAR DATOS']")    
        self.crmFichaEnergia.editarDatos_button_click()
        #Ya hemos dado click en el boton de EDITAR DATOS
        #Ahora debemos comenzar a llenar los inputs
        self.crmFichaEnergia.segmentoCliente_select("xpath","(//select[@class='form-control'])[1]","PARTICULAR")
        self.crmFichaEnergia.provinciaCliente_select("xpath","(//select[@type='text'])[1]",Provincia)
        #La operadora selecciona en blanco o value a 199, esto para que se guarden los demas datos, sino el CRM no actualiza
        self.crmFichaEnergia.operadora_select("xpath","//div[4]//div[2]//select[1]","199")
        self.crmFichaEnergia.cuentaBancariaIBAN_input("xpath","(//input[@type='text'])[1]",IBAN)
        self.crmFichaEnergia.entidadBancaria_input("xpath","//div[@class='col-xs-12 col-md-4 col-sm-6']//div[2]//div[2]//div[1]//div[2]//input[1]",Entidad_Bancaria)
        self.crmFichaEnergia.CIF_NIF_input("xpath","(//input[@type='text'])[3]",DNI_NIE)
        self.crmFichaEnergia.nombreCliente_input("xpath","(//input[@type='text'])[4]",nombreCliente)
        self.crmFichaEnergia.guardarDatosBasicos_button("xpath","//div[@class='row margin-right-20']//button[@class='hp-button btn btn-primary sombra-josu2 btn-sm'][normalize-space()='GUARDAR']")
        self.crmFichaEnergia.guardarDatosBasicos_button_click()
        #Ya hemos agregado los datos basicos disponibles, ahora
        
    def llenarDatosDireccion(self,Nombre_de_la_Calle,No_Calle, Provincia,Municipio,Cod_Postal,PisoLetra,BloqueEscalera):
        #procedemos a agregar los datos de direccion
        self.crmFichaEnergia.añadirDireccion_button("xpath","//button[normalize-space()='DIRECCIÓN']")
        self.crmFichaEnergia.añadirDireccion_button_click()
        self.crmFichaEnergia.tipoDireccion_select("xpath","//select[@class='form-control v_obligatorio']","INSTALACIÓN")
        self.crmFichaEnergia.direccion_input("xpath","(//input[@type='text'])[5]",Nombre_de_la_Calle)
        self.crmFichaEnergia.numeroCalle_input("xpath","//div[@id='pedido-form-direccion']//div[3]//div[3]//div[1]//div[2]//input[1]",No_Calle)
        self.crmFichaEnergia.provinciaCliente_input("xpath","(//input[@type='text'])[9]",Provincia)
        self.crmFichaEnergia.municipioCliente_input("xpath","(//input[@type='text'])[10]",Municipio)
        self.crmFichaEnergia.codigoPostalCliente_input("xpath","(//input[@type='text'])[11]",Cod_Postal)
        self.crmFichaEnergia.plantaPiso_input("xpath","//div[@class='row']//div[4]//div[1]//div[2]//input[1]",PisoLetra)
        self.crmFichaEnergia.bloqueEscalera_input("xpath","//div[@id='pedido-form-direccion']//div[5]//div[1]//div[2]//input[1]",BloqueEscalera)
        self.crmFichaEnergia.guardarDatosDireccion_button("xpath","//div[@id='pedido-form-direccion']//button[@class='hp-button btn btn-primary sombra-josu2 btn-sm'][normalize-space()='AÑADIR']")
        self.crmFichaEnergia.guardarDatosDireccion_button_click()
        print("Ficha de Energia Completada")
        
        
        #Vale una vez hemos manejado el cliente, procedemos a manejar los contratos que el agente
        #a vendido
         