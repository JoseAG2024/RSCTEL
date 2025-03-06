import json
import os
import re
import time
#import atexit
#import signal
import threading
import ClientesCRMONE
import oportunidadesCRMONE
import fichaEnergiaCRMONE
#import subprocess
#import models
#Librerias que necesito para interactuar con el formulario generado por QtDesigner
from PySide6 import QtGui
#from PySide6.QtGui import QKeyEvent, QKeySequence
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtWidgets import QMessageBox as msg
from views.frmPrincipal import Ui_frmPrincipal

class rsctelAgent(QMainWindow, Ui_frmPrincipal):
    def __init__(self):
            super().__init__()
            self.diccionario_datos={}
            self.setupUi(self)  # Inicializar la interfaz de usuario
            self.current_timestamp=""
            self.agregandoFila=False
            self.editandoFila=False
            self.indiceFilaAEditar=-1
            self.todos_contratos_iguales=False
            self.lblEstadoCopiaVenta.setVisible(False)
            self.tabFichas.setTabVisible(1,False)
            
            # Ejecuta el EXE y almacena el proceso
            #cargamos los archivos json
            path = os.path.expanduser('~/Documents/RSCTEL')
            os.makedirs(path, exist_ok=True)  # Crea la carpeta si no existe
            rsctelAgent.script_dir = path
            #Ficha Activa
            #Provincias
            archivoJson=open("provincias.json","r",-1,"utf-8-sig")
            self.provincias=json.load(archivoJson)
            #Tarifas
            archivoJson=open("tarifas.json","r",-1,"utf-8-sig")
            self.tarifas=json.load(archivoJson)
            
            #BANCOS
            archivoJson=open("bancos.json","r",-1,"utf-8-sig")
            self.bancos=json.load(archivoJson)
            
            
            

            #Cargo los datos de la fichaJson
            #Arranco el proceso que verifica en un hilo aparte si la ficha a cambiado
            self.cargarFichaJsonAControles()
            
            self.cmbProvincia.addItems(self.provincias)
            self.cmbProvincia.insertItem(0,"")
            self.cmbProvinciaSuministro.addItems(self.provincias)
            self.cmbProvinciaSuministro.insertItem(0,"")
            
                
            # Inicializa la lista de catalogos
            self.catalogos = [catalogo["nombre"] for catalogo in self.tarifas["Catalogos"]]
            # Carga los nombres de los catalogos en el combobox
            self.cmbCatalogos.addItems(self.catalogos)

            # Conecta el evento de cambio de selección del combobox de catalogos
            self.cmbCatalogos.currentTextChanged.connect(self.cmbCatalogos_currentTextChanged)
            self.cmbTiposContratos.currentTextChanged.connect(self.cmbTiposContratos_currentTextChanged)

            #Ahora conectamos los botones y la tabla a sus respectivos eventos
            self.pBAgregarContrato.clicked.connect(self.pBAgregarContrato_clicked)
            self.pBEliminarContrato.clicked.connect(self.pBEliminarContrato_clicked)
            self.pBEditarContrato.clicked.connect(self.pBEditarContrato_clicked)
            self.pBEnviarVentaACRM.clicked.connect(self.pBEnviarVentaACRM_clicked)
            self.pBGuardarCambiosEnContrato.clicked.connect(self.pBGuardarCambiosEnContrato_clicked)
            self.tWContratos.itemSelectionChanged.connect(self.tWContratos_ItemSelectionChanged)
            self.pBCancelarCambiosEnContrato.clicked.connect(self.pBCancelarCambiosEnContrato_clicked)

            #Aqui preveemos las ventas, si en los datos hay CUPS DE LUZ y de GAS se agregan los contratos predeterminadamente
            #a la lista de contratos vendidos
            #Hago un cambio de indice para disparar el evento de currenttextchanged en cada combobox dependiente
            #Ya que yo agregare manualmente las primeros contratos que me vienen de la ficha
            #Catalogo 1 de Energy Go, que es lo que mas venden ahora mismo
            self.cmbCatalogos.setCurrentIndex(1)
            #Tipo de contrato 0, que es LUZ
            self.cmbTiposContratos.setCurrentIndex(0)
            #Contrato 1, que es Tarifa Batman Fija 24h
            self.cmbContratos.setCurrentIndex(1)

            #Ajustamos el tamaño de cada columna de la tabla
            self.tWContratos.resizeColumnsToContents()
            self.limpiarControlesgBAgregarOEditarContrato()

    def cargarFichaJsonAControles(self):
        # Crear un temporizador que se ejecuta cada 100 ms (0.1 segundos)
        timer = QTimer(self)
        timer.timeout.connect(self.verificarYActualizarFicha)  # Conectar al método de verificación
        timer.start(250)  # Establecer el intervalo del temporizador en milisegundos

    def verificarYActualizarFicha(self):

            if os.path.exists("fichas.json"):
                #Ficha Activa
                archivoJson=open("fichas.json","r",-1,"utf-8-sig")
                self.fichaActiva=json.load(archivoJson)
                # Suponiendo que el archivo JSON tiene una clave 'timestamp'
                self.file_timestamp = self.fichaActiva.get('timestamp')

                if self.file_timestamp != self.current_timestamp:
                    if self.tWContratos.rowCount() > 0:
                        for i in reversed(range(self.tWContratos.rowCount())):
                            self.tWContratos.removeRow(i)
                    # Si las marcas de tiempo son diferentes, ejecutar la acción
                    print(f"Marca de tiempo ha cambiado: {self.file_timestamp}")
                    self.current_timestamp = self.file_timestamp  # Actualiza la marca de tiempo
                    #CARGAMOS DATOS GENERALES DEL CLIENTE
                    # Aquí puedes agregar tu lógica adicional
                    # Asignar texto al QLineEdit llamado txtNombreCliente
                    self.lENombreCliente.setText(self.fichaActiva["fichaEnergia"]["nombreCliente"])
                    self.lEDNI.setText(self.fichaActiva["fichaEnergia"]["DNI_NIE"])
                    self.lECodigoPostal.setText(self.fichaActiva["fichaEnergia"]["codigoPostal"])
                    
                    if str(self.fichaActiva["fichaEnergia"]["provincia"]).title() in self.provincias:
                        self.cmbProvincia.setCurrentText(str(self.fichaActiva["fichaEnergia"]["provincia"]).title())
                    else:
                        self.cmbProvincia.setCurrentIndex(0)
                        
                    self.lEMunicipio.setText(self.fichaActiva["fichaEnergia"]["poblacion"])
                    

                    #Aqui agregamos los datos del CUPS de Luz y Gas
                    self.lECUPS_Gas.setText(self.fichaActiva["fichaEnergia"]["CUPS_GAS"])
                    self.lECUPS_Luz.setText(self.fichaActiva["fichaEnergia"]["CUPS_LUZ"])                        

                    #Aqui rellenamos los datos en el grupo DATOS BANCARIOS
                    self.lENumeroIBAN.textChanged.connect(self.lENumeroIBAN_textChanged)
                    self.lENumeroIBANSuministro.textChanged.connect(self.lENumeroIBAN_textChanged)    
                    self.lENumeroIBAN.setText(self.fichaActiva["fichaEnergia"]["IBAN"])
                        
                        
                    direccion=""
                    direccion=self.fichaActiva["fichaEnergia"]["direccion"]
                    direccion=direccion.split(',')
                    # Asegurándote de que la lista 'direccion' tenga suficientes elementos antes de asignarlos
                    if len(direccion) > 0:
                        self.lENombreCalle.setText(direccion[0])  # Si hay al menos 1 elemento
                    else:
                        self.lENombreCalle.setText("")  # O cualquier valor por defecto

                    if len(direccion) > 1:
                        numeros = re.findall(r'\d+', direccion[1])
                        self.sBNumeroDeLaCalle.setValue(int(numeros[0]) if numeros else 0)  # Si hay al menos 2 elementos
                    else:
                        self.sBNumeroDeLaCalle.setValue(0)  # O valor por defecto (en este caso, 0)

                    if len(direccion) > 2:
                        self.lEPisoYLetra.setText(direccion[2])  # Si hay al menos 3 elementos
                    else:
                        self.lEPisoYLetra.setText("")  # O valor por defecto

                    if len(direccion) > 3:
                        self.lEBloqueOEscalera.setText(direccion[3])  # Si hay al menos 4 elementos
                    else:
                        self.lEBloqueOEscalera.setText("")  # O valor por defecto    
                        
                    #Volvemos a cambiar los combobox para agregar el contrato de Gas si existe un CUPS del Gas y dejamos ahi los combobox
                    #Catalogo 1 de Energy Go, que es lo que mas venden ahora mismo
                    self.cmbCatalogos.setCurrentIndex(1)
                    #Tipo de contrato 0, que es LUZ
                    self.cmbTiposContratos.setCurrentIndex(0)
                    #Contrato 1, que es lo que mas venden
                    self.cmbContratos.setCurrentIndex(1)
                    #Ahora agrego el contrato de Luz si hay CUPS de LUZ
                    if len(self.lECUPS_Luz.text())>0:
                        row=self.tWContratos.rowCount()
                        self.tWContratos.insertRow(row)
                        self.tWContratos.setItem(row,0,QTableWidgetItem(self.cmbCatalogos.currentText()))
                        self.tWContratos.setItem(row,1,QTableWidgetItem(self.cmbTiposContratos.currentText()))
                        self.tWContratos.setItem(row,2,QTableWidgetItem(self.cmbContratos.currentText()))
                        self.tWContratos.setItem(row,3,QTableWidgetItem(self.lECUPS_Luz.text()))
                        self.tWContratos.setItem(row,4,QTableWidgetItem(self.cmbProvincia.currentText()))
                        self.tWContratos.setItem(row,5,QTableWidgetItem(self.lEMunicipio.text()))
                        self.tWContratos.setItem(row,6,QTableWidgetItem(self.lENombreCalle.text()))
                        self.tWContratos.setItem(row,7,QTableWidgetItem(self.sBNumeroDeLaCalle.text()))
                        self.tWContratos.setItem(row,8,QTableWidgetItem(self.lEPisoYLetra.text()))
                        self.tWContratos.setItem(row,9,QTableWidgetItem(self.lEBloqueOEscalera.text()))
                        self.tWContratos.setItem(row,10,QTableWidgetItem(self.lECodigoPostal.text()))
                        self.tWContratos.setItem(row,11,QTableWidgetItem(self.lEEntidad.text()))
                        if len(self.lENumeroIBAN.text().strip())>2:
                            self.tWContratos.setItem(row,12,QTableWidgetItem(self.lENumeroIBAN.text()))
                        else:
                            self.tWContratos.setItem(row,12,QTableWidgetItem(""))

                    #Volvemos a cambiar los combobox para agregar el contrato de Gas si existe un CUPS del Gas y dejamos ahi los combobox
                    #Catalogo 1 de Energy Go, que es lo que mas venden ahora mismo
                    self.cmbCatalogos.setCurrentIndex(1)
                    #Tipo de contrato 1, que es GAS
                    self.cmbTiposContratos.setCurrentIndex(1)
                    #Contrato 0, que es EnergyGo Gas RL. 1
                    self.cmbContratos.setCurrentIndex(0)
                    if len(self.lECUPS_Gas.text())>0:
                        row=self.tWContratos.rowCount()
                        self.tWContratos.insertRow(row)
                        self.tWContratos.setItem(row,0,QTableWidgetItem(self.cmbCatalogos.currentText()))
                        self.tWContratos.setItem(row,1,QTableWidgetItem(self.cmbTiposContratos.currentText()))
                        self.tWContratos.setItem(row,2,QTableWidgetItem(self.cmbContratos.currentText()))
                        self.tWContratos.setItem(row,3,QTableWidgetItem(self.lECUPS_Gas.text()))
                        self.tWContratos.setItem(row,4,QTableWidgetItem(self.cmbProvincia.currentText()))
                        self.tWContratos.setItem(row,5,QTableWidgetItem(self.lEMunicipio.text()))
                        self.tWContratos.setItem(row,6,QTableWidgetItem(self.lENombreCalle.text()))
                        self.tWContratos.setItem(row,7,QTableWidgetItem(self.sBNumeroDeLaCalle.text()))
                        self.tWContratos.setItem(row,8,QTableWidgetItem(self.lEPisoYLetra.text()))
                        self.tWContratos.setItem(row,9,QTableWidgetItem(self.lEBloqueOEscalera.text()))
                        self.tWContratos.setItem(row,10,QTableWidgetItem(self.lECodigoPostal.text()))
                        self.tWContratos.setItem(row,11,QTableWidgetItem(self.lEEntidad.text()))
                        if len(self.lENumeroIBAN.text().strip())>15:
                            self.tWContratos.setItem(row,12,QTableWidgetItem(self.lENumeroIBAN.text()))
                        else:
                            self.tWContratos.setItem(row,12,QTableWidgetItem(""))
                        
                    
            else:
                #Si el archivo JSON de FICHA del CLiente no existe, significa que en el Script
                #windowMonitor se ha detectado el cierre de la ventana Script de OCM,
                #por lo cual procedo a limpiar los datos de la anterior ficha
                self.limpiarTodosLosCampos()
                
    def limpiarTodosLosCampos(self):
        self.limpiarControlesgBAgregarOEditarContrato()
        self.lENombreCliente.setText("")
        self.lEDNI.setText("")
        self.lECodigoPostal.setText("")
        self.cmbProvincia.setCurrentIndex(0)
        self.lEMunicipio.setText("")
        self.lENombreCalle.setText("")
        self.sBNumeroDeLaCalle.setValue(0)
        self.lEPisoYLetra.setText("")
        self.lEBloqueOEscalera.setText("")
        self.lECUPS_Luz.setText("")
        self.lECUPS_Gas.setText("")
        self.lENumeroIBAN.setText("")
        self.lEEntidad.setText("")
        
        #Limpiamos la tabla de datos con un bucle, osea eliminamos cada fila
        filas = self.tWContratos.rowCount()      # Obtener el número de filas
        for fila in reversed(range(0,filas)):
            self.tWContratos.removeRow(fila)
        
    def validarLoginCRM(self):
        if len(self.lEUserCRM.text())<1:
            self.lEUserCRM.setStyleSheet("background-color: red;")
            msg.critical(self,"RSCTEL Agent","El USUARIO de CRM no puede estar vacio.")
            self.lEUserCRM.setStyleSheet("background-color: white;")
            self.lEUserCRM.setFocus()
            return False
        elif len(self.lEPassCRM.text())<1:
            self.lEPassCRM.setStyleSheet("background-color: red;")
            msg.critical(self,"RSCTEL Agent","La CONTRASEÑA de CRM no puede estar vacio.")
            self.lEPassCRM.setStyleSheet("background-color: white;")
            self.lEPassCRM.setFocus()
            return False
        return True
   
    def pBCancelarCambiosEnContrato_clicked(self):
        #El boton que cancela la edicion o el agregado de un contrato, aqui restablecemos las variables relacionadas
        #a la edicion o creacion de un nuevo contrato.
        self.limpiarControlesgBAgregarOEditarContrato()
        self.gBAgregarOEditarContrato.setEnabled(False)
        self.tWContratos.setEnabled(True)
        self.pBAgregarContrato.setEnabled(True)
        self.pBEnviarVentaACRM.setEnabled(True)
        self.pBEliminarContrato.setEnabled(True)
        self.pBEditarContrato.setEnabled(True)
        if self.agregandoFila==True:
            self.agregandoFila=False
        elif self.editandoFila==True:
            self.editandoFila=False
            self.indiceFilaAEditar=-1

    def limpiarControlesgBAgregarOEditarContrato(self):
        self.lECUPS.setText("")
        self.cmbProvinciaSuministro.setCurrentText("")
        self.lEMunicipioSuministro.setText("")
        self.lENombreCalleSuministro.setText("")
        self.sBNumeroCalleSuministro.setValue(0)
        self.lEPisoYLetraSuministro.setText("")
        self.lEBloqueEscaleraSuministro.setText("")
        self.lECodigoPostalSuministro.setText("")
        self.lENumeroIBANSuministro.setText("")
        self.lEEntidadSuministro.setText("")
    
    def pBEnviarVentaACRM_clicked(self):
        #Aqui lo que hare es copiar los datos, almacenarlos en un un diccionario y trabajarlos desde ahi
        #ya que necesito liberar los controles para recibir las llamadas mientras se copia la venta a CRM
        #para ello la logica es la siguiente
        #JOSE AGUILAR G 05/03/2025
        #Si los datos en la ficha estan correctos
            #procedemos a extraer a un diccionario todos los contratos vendidos por el agente con un bucle para basarme en los datos de la tabla
        if self.validarDatosGeneralesCliente()==False:
            print("Validacion de datos generales fallida")
            self.lblEstadoCopiaVenta.setText("Validacion de datos generales fallida")
            self.update()
            return False
        elif self.validarTablaDeContratos()==False:
            print("Validacion de tabla de contratos fallida")
            self.lblEstadoCopiaVenta.setText("Validacion de tabla de contratos fallida")
            self.update()
            return False
        elif self.validarLoginCRM()==False:
            print("Sin Datos de Inicio de Sesion")
            self.lblEstadoCopiaVenta.setText("Sin Datos de Inicio de Sesion")
            self.update()
            return False
        
        self.lblEstadoCopiaVenta.setVisible(True)
        #Envio una actualizacion al sistema.
        self.lblEstadoCopiaVenta.setText("Extrayendo los datos generales de la Venta")
        self.update()
        self.datos_diccionario = {
            'Agente': self.lEUserCRM.text(),
            'Contraseña': self.lEPassCRM.text(),
            'NombreCliente': self.lENombreCliente.text(),
            'DNI_NIE': self.lEDNI.text(),
            'Telefono': "",
            'Ventas': {}
        }

        #Envio una actualizacion al sistema.
        self.lblEstadoCopiaVenta.setText("Extrayendo los datos de los contratos")
        self.update()
        for fila in range(self.tWContratos.rowCount()):
            #Definimos las variables temporales, o de cada contrato, para mejor manejo de codigo.
            #Viva la libertad carajo....
            self.datos_diccionario["Ventas"]["Venta_"+str(fila)] = {
                "Catalogo": self.tWContratos.item(fila,0).text(),
                "Tipo_de_Contrato": self.tWContratos.item(fila,1).text(),
                "Contrato": self.tWContratos.item(fila,2).text(),
                "CUPS": self.tWContratos.item(fila,3).text(),
                "Provincia": self.tWContratos.item(fila,4).text(),
                "Municipio": self.tWContratos.item(fila,5).text(),
                "Nombre_de_la_Calle":self.tWContratos.item(fila,6).text(),
                "No_Calle":self.tWContratos.item(fila,7).text(),
                "Piso_Letra":self.tWContratos.item(fila,8).text(),
                "Bloq_Esc":self.tWContratos.item(fila,9).text(),
                "Cod_Postal":self.tWContratos.item(fila,10).text(),
                "Entidad_Bancaria":self.tWContratos.item(fila,11).text(),
                "IBAN":self.tWContratos.item(fila,12).text()
            }
        
        # Nombre de la carpeta y el archivo
        carpeta = "VENTAS"
        archivo = str(self.datos_diccionario["DNI_NIE"]) + "_" + str(self.datos_diccionario["NombreCliente"]) + "_" + str(self.datos_diccionario["Telefono"]) + ".json"

        # Crear la carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Ruta completa del archivo
        ruta_archivo = os.path.join(carpeta, archivo)

        # Guardar el diccionario en el archivo JSON
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(self.datos_diccionario, f, indent=4, ensure_ascii=False)

        #Envio una actualizacion al sistema.
        self.lblEstadoCopiaVenta.setText("Creando Respaldo de la Venta...")
        self.update()
        
        
        #Aqui voy a enviar si preguntamos al usuario si duplicar ficha, o al ser diferentes catalagos, pues duplicamos de una vez
        #Lo unico que hacemos es establecer la variable Contratos_Separados en True o False
        
        if len(self.datos_diccionario["Ventas"])>0:
            # Verificar si todos los 'catalogo' son iguales
            catalogo_values = [venta['Catalogo'] for venta in self.datos_diccionario['Ventas'].values()]
            # Verificar si todos los valores de 'catalogo' son iguales
            self.todos_contratos_iguales = len(set(catalogo_values)) == 1
            
            if self.todos_contratos_iguales ==True:
                if len(self.datos_diccionario["Ventas"])>1:
                    if msg.question(self,"RSCTEL Agent",f"¿Crear una oportunidad para cada Contrato?",msg.StandardButton.Yes ,msg.StandardButton.No):
                        #Metodo que incluye clonar contratos
                        print("Metodo que incluye clonar contratos")
                        self.thread = threading.Thread(target=self.CRMONE_FichaEnergia,args=("ClonarContratos",), daemon=True)
                        self.thread.start()
                else:
                    #metodo que copia todos los contratos en una sola oportunidad
                    print("metodo que copia todos los contratos en una sola oportunidad")
                    self.thread = threading.Thread(target=self.CRMONE_FichaEnergia,args=("AgruparContratos",), daemon=True)
                    self.thread.start()
            else:
                print("Metodo que incluye clonar contratos")
                self.thread = threading.Thread(target=self.CRMONE_FichaEnergia,args=("ClonarContratos",), daemon=True)
                self.thread.start() 
        return True

    #En este metodo es donde sucede la logica para interactuar con el CRMONE
    def CRMONE_FichaEnergia(self,metodo_de_Copia):
        try:
            #realizo verificaciones de catalagos para saber si procedemos con duplicados o no
            #si hay catalagos diferentes entonces
                #automaticamente me voy por el camino de duplicar
            #si no hay catalagos diferentes entonces
                #muestro un mensaje en el que pregunto si quiere una sola oportunidad o crear una por catalogo

            #Asignamos las variables generales
            self.idOportunidadCRMONE=""
            usuarioCRM= self.datos_diccionario["Agente"]
            passCRM=self.datos_diccionario["Contraseña"]
            nombreCliente=self.datos_diccionario["NombreCliente"]
            DNI_NIE=self.datos_diccionario["DNI_NIE"]
            
            Ficha_Clientes=ClientesCRMONE.ClientesCRMONE(self)
            #Envio una actualizacion al sistema.
            self.lblEstadoCopiaVenta.setText("Iniciando Sesion en CRMONE")
            self.update()
            if Ficha_Clientes.IniciarSesionCRMONE(usuarioCRM,passCRM)==False:
                #Envio una actualizacion al sistema.
                self.lblEstadoCopiaVenta.setText("Usuario o Contraseña de CRMONE incorrectos.")
                self.update()
                time.sleep(30)
                self.lblEstadoCopiaVenta.setVisible=False
                return
            #Envio una actualizacion al sistema.
            self.lblEstadoCopiaVenta.setText("Verificando si existe cliente...")
            self.update()
            
            self.lblEstadoCopiaVenta.setText(str(Ficha_Clientes.AbrirFichaCliente()))
            self.update()
            Ficha_Clientes.crear_Verificar_Cliente(DNI_NIE,nombreCliente)

            

            filas = len(self.datos_diccionario["Ventas"])      # Obtener el número de filas
            #COmienzo a recorrer la cantidad de filas en la tabla, que es igual a la cantidad de contratos vendidos.
            #EN la tabla estan los datos unicos para el contrato, si el usuario marca la opcion
            #crear oportunidad por cada contrato, entonces deberemos hacer un "duplicar" a la primer ficha que se
            #añada al crm, ya que es la unica manera de ingresar contratos por separados, osea que en ese punto la logica cambia, el resto de
            #añadir el cliente es unico igual que la primera oportunidad, si el usuario ha marcado que se añadan los contratos por separado
            #no esta pidiendo que en CRM dupliquemos la oportunidad y la llenemos

            
            #El comportamiento o la logica aqui, no son los esperados, revisarlo el viernes 20/02/2025
            #La logica deberia ser:
            
                #Si hay dos o mas contratos, y la opcion de contratos por oportunidades separadas esta deshabilitada o solo hay un contrato
            if metodo_de_Copia=="AgruparContratos":
                #entonces lo que debo de hacer es ir a oportunidades
                print("Filas" + str(filas)) 
                Ficha_Oportunidades=oportunidadesCRMONE.oportunidadesCRMONE(self, Ficha_Clientes.navegador.driver)
                #Envio una actualizacion al sistema.
                self.lblEstadoCopiaVenta.setText("Comenzando la creacion de las oportunidades en CRMONE")
                self.update()
                Ficha_Oportunidades.abrirFichaOportunidad()
                #crear una nueva oportunidad
                #Envio una actualizacion al sistema.
                self.lblEstadoCopiaVenta.setText("Creando Nueva Oportunidad...")
                self.update()
                Ficha_Oportunidades.crearOportunidad(DNI_NIE)
                #editar los ajustes de esa oportunidad
                #establecer el catalogo y el agente asignado
                #luegho dar clic en guardar
                #Envio una actualizacion al sistema.
                self.lblEstadoCopiaVenta.setText("Configurando el Catalogo")
                self.update()
                catalogo=self.datos_diccionario["Ventas"]["Venta_0"]["Catalogo"]
                Ficha_Oportunidades.editarAjustesOportunidad(catalogo,usuarioCRM)
                #Envio una actualizacion al sistema.
                self.lblEstadoCopiaVenta.setText("Comenzando a Llenar la Ficha")
                self.update()
                self.idOportunidadCRMONE=Ficha_Oportunidades.clicEditarPedido()
                #recorrer los contratos en la tabla de contratos agregados y por cada uno dee ellos hacer lo siguente
                for fila in range(filas):
                    #Definimos las variables temporales, o de cada contrato, para mejor manejo de codigo.
                    #Viva la libertad carajo....
                    catalogo=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Catalogo"]       
                    Tipo_de_Contrato=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Tipo_de_Contrato"]
                    Contrato=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Contrato"]   
                    CUPS=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["CUPS"]
                    Provincia=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Provincia"]
                    Municipio=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Municipio"]
                    Nombre_de_la_Calle=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Nombre_de_la_Calle"]
                    No_Calle=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["No_Calle"]
                    Piso_Letra=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Piso_Letra"]
                    Bloq_Esc=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Bloq_Esc"]
                    Cod_Postal=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Cod_Postal"]
                    Entidad_Bancaria=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Entidad_Bancaria"]
                    IBAN=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["IBAN"]
                    #En la oportunidad agregar los productos en la misma ficha
                    Ficha_Energia=fichaEnergiaCRMONE.fichaEnergiaCRM(Ficha_Oportunidades.driver)
                    

                    if Tipo_de_Contrato=="Luz":
                        #Envio una actualizacion al sistema.
                        self.lblEstadoCopiaVenta.setText("Llenando datos del Contrato de Luz " + Contrato)
                        self.update()
                        Ficha_Energia.llenarContratoLuz(Contrato,CUPS)
                    elif Tipo_de_Contrato=="Gas":
                        #Envio una actualizacion al sistema.
                        self.lblEstadoCopiaVenta.setText("Llenando datos del Contrato de Gas " + Contrato)
                        self.update()
                        Ficha_Energia.llenarContratoGas(Contrato,CUPS)
                #aqui termina la repeticion del ciclo por cada contrato
                #~Editar datos basicos
                #Envio una actualizacion al sistema.
                self.lblEstadoCopiaVenta.setText("Llenando los datos basicos del cliente...")
                self.update()
                Ficha_Energia.llenarDatosBasicos(Provincia,IBAN,Entidad_Bancaria,DNI_NIE,nombreCliente)
                #editar datos de direccion
                #Envio una actualizacion al sistema.
                self.lblEstadoCopiaVenta.setText("Llenando las direcciones...")
                self.update()
                Ficha_Energia.llenarDatosDireccion(Nombre_de_la_Calle,No_Calle,Provincia,Municipio,Cod_Postal,Piso_Letra, Bloq_Esc)
            else:
                #recorrer los contratos en la tabla de contratos agregados y para cada uno de ellos hacer lo siguente
                #Envio una actualizacion al sistema.
                self.lblEstadoCopiaVenta.setText("Recorriendo las ventas...")
                self.update() 
                for fila in range(filas):
                    #Definimos las variables temporales, o de cada contrato, para mejor manejo de codigo.
                    #Viva la libertad carajo....
                    catalogo=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Catalogo"]       
                    Tipo_de_Contrato=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Tipo_de_Contrato"]
                    Contrato=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Contrato"]   
                    CUPS=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["CUPS"]
                    Provincia=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Provincia"]
                    Municipio=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Municipio"]
                    Nombre_de_la_Calle=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Nombre_de_la_Calle"]
                    No_Calle=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["No_Calle"]
                    Piso_Letra=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Piso_Letra"]
                    Bloq_Esc=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Bloq_Esc"]
                    Cod_Postal=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Cod_Postal"]
                    Entidad_Bancaria=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["Entidad_Bancaria"]
                    IBAN=self.datos_diccionario["Ventas"]["Venta_"+str(fila)]["IBAN"]
                    #si la fila es 0, osea es el primer contrato de la tabla
                    if fila==0:
                        #entonces lo que debo de hacer es ir a oportunidades
                        Ficha_Oportunidades=oportunidadesCRMONE.oportunidadesCRMONE(self, Ficha_Clientes.navegador.driver)
                        #Envio una actualizacion al sistema.
                        self.lblEstadoCopiaVenta.setText("Creando la Primera Oportunidad")
                        self.update()
                        Ficha_Oportunidades.abrirFichaOportunidad()
                        #crear una nueva oportunidad
                        Ficha_Oportunidades.crearOportunidad(DNI_NIE)
                        #editar los ajustes de esa oportunidad
                        #establecer el catalogo y el agente asignado
                        #luegho dar clic en guardar
                        #Envio una actualizacion al sistema.
                        self.lblEstadoCopiaVenta.setText("Editando ajustes de catalogo " + catalogo)
                        self.update()
                        Ficha_Oportunidades.editarAjustesOportunidad(catalogo,usuarioCRM)
                        #editar la oportunidad
                        #Envio una actualizacion al sistema.
                        self.lblEstadoCopiaVenta.setText("Comenzando a Llenar la Ficha")
                        self.update()
                        
                        self.idOportunidadCRMONE=Ficha_Oportunidades.clicEditarPedido()
                        #En la oportunidad agregar solo la primera fila de contratos
                        #En la oportunidad agregar los productos en la misma ficha
                        Ficha_Energia=fichaEnergiaCRMONE.fichaEnergiaCRM(Ficha_Oportunidades.driver)
                        if Tipo_de_Contrato=="Luz":
                            #Envio una actualizacion al sistema.
                            self.lblEstadoCopiaVenta.setText("Llenando datos del Contrato de Luz " + Contrato)
                            self.update()
                            Ficha_Energia.llenarContratoLuz(Contrato,CUPS)
                        elif Tipo_de_Contrato=="Gas":
                             #Envio una actualizacion al sistema.
                            self.lblEstadoCopiaVenta.setText("Llenando datos del Contrato de Gas " + Contrato)
                            self.update()
                            Ficha_Energia.llenarContratoGas(Contrato,CUPS)
                        #~Editar datos basicos
                        #Envio una actualizacion al sistema.
                        self.lblEstadoCopiaVenta.setText("Llenando los datos basicos del cliente...")
                        self.update()
                        Ficha_Energia.llenarDatosBasicos(Provincia,IBAN,Entidad_Bancaria,DNI_NIE,nombreCliente)
                        #editar datos de direccion
                        #Envio una actualizacion al sistema.
                        self.lblEstadoCopiaVenta.setText("Llenando las direcciones...")
                        self.update()
                        Ficha_Energia.llenarDatosDireccion(Nombre_de_la_Calle,No_Calle,Provincia,Municipio,Cod_Postal,Piso_Letra,Bloq_Esc)
                    #si la fila es mayor que 0,
                    elif fila>0:
                        #entonces lo que debo de hacer es ir a oportunidades
                        Ficha_Oportunidades=oportunidadesCRMONE.oportunidadesCRMONE(self, Ficha_Clientes.navegador.driver)
                        
                        Ficha_Oportunidades.abrirFichaOportunidad()        
                        #Duplicar la Ultima oportunidad
                        #editar la oportunidad
                        #Envio una actualizacion al sistema.
                        self.lblEstadoCopiaVenta.setText("Creando copia de la Ficha...")
                        self.update()
                        Ficha_Oportunidades.duplicar_editarFicha(catalogo,usuarioCRM)                   
                        #En la oportunidad agregar solo la fila actual de contratos
                        Ficha_Energia=fichaEnergiaCRMONE.fichaEnergiaCRM(Ficha_Oportunidades.driver)
                        #Envio una actualizacion al sistema.
                        self.lblEstadoCopiaVenta.setText("Comenzando a Llenar la Ficha")
                        self.update()
                        if Tipo_de_Contrato=="Luz":
                            #Envio una actualizacion al sistema.
                            self.lblEstadoCopiaVenta.setText("Llenando datos del Contrato de Luz " + Contrato)
                            self.update()
                            Ficha_Energia.llenarContratoLuz(Contrato,CUPS)
                        elif Tipo_de_Contrato=="Gas":
                             #Envio una actualizacion al sistema.
                            self.lblEstadoCopiaVenta.setText("Llenando datos del Contrato de Gas " + Contrato)
                            self.update()
                            Ficha_Energia.llenarContratoGas(Contrato,CUPS)
                        #~Editar datos basicos
                        #Envio una actualizacion al sistema.
                        self.lblEstadoCopiaVenta.setText("Llenando los datos basicos del cliente...")
                        self.update()
                        Ficha_Energia.llenarDatosBasicos(Provincia,IBAN,Entidad_Bancaria,DNI_NIE,nombreCliente)
                        #editar datos de direccion
                        #Envio una actualizacion al sistema.
                        self.lblEstadoCopiaVenta.setText("Llenando las direcciones...")
                        self.update()
                        Ficha_Energia.llenarDatosDireccion(Nombre_de_la_Calle,No_Calle,Provincia,Municipio,Cod_Postal,Piso_Letra,Bloq_Esc)    
            if Ficha_Energia.driver!=None:
                Ficha_Energia.driver.quit()
                
            self.lblEstadoCopiaVenta.setText("La venta ha sido registrada con Exito en CRMONE con ID: " + self.idOportunidadCRMONE)
            self.update()               
            time.sleep(20)
            self.lblEstadoCopiaVenta.setVisible(False)
        except Exception as e:
            self.lblEstadoCopiaVenta.setText(f"Error:{e} No se ha podido copiar la venta. Archivo respaldado en la carpeta: " + self.script_dir + "/VENTAS")
            self.update()
            time.sleep(120)
            self.lblEstadoCopiaVenta.setVisible(False)

    def validarDatosGeneralesCliente(self):
        #Validare los controles que son obligatorios uno a uno, 
        #Esta funcion estara expensa a mejora y optimizacion de codigo
        #Comenzamos por el nombre del cliente
        if len(self.lENombreCliente.text())<3:
            self.lENombreCliente.setStyleSheet("background-color: red;")
            msg.critical(self,"RSCTEL Agent","El nombre del cliente no puede ser vacio o imcompleto.")
            self.lENombreCliente.setStyleSheet("background-color: white;")
            self.lENombreCliente.setFocus()
            return False
        elif len(self.lEDNI.text())<9:
            self.lEDNI.setStyleSheet("background-color: red;")
            msg.critical("RSCTEL Agent","El DNI o NIE introducido esta incompleto.")
            self.lEDNI.setStyleSheet("background-color: white;")
            self.lEDNI.setFocus()
            return False
            exit()
        elif len(self.lECodigoPostal.text())<5:
            self.lECodigoPostal.setStyleSheet("background-color: red;")
            msg.critical(self,"RSCTEL Agent","Verifica que el codigo postal tiene 5 digitos")
            self.lECodigoPostal.setStyleSheet("background-color: white;")
            self.lECodigoPostal.setFocus()
            return False
        elif self.cmbProvincia.currentText()=="":
            self.cmbProvincia.setStyleSheet("background-color: red;")
            msg.critical(self,"RSCTEL Agent","No hay una provincia seleccionada")
            self.cmbProvincia.setStyleSheet("background-color: white;")
            self.cmbProvincia.setFocus()
            return False
        elif len(self.lEMunicipio.text())<1:
            self.lEMunicipio.setStyleSheet("background-color: red;")
            msg.critical(self,"RSCTEL Agent","Verifica que el nombre del municipio no este vacio")
            self.lEMunicipio.setStyleSheet("background-color: white;")
            self.lEMunicipio.setFocus()
            return False
        elif len(self.lENombreCalle.text())<1:
            self.lENombreCalle.setStyleSheet("background-color: red;")
            msg.critical(self,"RSCTEL Agent","Verifica que el nombre de la calle no este vacio")
            self.lENombreCalle.setStyleSheet("background-color: white;")
            self.lENombreCalle.setFocus()
            return False
        elif len(self.lEPisoYLetra.text())<1:
            self.lEPisoYLetra.setStyleSheet("background-color: red;")
            msg.critical(self,"RSCTEL Agent","Verifica que el Piso y Letra esten correctos")
            self.lEPisoYLetra.setStyleSheet("background-color: white;")
            self.lEPisoYLetra.setFocus()
            return False
        return True
            
    def validarTablaDeContratos(self):

        filas = self.tWContratos.rowCount()      # Obtener el número de filas
        columnas_a_validar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12]  # Índices de las columnas que quieres validar 

        for fila in range(filas):
            for columna in columnas_a_validar:
                item = self.tWContratos.item(fila, columna)  # Obtener el item de la celda

                #Validare solo ciertas columnas
                if item is None or item.text()=="":
                    if item != None:
                        self.tWContratos.item(fila, columna).setBackground(QtGui.Qt.GlobalColor(QtGui.Qt.GlobalColor.red))
                    match columna:
                        case 0:
                            msg.critical(self,"RSCTEL Agent",f"El Catalogo no puede estar vacio. \nRevisa la Fila: {fila + 1} En los Productos Vendidos.")
                            return False
                        case 1:
                            msg.critical(self,f"RSCTEL Agent",f"El Tipo de Contrato no puede estar vacio. \nRevisa la Fila: {fila + 1} En los Productos Vendidos.")
                            return False
                        case 2:
                            msg.critical(self,f"RSCTEL Agent",f"El Contrato no puede estar vacio. \nRevisa la Fila: {fila + 1} En los Productos Vendidos.")
                            return False
                        case 3:
                            msg.critical(self,f"RSCTEL Agent",f"El CUPS no puede estar vacio. \nRevisa la Fila: {fila + 1} En los Productos Vendidos.")
                            return False
                        case 4:
                            msg.critical(self,f"RSCTEL Agent",f"La Provincia no puede estar vacio. \nRevisa la Fila: {fila + 1} En los Productos Vendidos.")
                            return False
                        case 5:
                            msg.critical(self,f"RSCTEL Agent",f"El Municipio no puede estar vacio. \nRevisa la Fila: {fila + 1} En los Productos Vendidos.")
                            return False
                        case 6:
                            msg.critical(self,f"RSCTEL Agent",f"El Nombre de la Calle no puede estar vacio. \nRevisa la Fila: {fila + 1} En los Productos Vendidos.")
                            return False
                        case 7:
                            msg.critical(self,f"RSCTEL Agent",f"El No. de Calle no puede estar vacio. \nRevisa la Fila: {fila + 1} En los Productos Vendidos.")
                            return False
                        case 8:
                            msg.critical(self,f"RSCTEL Agent",f"El Piso y Letra no puede estar vacio. \nRevisa la Fila: {fila + 1} En los Productos Vendidos.")
                            return False
                        case 10:
                            msg.critical(self,f"RSCTEL Agent",f"El Código Postal no puede estar vacio. \nRevisa la Fila: {fila + 1} En los Productos Vendidos.")
                            return False
                        case 12:
                            msg.critical(self,f"RSCTEL Agent",f"El IBAN no puede estar vacio. \nRevisa la Fila: {fila + 1} En los Productos Vendidos.")
                            return False
                    if item != None:
                        self.tWContratos.item(fila, columna).setBackground(QtGui.Qt.GlobalColor(QtGui.Qt.GlobalColor.white))
        print("Contratos validados")
        return True
    
    def validarControles_gBAgregarOEditarContrato(self):
        if len(self.lECUPS.text())<20:
            self.lECUPS.setStyleSheet("background-color: red;")
            msg.critical(self,"RSCTEL Agent","CUPS incompleto, por favor revisa.")
            self.lECUPS.setStyleSheet("background-color: white;")
            self.lECUPS.setFocus()
            return False
        elif self.cmbProvinciaSuministro.currentText()=="":
            self.cmbProvinciaSuministro.setStyleSheet("background-color: red;")
            msg.critical(self,"RSCTEL Agent","No hay una provincia seleccionada")
            self.cmbProvinciaSuministro.setStyleSheet("background-color: white;")
            self.cmbProvinciaSuministro.setFocus()
            return False
        elif len(self.lEMunicipioSuministro.text())<1:
            self.lEMunicipioSuministro.setStyleSheet("background-color: red;")
            msg.critical(self,"RSCTEL Agent","Verifica que el nombre del municipio no este vacio")
            self.lEMunicipioSuministro.setStyleSheet("background-color: white;")
            self.lEMunicipioSuministro.setFocus()
            return False
        elif len(self.lENombreCalleSuministro.text())<1:
            self.lENombreCalleSuministro.setStyleSheet("background-color: red;")
            msg.critical(self,"RSCTEL Agent","Verifica que el nombre de la calle no este vacio")
            self.lENombreCalleSuministro.setStyleSheet("background-color: white;")
            self.lENombreCalleSuministro.setFocus()
            return False
        elif len(self.lEPisoYLetraSuministro.text())<1:
            self.lEPisoYLetraSuministro.setStyleSheet("background-color: red;")
            msg.critical(self,"RSCTEL Agent","Verifica que el Piso y Letra esten correctos")
            self.lEPisoYLetraSuministro.setStyleSheet("background-color: white;")
            self.lEPisoYLetraSuministro.setFocus()
            return False
        elif len(self.lECodigoPostalSuministro.text())<5:
            self.lECodigoPostalSuministro.setStyleSheet("background-color: red;")
            msg.critical(self,"RSCTEL Agent","Verifica que el codigo postal tiene 5 digitos")
            self.lECodigoPostalSuministro.setStyleSheet("background-color: white;")
            self.lECodigoPostalSuministro.setFocus()
            return False
        elif len(self.lENumeroIBANSuministro.text())<28:
            self.lENumeroIBANSuministro.setStyleSheet("background-color: red;")
            msg.critical(self,"RSCTEL Agent","Verifica que el IBAN del suminsitro este correcto.")
            self.lENumeroIBANSuministro.setStyleSheet("background-color: white;")
            self.lENumeroIBANSuministro.setFocus()
            return False
            
        return True
         
    #Evento click del boton agregar contrato nuevo
    def pBAgregarContrato_clicked(self):
        """"
        Esta funcion lo que hace es que habilita el groupBox de datos del contrato
        deshabilita la tabla y el boton agregar datos.
        y limpia los datos del groupBox
        """
        self.agregandoFila=True
        self.gBAgregarOEditarContrato.setEnabled(True)
        self.tWContratos.setEnabled(False)
        self.pBAgregarContrato.setEnabled(False)
        self.pBEliminarContrato.setEnabled(False)
        self.pBEditarContrato.setEnabled(False)
        self.pBGuardarCambiosEnContrato.setEnabled(True)
        self.pBEnviarVentaACRM.setEnabled(False)

    def pBGuardarCambiosEnContrato_clicked(self):
        #Podemos estar en dos posibles estados, agregando un contrato nuevo
        #o podemos bien estar editando un contrato
        #primero validamos los controles dentro del GruopBox
        
        if self.validarControles_gBAgregarOEditarContrato()==True:
            if self.agregandoFila==True:
                #Cuando es agregar una fila, el row toma el valor de la ultima
                #fila de la tabla, ya que el boton agregar contrato
                #añade una fila vacia al final de la tabla, la cual es su indice
                #el conteo de filas totales en la tabla
                row=self.tWContratos.rowCount()
                self.tWContratos.insertRow(row)
                print("LLenar los datos a la tabla")
                self.tWContratos.setItem(row,0,QTableWidgetItem(self.cmbCatalogos.currentText()))
                self.tWContratos.setItem(row,1,QTableWidgetItem(self.cmbTiposContratos.currentText()))
                self.tWContratos.setItem(row,2,QTableWidgetItem(self.cmbContratos.currentText()))
                self.tWContratos.setItem(row,3,QTableWidgetItem(self.lECUPS.text()))
                self.tWContratos.setItem(row,4,QTableWidgetItem(self.cmbProvinciaSuministro.currentText()))
                self.tWContratos.setItem(row,5,QTableWidgetItem(self.lEMunicipioSuministro.text()))
                self.tWContratos.setItem(row,6,QTableWidgetItem(self.lENombreCalleSuministro.text()))
                self.tWContratos.setItem(row,7,QTableWidgetItem(self.sBNumeroCalleSuministro.text()))
                self.tWContratos.setItem(row,8,QTableWidgetItem(self.lEPisoYLetraSuministro.text()))
                self.tWContratos.setItem(row,9,QTableWidgetItem(self.lEBloqueEscaleraSuministro.text()))
                self.tWContratos.setItem(row,10,QTableWidgetItem(self.lECodigoPostalSuministro.text()))
                self.tWContratos.setItem(row,11,QTableWidgetItem(self.lEEntidadSuministro.text()))
                self.tWContratos.setItem(row,12,QTableWidgetItem(self.lENumeroIBANSuministro.text()))
                #Habilitamos la puta tabla con los putos botones
                self.tWContratos.setEnabled(True)
                self.pBEliminarContrato.setEnabled(False)
                self.pBEditarContrato.setEnabled(False)
                self.pBAgregarContrato.setEnabled(True)
                self.gBAgregarOEditarContrato.setEnabled(False)
                self.agregandoFila=False
                
            elif self.editandoFila==True:
                #Cambiamos el valor a de row al valor de Indice de Fila a Editar que es la variable
                #que captura el numero de la fila que se esta editando cuando se le da clic
                #al boton de editar
                row=self.indiceFilaAEditar
                print("Editando la puta fila")
                print("LLenar los datos a la tabla")
                self.tWContratos.setItem(row,0,QTableWidgetItem(self.cmbCatalogos.currentText()))
                self.tWContratos.setItem(row,1,QTableWidgetItem(self.cmbTiposContratos.currentText()))
                self.tWContratos.setItem(row,2,QTableWidgetItem(self.cmbContratos.currentText()))
                self.tWContratos.setItem(row,3,QTableWidgetItem(self.lECUPS.text()))
                self.tWContratos.setItem(row,4,QTableWidgetItem(self.cmbProvinciaSuministro.currentText()))
                self.tWContratos.setItem(row,5,QTableWidgetItem(self.lEMunicipioSuministro.text()))
                self.tWContratos.setItem(row,6,QTableWidgetItem(self.lENombreCalleSuministro.text()))
                self.tWContratos.setItem(row,7,QTableWidgetItem(self.sBNumeroCalleSuministro.text()))
                self.tWContratos.setItem(row,8,QTableWidgetItem(self.lEPisoYLetraSuministro.text()))
                self.tWContratos.setItem(row,9,QTableWidgetItem(self.lEBloqueEscaleraSuministro.text()))
                self.tWContratos.setItem(row,10,QTableWidgetItem(self.lECodigoPostalSuministro.text()))
                self.tWContratos.setItem(row,11,QTableWidgetItem(self.lEEntidadSuministro.text()))
                self.tWContratos.setItem(row,12,QTableWidgetItem(self.lENumeroIBANSuministro.text()))
                #Habilitamos la puta tabla con los putos botones
                self.tWContratos.setEnabled(True)
                self.pBAgregarContrato.setEnabled(True)
                self.pBEliminarContrato.setEnabled(True)
                self.pBEditarContrato.setEnabled(True)
                self.gBAgregarOEditarContrato.setEnabled(False)
                self.editandoFila=False
                self.indiceFilaAEditar=-1
            #Ajustamos el tamaño de cada columna de la tabla
            self.limpiarControlesgBAgregarOEditarContrato()
            self.pBEnviarVentaACRM.setEnabled(True)
            self.tWContratos.resizeColumnsToContents()
        else:
            exit   
                      
    def pBEditarContrato_clicked(self):
        #Verificamos si la fila seleccionada es mayor o igual a cero, en otras palabras
        #verificamos si hay una fila seccionada
        self.indiceFilaAEditar=self.tWContratos.currentRow()
        #Activo el boton para guardar los cambios.
        self.pBGuardarCambiosEnContrato.setEnabled(True)
        #Deshabilito el boton de Enviar A CRM
        self.pBEnviarVentaACRM.setEnabled(False)
        
        if self.indiceFilaAEditar >=0:
            #Si hay una fila selccionada asiganmos los valores a su control correspondiente
            #Tambien al final deshabilitamos los botones y la tabla misma, habilitamos el groupBox donde
            #estan los controles de edicion del contrato
            self.gBAgregarOEditarContrato.setEnabled(True)
            self.cmbCatalogos.setCurrentText(self.tWContratos.item(self.indiceFilaAEditar,0).text())
            self.cmbTiposContratos.setCurrentText(self.tWContratos.item(self.indiceFilaAEditar,1).text())
            self.cmbContratos.setCurrentText(self.tWContratos.item(self.indiceFilaAEditar,2).text())
            self.lECUPS.setText(self.tWContratos.item(self.indiceFilaAEditar,3).text())
            self.cmbProvinciaSuministro.setCurrentText(self.tWContratos.item(self.indiceFilaAEditar,4).text())
            self.lEMunicipioSuministro.setText(self.tWContratos.item(self.indiceFilaAEditar,5).text())
            self.lENombreCalleSuministro.setText(self.tWContratos.item(self.indiceFilaAEditar,6).text())
            
            if self.tWContratos.item(self.indiceFilaAEditar,7).text()=="S/N":
                self.sBNumeroCalleSuministro.setValue(0)
            else:
                self.sBNumeroCalleSuministro.setValue(int(self.tWContratos.item(self.indiceFilaAEditar,7).text()))
            
            
            self.lEPisoYLetraSuministro.setText(self.tWContratos.item(self.indiceFilaAEditar,8).text())
            self.lEBloqueEscaleraSuministro.setText(self.tWContratos.item(self.indiceFilaAEditar,9).text())
            self.lECodigoPostalSuministro.setText(self.tWContratos.item(self.indiceFilaAEditar,10).text())
            self.lEEntidadSuministro.setText(self.tWContratos.item(self.indiceFilaAEditar,11).text())
            self.lENumeroIBANSuministro.setText(self.tWContratos.item(self.indiceFilaAEditar,12).text())
            
            #Deshabilito los botones de Eliminar, Editar y Agregar, y por supuesto el TableView
            self.pBEditarContrato.setEnabled(False)
            self.pBEliminarContrato.setEnabled(False)
            self.pBAgregarContrato.setEnabled(False)
            self.tWContratos.setEnabled(False)
            #Establezco el valor de Editando Fila a True
            #y capturo el valor de la fila seleccionada y lo establezco en la variable
            #que me guarda el numero de fila.
            self.editandoFila=True  
            
    def pBEliminarContrato_clicked(self):
        respuesta = msg.question(self, "RSCTEL Agent", "¿Seguro que deseas elminiar el contrato seleccionado?", msg.Yes | msg.No)
        if respuesta==msg.Yes:
            self.tWContratos.removeRow(self.tWContratos.currentRow())
            
    def tWContratos_ItemSelectionChanged(self):
        # Obtenemos la fila actual seleccionada
        row = self.tWContratos.currentRow()
        # Si se seleccionó alguna fila (currentRow() devuelve >= 0), habilitamos el botón.
        if row >= 0:
            self.pBEditarContrato.setEnabled(True)
            self.pBEliminarContrato.setEnabled(True)
        else:
            self.pBEditarContrato.setEnabled(False)
            self.pBEliminarContrato.setEnabled(False)

    def cmbCatalogos_currentTextChanged(self, texto):
        for catalogo in self.tarifas["Catalogos"]:
            if catalogo['nombre'] == texto:
                self.tipos_de_contrato = catalogo['tipos_de_contrato']
        
        self.cmbTiposContratos.clear()
        self.cmbTiposContratos.addItems([tipo['nombre'] for tipo in self.tipos_de_contrato])
        self.cmbContratos.clear()
        self.cmbTiposContratos.setCurrentIndex(1)
        self.cmbTiposContratos.setCurrentIndex(0)

    def cmbTiposContratos_currentTextChanged(self, texto):
        # Primero debes saber que catalogo se ha seleccionado para poder obtener los tipos de contrato
        catalogo_seleccionado = self.cmbCatalogos.currentText()
        for catalogo in self.tarifas["Catalogos"]:
            if catalogo['nombre'] == catalogo_seleccionado:
                for tipo in catalogo['tipos_de_contrato']:
                    if tipo['nombre'] == texto:
                        self.contratos = tipo['contratos']

        self.cmbContratos.clear()
        self.cmbContratos.addItems([contrato['nombre'] for contrato in self.contratos])
        self.cmbContratos.setCurrentIndex(1)
        self.cmbContratos.setCurrentIndex(0)
      
    def lENumeroIBAN_textChanged(self,texto):
        codigo="ES"+texto[5:9]
        # Obtener el nombre del banco si la clave existe, sino mostrar un mensaje
        nombre_banco = self.bancos.get(codigo, {}).get("NOMBRE", "Banco no encontrado")
        # Establecer el nombre en el QLineEdit
        control=self.sender()
        if control.objectName()==self.lENumeroIBAN.objectName():
            self.lEEntidad.setText(nombre_banco)
        else:
            self.lEEntidadSuministro.setText(nombre_banco)

    #Intentare definir una funcion para escuchar las teclas desde este formulario.
    '''
    def keyPressEvent(self, event: QKeyEvent):
        if self.lEDNI!="":
            special_keys = [
                Qt.Key_F1, Qt.Key_F2, Qt.Key_F3, Qt.Key_F4, Qt.Key_F5,
                Qt.Key_F6, Qt.Key_F7, Qt.Key_F8, Qt.Key_F9, Qt.Key_F10,
                Qt.Key_F12, Qt.Key_Escape
            ]
            # Obtener información de la tecla presionada
            key_code = event.key()

            # Convertir el código de la tecla en su nombre textual (por ejemplo, F1, Escape, etc.)
            key_name = QKeySequence(key_code).toString()

            
            # Obtener información de la tecla presionada
            key_code = event.key()
            # Verificar si la tecla es especial
            if key_name=="F11": #in special_keys:
                #Si pasamos las validaciones de los controles, entonces escribimos el archivo
                if self.pBEnviarVentaACRM_clicked()==True:
                    
                    # Si el archivo existe, eliminarlo
                    if os.path.exists( "keys_pressed.txt"):
                        os.remove("keys_pressed.txt")
                    # Escribir en el archivo de texto si la tecla es especial
                    with open( "keys_pressed.txt", "a", encoding="utf-8") as file:
                        file.write(f"{key_name}")
            elif key_code in special_keys:
                # Si el archivo existe, eliminarlo
                if os.path.exists("keys_pressed.txt"):
                    os.remove("keys_pressed.txt")
                # Escribir en el archivo de texto si la tecla es especial
                with open("keys_pressed.txt", "a", encoding="utf-8") as file:
                    file.write(f"{key_name}")
'''

# Función para cerrar el proceso al salir
'''
def cerrar_procesos():
    if windowMonitor.poll() is None:  # Si el proceso sigue corriendo
        os.kill(windowMonitor.pid, signal.SIGTERM)  # Enviar señal de terminación
    if hotkeyMonitor.poll() is None:  # Si el proceso sigue corriendo
        os.kill(hotkeyMonitor.pid, signal.SIGTERM)  # Enviar señal de terminación
# Registrar la función para que se ejecute al salir de Python       
'''

if __name__ == "__main__":
    app = QApplication([])
    window = rsctelAgent()
    
    # Ejecuta el EXE y almacena el proceso
    #cargamos los archivos json
    path = os.path.join(os.path.expanduser("~"), "Documents", "RSCTEL")
        
    os.makedirs(path, exist_ok=True)  # Crea la carpeta si no existe
    rsctelAgent.script_dir = path
    #Ficha Activa
    #Provincias
    archivoJson=open("provincias.json","r",-1,"utf-8-sig")
    rsctelAgent.provincias=json.load(archivoJson)
    #Tarifas
    archivoJson=open("tarifas.json","r",-1,"utf-8-sig")
    rsctelAgent.tarifas=json.load(archivoJson)
    
    #BANCOS
    archivoJson=open("bancos.json","r",-1,"utf-8-sig")
    rsctelAgent.bancos=json.load(archivoJson)
    
    #windowMonitor = subprocess.Popen("windowMonitor.exe") 
    #hotkeyMonitor = subprocess.Popen("hotkeysMonitor.exe")
    window.showMaximized()
    #atexit.register(cerrar_procesos)
    app.exec()  
   
    
