#Requires AutoHotkey v2.0
#include Libs\UIA.ahk
#Include Libs\JSON.ahk
#SingleInstance Force
;#Include tools.ahk

global CodificarCon:=""
global tituloVentana:="Script -"
global VentanaScript := ""
global TituloScript:=""
global teclaPresionada:=""





CarpetaTemporal:=A_MyDocuments . "\RSCTEL\TEMP\"
CarpetaRaiz:=A_MyDocuments . "\RSCTEL\"
versionControl:=""

    ;MsgBox(GetProcessId("C:\Users\SOPORTE_RSCTEL\Desktop\AutoHotkey\RSCTEL\OCMAgent\OCMAgent.exe"))



    ; ========================
    ; Región Mostrar Mensaje Asicronico
    ; ========================
    ;Mensajes := Gui()
    ;mensajes.Title:="RSCTEL Bot"
    ;Mensajes.Opt("+AlwaysOnTop +Owner -MinimizeBox -SysMenu" )  ; +Owner avoids a taskbar button.
    ;Mensajes.Add("Text",, "El programa ha iniciado correctamente.")
    ;Mensajes.Show("NoActivate")  ; NoActivate avoids deactivating the currently active window.
    ; ========================
    ; Región Mostrar Mensaje Asicronico
    ; ========================

    MsgBox "El programa ha iniciado correctamente.","RSCTEL Bot","T2"


if ProcessExist("OCMAgent.exe"){
    Inicio:
    versionControl:=""
    ;Obtengo el nombre de la ventana si existe, de lo contrario no hago nada y regreso a INICIO
    FuncionesOCM("TituloScript")
    if InStr(TituloScript,"MASMOVIL",0,1,1)>0 or InStr(TituloScript,"Naturgy",0,1,1)>0 {
        ;Reinicio la variable
        teclaPresionada:=""

        ;Capturo las teclas presionadas por el usuario

        ;teclaPresionada := InputHook("L1 B","{Escape}{F1}{F2}{F3}{F4}{F5}{F6}{F7}{F8}{F9}{F10}{F11}{F12}")
        ;teclaPresionada.Start
        ;teclaPresionada.Wait

        ;ventaEnergia()
        ; Bucle que espera una tecla específica
        
            Loop {
                ; Captura Escape
                if GetKeyState("Escape", "P") {
                    TeclaPresionada := "Escape"
                    break
                }
            
                ; Captura teclas F1-F12
                Loop 12 {
                    tecla := "F" . A_Index
                    if GetKeyState(tecla, "P") {
                        TeclaPresionada := tecla
                        break 2
                    }
                }
            
                Sleep 10 ; Pequeña pausa para evitar consumir demasiados recursos
            }
        

        ;Bloquea Escape
        Esc::return
        ; Bloquea F1-F12
        F1::return
        F2::return
        F3::return
        F4::return
        F5::return
        F6::return
        F7::return
        F8::return
        F9::return
        F10::return
        F11::return
        F12::return
    }
    


    ;Verifico si el OCM esta abierto
    if ProcessExist("OCMAgent.exe"){
        
        try {
                if ControlGetEnabled("WindowsForms10.Window.8.app.0.141b42a_r7_ad19", "Agent") = true{
                    versionControl:="r7"
                }
        } catch Error as e {

            try {
                if ControlGetEnabled("WindowsForms10.Window.8.app.0.141b42a_r8_ad19", "Agent") = true{
                    versionControl:="r8"
                }
            } catch Error as e {
                versionControl:=""
            }
            
        }

        

        ;Asigno el control del boton Descolgar o Rellamar
        ;Verifico el estado del boton Descolgar
        ;Si descolgar esta habilitado entonces estamos en ACW o que implica que la ventana de Script esta abierta
        
        if versionControl="r7" or versionControl="r8"{
             if InStr(teclaPresionada,"F",0,1,1) > 0 {
                
                    ;Declaro la etiqueta para poder volver a este punto
                    ObtenerFichaOCM:
                    ;Obtengo el nombre de la ventana si existe, de lo contrario no hago nada y regreso a INICIO
                    FuncionesOCM("TituloScript")
                    ;Si se obtiene un nombre de ventana valido, entonces ejecuto las funciones dependiendo el script
                    
                    if InStr(TituloScript,"Naturgy",0,1,1)>0 {
                        ;Si la ficha es Energia, comienzo por asignar el valor a la variable Ficha activa que es la que me ayuda
                        ;identificar a que programa o campaña pertenece el usuario
                        FichaActiva:="Energia" 
                        ;Bloqueo las entradas del usuario para evitar errores indeseados
                        BlockInput("On")
                        ;Llamo a la funcion CampañaEnergia, para que segun la tecla presionada me devuelva
                        ;o me ejecute las tareas a realizar segun la programacion de cada tecla
                        CampañaEnergia(teclaPresionada)
                        ;Verifico que si es una llamada agendada o no
                        ;ya que si es agendada no guardare automaticamente
                        ;sino que pondre el foco en el datetimePicker
                        if teclaPresionada="F5" or teclaPresionada="F6" or teclaPresionada="F9"{
                            ;Estas teclas estan asignadas a llamadas agendadas
                            ;procedo a codificar la llamada agendada
                            FuncionesOCM("Codificar_Llamada_Agendada")
                        }else if teclaPresionada="F11"{

                            ;una vez obtenga la codificación del sistema OCM segun la ficha actual
                            ;procedo a codificar la llamada
                           
                            ventaEnergia()
                            FuncionesOCM("Codificar_Llamada")
                        }else{
                            FuncionesOCM("Codificar_Llamada")
                        }
                        ;una vez se ha codificado y guardado la ficha del cliente, procedo a desbloquear
                        ; las entradas del usuario
                        BlockInput ("Off")
                        
                    }else if InStr(TituloScript,"MASMOVIL",,1,1){
                        ;Si la ficha activa es Telefonia, o el programa de telefonia que tenemos ahora mismo en 2025
                        ;entonces sus codificaciones para las fichas son ligeramente diferentes a las de energia
                        FichaActiva:="Telefonia"
                        ;Bloqueo las entradas del usuario para evitar errores indeseados
                        BlockInput("On")
                        ;Llamo a la funcion CampañaEnergia, para que segun la tecla presionada me devuelva
                        ;o me ejecute las tareas a realizar segun la programacion de cada tecla
                        CampañaTelefonia(teclaPresionada)

                        ;Verifico que si es una llamada agendada o no
                        ;ya que si es agendada no guardare automaticamente
                        ;sino que pondre el foco en el datetimePicker
                        if teclaPresionada="F4" or teclaPresionada="F5" or teclaPresionada="F9"{
                            ;Estas teclas estan asignadas a llamadas agendadas
                            ;procedo a codificar la llamada agendada
                            FuncionesOCM("Codificar_Llamada_Agendada")
                        }else if teclaPresionada="F11"{
                            ;Esta es una tecla especial porque aqui interactuo con el CRM de la empresa
                            ;por eso lo programo por separado
                        }else{
                            ;una vez obtenga la codificación del sistema OCM segun la ficha actual
                            ;procedo a codificar la llamada
                            FuncionesOCM("Codificar_Llamada")
                        }

                        ;una vez obtenga la codificación del sistema OCM segun la ficha actual
                        ;procedo a codificar la llamada
                        ;una vez se ha codificado y guardado la ficha del cliente, procedo a desbloquear
                        ; las entradas del usuario
                        BlockInput ("Off")
                    }
            /*Al parecer el script es muy rapido o algo pasa
            que sino espero a que la ventana script este 
            inactiva, el script se repite inmediatamente lo que genera un error, en el cual
            no encuentra los controles (repite la codificacion aun cuando esta codificando actualmente)
            esta ultima linea "WinWaitNotActive(tituloVentana)" hace que no suceda ese error*/ 
            WinWaitNotActive(tituloVentana)       
            }
            
        }else if teclaPresionada="Escape" {
            ;Para cualquier programa, siempre la tecla Escape se asignara para 
            ;colgar la llamada
            FuncionesOCM.call("Colgar_Llamada")
        }
    }else{
        

        if MsgBox("OCMAgent no se encuentra abierto.`n¿Deseas cerrar RSCTEL Bot?", "RSCTEL Bot", "YesNo")="Yes" {
            ExitApp  ; Salir de la aplicación de AHK
            }
        }
    goto Inicio
}



/******************************************************
*******************************************************
***************** FUNCIONES DEL PROGRAMA **************
*******************************************************
*******************************************************/

FuncionesOCM(Operacion){
    global VentanaScript
    global TituloScript
    global CodificarCon
    global tituloVentana
    try {
        if Operacion="Codificar_Llamada"{
            ;Envio una tecla de Escape porque he detectado que
            ;al tener el menu de windows abierto, no me deja posicionar
            ;la ventana al frente
            Send("{Escape}")
            ;Muevo la ventana del Script de OCM al frente
            WinMoveTop(tituloVentana)
            ;Espero que la ventana este activa
            WinWait(tituloVentana)
            ;Doy clic en el boton de actualizar informacion en la ficha.
            VentanaScript.FindElement({Type:"Button", Name:"Actualizar Información"}).ControlClick("left",1)
            ;Doy clic en el boton de Codificar, que esta con el automationID en "botonCodificar"
            ;esto en la version 2.1.44.10 del OCM
            VentanaScript.FindElement({AutomationId:"botonCodificar"}).ControlClick("left",1)
            ;Doy clic en el Item a Codificar, que es de Tipo: TreeItem, y tiene por nombre lo que se
            ;se desea codificar segun el programa activo
            ;esto en la version 2.1.44.10 del OCM
            VentanaScript.FindElement({Type:"TreeItem", Name:CodificarCon}).Click("left",2)
            ;Doy clic en el boton de Guardar y Cerrar, que esta con el automationID en "botonGuardar"
            ;esto en la version 2.1.44.10 del OCM
            VentanaScript.FindElement({AutomationId:"botonGuardar"}).ControlClick("left",1)
        }else if Operacion="Codificar_Llamada_Agendada" {

            ;Envio una tecla de Escape porque he detectado que
            ;al tener el menu de windows abierto, no me deja posicionar
            ;la ventana al frente
            Send("{Escape}")
            ;Muevo la ventana del Script de OCM al frente
            WinMoveTop(tituloVentana)
            ;Espero que la ventana este activa
            WinWait(tituloVentana)
            ;Doy clic en el boton de actualizar informacion en la ficha.
            VentanaScript.FindElement({Type:"Button", Name:"Actualizar Información"}).ControlClick("left",1)
            ;Doy clic en el boton de Codificar, que esta con el automationID en "botonCodificar"
            ;esto en la version 2.1.44.10 del OCM
            VentanaScript.FindElement({AutomationId:"botonCodificar"}).ControlClick("left",1)
            /*Doy clic en el Item a Codificar, que es de Tipo: TreeItem, y tiene por nombre lo que se
            se desea codificar segun el programa activo
            esto en la version 2.1.44.10 del OCM*/
            VentanaScript.FindElement({Type:"TreeItem", Name:CodificarCon}).Click("left",2)
            ;Doy clic en el boton de Guardar y Cerrar, que esta con el automationID en "botonGuardar"
            ;esto en la version 2.1.44.10 del OCM
            VentanaScript.FindElement({AutomationId:"dateTimePicker1"}).ControlClick("left",1)
            
        }else if Operacion="Colgar_Llamada" {
            ;Clic en el boton colgar
            try {
                ControlClick("WindowsForms10.Window.8.app.0.141b42a_r7_ad111", "Agent",,"LEFT",1)
            } catch Error as e {
                ControlClick("WindowsForms10.Window.8.app.0.141b42a_r8_ad111", "Agent",,"LEFT",1)
            }
                
            
        }else if Operacion="TituloScript" {
            ;Si existe una ventana con el texto "Script -" que es lo unico que no cambia de la
            ;ventana del script de OCM
            if WinExist(tituloVentana){
                WinActivate(tituloVentana)
                WinMoveTop(tituloVentana)
                WinWait(tituloVentana)
                ;Asigno la ventana a un objeto UIElement
                VentanaScript:=UIA.ElementFromHandle("Script -")
                ;Asigno el nombre de la variable NombreScript
                TituloScript:= VentanaScript.FindElement({ClassName:"Chrome_WidgetWin_1",LocalizedType:"panel"}).name 
                    
            }else{
                ;Si la ventana no existe, devuelvo la variable NombreScript vacia
                TituloScript:=""
            }
        }

    }catch as e{
        ;Lo primero es liberar el bloqueo del input
        BlockInput "Off"
        /*Si por alguna razon no se logra codificar la ficha, en lugar de un error inesperado
        muestro un mensaje y reintento*/
        

        if MsgBox("Ha ocurrido un error al intentar codificar la ficha, ¿Deseas volver a intentar codificar?. `r" . e.Message . " `r " . e.Line, "RSCTEL Bot", "YesNo")="No" {
            ExitApp  ; Finaliza la ejecución del script
        }
    }
}


CampañaEnergia(tecla){
    global CodificarCon

    if tecla="F1"{
        CodificarCon:="CON CONTACTADO"
    }else if tecla="F2"{
        CodificarCon:="NO INTERESADO"
    }else if tecla="F3"{
        CodificarCon:="BUZON DE VOZ"
    }else if tecla="F4"{
        CodificarCon:="BONO SOCIAL"
    }else if tecla="F5"{
        CodificarCon:="LLAMAR POR LA MAÑANA"
    }else if tecla="F6"{
        CodificarCon:="LLAMAR POR LA TARDE"
    }else if tecla="F7"{
        CodificarCon:="LLAMADA DESCONECTADA"
    }else if tecla="F8"{
        CodificarCon:="ERROR DATOS"
    }else if tecla="F9"{
        CodificarCon:="LLAMADA AGENDADA"
    }else if tecla="F10"{
        CodificarCon:="NO RESIDE EN PUNTO SUMINISTRO"
    }else if tecla="F11"{
        ;AQUI SE INTERACTUA CON CRM
        CodificarCon:="VENTA"
    }else if tecla="F12"{
        CodificarCon:="YA CLIENTE NATURGY"
    }
}

CampañaTelefonia(tecla){
    global CodificarCon

    if tecla="F1"{
        CodificarCon:="NO CONTACTADO"
    }else if tecla="F2"{
        CodificarCon:="NO INTERESA"
    }else if tecla="F3"{
        CodificarCon:="BUZON DE VOZ"
    }else if tecla="F4"{
        CodificarCon:="LLAMAR POR LA MAÑANA"
    }else if tecla="F5"{
        CodificarCon:="LLAMAR POR LA TARDE"
    }else if tecla="F6"{
        CodificarCon:="LLAMADA DESCONECTADA"
    }else if tecla="F7"{
        CodificarCon:="DIRECCION INCORRECTA"
    }else if tecla="F8"{
        CodificarCon:="NO CORRESPONDE NOMBRE TITULAR"
    }else if tecla="F9"{
        CodificarCon:="LLAMADA AGENDADA"
    }else if tecla="F10"{
        CodificarCon:="YA CLIENTE MASMOVIL"
    }else if tecla="F11"{
        CodificarCon:="VENTA"
        ;AQUI SE INTERACTUA CON CRM
    }else if tecla="F12"{
        CodificarCon:="COMPROMISO PERMANENCIA POR TERMINALES"
    }
}

;Funcion para copiar los datos de la ficha que se acaba de encontrar
ventaEnergia(){
    ; Definir la ruta del archivo JSON
    jsonPath := "fichas.json"

    ; Escribir la estructura completa en el archivo (JSON inicial)
    jsonInicial :=
    "
    (
    {
        "fichaEnergia": {
            "nombreCliente": "",
            "DNI_NIE": "",
            "email":"",
            "direccion": "",
            "provincia": "",
            "poblacion": "",
            "IBAN": "",
            "CUPS_LUZ": "",
            "CUPS_GAS": "",
            "codigoPostal": "",
            "contratoLuz": "",
            "contratoGas": "",
            "SVAE": "",
            "SVAG": "",
            "cuotaAcnur": ""
        },
        "timestamp": ""
    }
    )"
    
    fileJ := FileOpen(jsonPath, "w", "UTF-8")
    fileJ.Write(jsonInicial)
    fileJ.Close()

    ; Llevar la ventana de OCM al frente y esperar que esté activa
    ;WinMoveTop(titulo_Ventana_A_Monitorear)
    if WinExist(tituloVentana){
        ;WinWaitActive(titulo_Ventana_A_Monitorear)

        ; Leer y parsear el JSON desde el archivo
        archivoJson := FileRead(jsonPath)
        ficha := JSON.parse(archivoJson)


        ;Declaramos las variables que extraere de OCM y las asignamos al json
        ficha["fichaEnergia"]["nombreCliente"]:=VentanaScript.FindElement({Type: "Edit", AutomationId:"__NOMBRE_var"}).GetPropertyValue("Value")
        ficha["fichaEnergia"]["DNI_NIE"]:=VentanaScript.FindElement({Type: "Edit", AutomationId:"__DNI_NIE_var"}).GetPropertyValue("Value")
        ficha["fichaEnergia"]["email"]:=VentanaScript.FindElement({Type: "Edit", AutomationId:"__EMAIL_var"}).GetPropertyValue("Value")
        ficha["fichaEnergia"]["direccion"]:=VentanaScript.FindElement({Type: "Edit", AutomationId:"__DIRECCION_var"}).GetPropertyValue("Value")
        ficha["fichaEnergia"]["provincia"]:=VentanaScript.FindElement({Type: "Edit", AutomationId:"__PROVINCIA_var"}).GetPropertyValue("Value")
        ficha["fichaEnergia"]["poblacion"]:=VentanaScript.FindElement({Type: "Edit", AutomationId:"__POBLACION_var"}).GetPropertyValue("Value")
        ficha["fichaEnergia"]["IBAN"]:=VentanaScript.FindElement({Type: "Edit", AutomationId:"__IBAN_var"}).GetPropertyValue("Value")
        ficha["fichaEnergia"]["CUPS_LUZ"]:=VentanaScript.FindElement({Type: "Edit", AutomationId:"__CUPS_LUZ_var"}).GetPropertyValue("Value")
        ficha["fichaEnergia"]["CUPS_GAS"]:=VentanaScript.FindElement({Type: "Edit", AutomationId:"__CUPS_GAS_var"}).GetPropertyValue("Value")
        ;NUMERO_CLIENTE:=VentanaScript.FindElement({Type: "Edit", AutomationId:"__NOMBRE_var"}).GetPropertyValue("Value")
        ficha["fichaEnergia"]["codigoPostal"]:=VentanaScript.FindElement({Type: "Edit", AutomationId:"__CODIGO_POSTAL_var"}).GetPropertyValue("Value")
        ficha["fichaEnergia"]["contratoLuz"]:=VentanaScript.FindElement({Type:"ComboBox", AutomationId:"__other_4_var"}).GetPropertyValue("Value")
        ficha["fichaEnergia"]["contratoGas"]:=VentanaScript.FindElement({Type:"ComboBox", AutomationId:"__other_10_var"}).GetPropertyValue("Value")
        ficha["fichaEnergia"]["SVAE"]:=VentanaScript.FindElement({Type:"ComboBox", AutomationId:"__other_9_var"}).GetPropertyValue("Value")
        ficha["fichaEnergia"]["SVAG"]:=VentanaScript.FindElement({Type:"ComboBox", AutomationId:"__other_15_var"}).GetPropertyValue("Value")
        ficha["fichaEnergia"]["cuotaAcnur"]:=VentanaScript.FindElement({Type:"ComboBox", AutomationId:"__CUOTA_ACNUR_var"}).GetPropertyValue("Value")
        ficha["timestamp"] := A_Now

        ; Guardar el JSON actualizado en el archivo
        jsonFicha := JSON.stringify(ficha)
        fileJ := FileOpen(jsonPath, "w", "UTF-8")
        fileJ.Write(jsonFicha)
        fileJ.Close()

        ; Mover la ventana al fondo y esperar que se cierre (con timeout de 5 minutos)
        ;WinMoveBottom(titulo_Ventana_A_Monitorear)
        if WinExist("RSCTEL Agent"){
            WinWait("RSCTEL Agent")
            WinActivate("RSCTEL Agent")
        }else{
            Run("rsctel_main.exe")
            WinWait("RSCTEL Agent")
            WinActivate("RSCTEL Agent")
        }
        WinActivate(tituloVentana)

        
        
    }
    
}

