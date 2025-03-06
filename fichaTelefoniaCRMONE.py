import CRMONE_V2
from tkinter import messagebox as msg


if msg.askyesno("RSCTEL Agent","Deseas probar el codigo?")==True:
    print("Dijo que si")
    #Navegamos hasta la pagina de Login de CRM
    navegador=CRMONE_V2.Navegador('https://rsctel.wikitic.es/index.php/pedido/n/8414')
    navegador.navegar()
    crmLogin=CRMONE_V2.LoginCRM(navegador.driver)
    crmLogin.usuario_edit("JOSE.AGUILAR","name","inp_usuario")
    crmLogin.contraseña_edit("Hashem11","name","inp_pass")
    crmLogin.ingresar_button("css selector",'button[type="submit"]')
    crmLogin.loguearse()
    
    #FICHA DE OFERTA BASICA PAGINA PRINCIPAL
    crmFichaTelefonia=CRMONE_V2.fichaTelefonia(navegador.driver)
    crmFichaTelefonia.tipoCliente_Select("xpath","//select[@id='select_basic_tipo_empresa']","AUTÓNOMO")
    crmFichaTelefonia.escenario_Select("xpath","//select[@id='select_basic_escenario']","Cliente Existente")
    crmFichaTelefonia.campos_Extras_Provincia_select2("xpath","//span[@id='select2-select_basic_zonas-container']")
    crmFichaTelefonia.campos_Extras_Opcion_Provincia("xpath","//input[@class='select2-search__field']","Burgos")
    crmFichaTelefonia.campos_Extras_Operador_select2("xpath","//span[@id='select2-select_basic_operador-container']")
    crmFichaTelefonia.campos_Extras_Opcion_Operador("xpath","//input[@class='select2-search__field']","MOVISTAR")
    crmFichaTelefonia.div_Ir_A_Oferta_Basica("xpath","//div[@class='bloque-oferta-rapida']//div[@class='boton-toggle-oferta']//div[1]")
    crmFichaTelefonia.div_Oferta_Fijo("xpath","//div[@class='texto'][normalize-space()='Fijo']")
    crmFichaTelefonia.div_Oferta_Movil("xpath","//div[@class='texto'][normalize-space()='Móvil']")
    crmFichaTelefonia.div_Oferta_Centralita("xpath","//div[@class='texto'][normalize-space()='Centralita']")
    crmFichaTelefonia.div_Oferta_Otros("xpath","//div[@class='texto'][normalize-space()='Otros']")
    crmFichaTelefonia.div_Oferta_Lineas_Adicionales("xpath","//div[@class='texto'][normalize-space()='Líneas adicionales']")
    crmFichaTelefonia.div_Oferta_Lineas_Extra("xpath","//div[@class='texto'][normalize-space()='Líneas Extra']")
    crmFichaTelefonia.div_Oferta_Television("xpath","//div[@class='texto'][normalize-space()='Televisión']")
    crmFichaTelefonia.div_Oferta_SVA("xpath","//div[@class='texto'][normalize-space()='SVA']")
    crmFichaTelefonia.button_Detalle_De_Productos("xpath","//button[@id='bt_detalle_productos']")
    #crmFichaTelefonia.llenar_Vista_Oferta_Basica()
    
    #FICHA DE OFERTA BASICA FIJO
    #crmFichaTelefonia.tab_Fijo("xpath","//li[@class='tab-fijo']//a")
    crmFichaTelefonia.opt_Tipo_Linea_Fijo("xpath","//input[@name='radio_fijo-porta' and @value='0']/ancestor::div[contains(@class, 'iradio_flat-blue')]")
    crmFichaTelefonia.oferta_Basica_Fijo_Internet_select2("xpath","//span[@id='select2-pp_internet-container']")
    crmFichaTelefonia.oferta_Basica_Fijo_Internet_Opcion("xpath","//input[@class='select2-search__field']","Fibra 1GB")
    crmFichaTelefonia.llenar_Oferta_Basica_Fijo()
    
    #FICHA DE OFERTA BASICA MOVIL
    crmFichaTelefonia.tab_Movil("xpath","//li[@class='tab-movil']")
    crmFichaTelefonia.opt_Tipo_Linea_Movil("xpath","//input[@name='radio_movil-porta' and @value='1']/ancestor::div[contains(@class, 'iradio_flat-blue')]")
    crmFichaTelefonia.oferta_Basica_Movil_Producto_select2("xpath","//span[@id='select2-pp_linea_principal-container']")
    crmFichaTelefonia.oferta_Basica_Movil_Producto_Opcion("xpath","//input[@class='select2-search__field']","Móvil 20Gb y Llamadas Ilimitadas (sólo móvil)")
    crmFichaTelefonia.llenar_Oferta_Basica_Movil()
    
    #FICHA DE OFERTA LÍNEAS ADICIONALES
    #Fecha: 20/02
    #Comenzaba a clonar lo de la ficha de arriba pero lo hare estandar para las tres pestañas que son iguales excepto la primera 
    #que no lleva el boton de agregar como en la adicional y extras.
    #Primero comenzamos por la Lineas Adicionales
    crmFichaTelefonia.tab_Lineas_Adicionales_Extras("xpath","//li[@class='tab-movil_secundario']//a")
    crmFichaTelefonia.button_Agregar_Lineas_Adicionales_Extras("xpath","//button[@id='bt_ver_movil_secundario']")
    crmFichaTelefonia.opt_Tipo_Lineas_Adicionales_Extras("xpath","//input[@name='radio_movil_secundario-porta' and @value='1']/ancestor::div[contains(@class, 'iradio_flat-blue')]")
   
    #Error a partir de aqui, no encuentra  los objetos
    crmFichaTelefonia.oferta_Basica_Lineas_Adicionales_Extras_Producto_select2("xpath","//span[@id='select2-pp_linea_principal-container']")
    crmFichaTelefonia.oferta_Basica_Lineas_Adicionales_Extras_Producto_Opcion("xpath","//input[@class='select2-search__field']","Móvil 70Gb y Llamadas Ilimitadas (sólo móvil)")
    crmFichaTelefonia.llenar_Oferta_Basica_Lineas_Adicionales_Extras()