import flet as ft
import tkinter as tk
import pyodbc
import bcrypt
from menu import get_menu_view
# ---------------------------------
# OBTENER LA RESOLUCION DE PANTALLA 
# ---------------------------------
root = tk.Tk()
ancho = root.winfo_screenwidth()
alto = root.winfo_screenheight()

# ------------------------
# CONEXIÓN A SQL SERVER
# ------------------------
def conectar_sql_server():
    return pyodbc.connect(
      'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=INGJORGELOPEZ\\SQLEXPRESS;'
        'DATABASE=FLET;'
        'UID=sa;'
        'PWD=1234'
    )

# ------------------------
# REGISTRAR USUARIO SQL
# ------------------------
def registrar_usuario(username, password):
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    try:
        print(f"Registrando usuario: {username}, hash: {password_hash[:10]}...")
        conn = conectar_sql_server()
        cursor = conn.cursor()

        cursor.execute("EXEC sp_registrar_usuario ?, ?", username, password_hash)
        resultado = cursor.fetchone()

        conn.commit()  # <- Puede ser necesario aquí explícitamente

        return resultado and resultado[0] == 1
    except Exception as e:
        print("Error en registro:", e)
        return False
    finally:
        conn.close()

# ------------------------
# VALIDAR USUARIO SQL
# ------------------------
def validar_usuario(username, password):
    try:
        conn = conectar_sql_server()
        cursor = conn.cursor()
        cursor.execute("EXEC sp_obtener_hash ?", username)
        row = cursor.fetchone()
        if row:
            stored_hash = row[0]
            return bcrypt.checkpw(password.encode(), stored_hash.encode())
        return False
    except:
        return False
    finally:
        conn.close()

# ------------------------
# INERFAZ FLET
# ------------------------
def main(page: ft.Page):
    def ajustar_pantalla_inicial():  
        page.window.width = int(ancho*0.25)  
        page.window.height = int(alto*0.35)  
        page.window.resizable = False 
        page.window.maximizable = False
        page.window.center()
        page.update()

    # ------------------------
    # FUNCIONES
    # ------------------------
    
    def ajustar_pantalla_home():
        page.window.width = int(ancho*0.90)
        page.window.height = int(alto*0.90)
        page.window.center()
        page.update()

    def handle_password_icon_click(e):
        if clave.password:
            clave.password = False
            clave.suffix = icono_password
            clave.update()
            
        else:
            clave.password = True
            clave.suffix = icono_password_off
            clave.update()
            
    def limpiar_campos():
            mensaje.value = ""
            usuario.value = ""
            clave.value = ""

    def login_click(e):
        if validar_usuario(usuario.value, clave.value):
            page.update()
            limpiar_campos()
            page.dialog = None
            page.clean()
            page.go("/home")
        else:
            mensaje.value = "❌ Error de Usuario o Contraseña "
            mensaje.color = ft.Colors.RED
            page.update()

    def registrar_click(e):
        if registrar_usuario(usuario.value, clave.value):
            mensaje.value = "✅ Usuario registrado"
            mensaje.color = ft.Colors.GREEN
        else:
            mensaje.value = "❌ Usuario ya existe o error"
            mensaje.color = ft.Colors.RED
        page.update()

    def alternar_modo(e):
        if modo.value == "login":
            modo.value = "registro"
            btn_login.text = "Registrar"
            btn_switch.text = "¿Ya tienes cuenta? Inicia sesión"
        else:
            modo.value = "login"
            btn_login.text = "Iniciar sesión"
            btn_switch.text = "¿No tienes cuenta? Regístrate"
        mensaje.value = ""
        page.update()
    
    def route_change(e):
        page.views.clear()
        if page.route == "/":
           ajustar_pantalla_inicial()   
           page.views.append(login_view())  
           page.update()
        elif page.route == "/home":
           ajustar_pantalla_home()
           view, cargar_menu = get_menu_view(page)
           page.views.append(view)
           page.update()
           cargar_menu()  # <-- Ahora que ya está en la página, puedes cargar el contenido
       

    # ------------------------
    # NAVEGACION DE VISTAS
    # ------------------------
    def login_view():
        return ft.View(
            "/",
            controls=[ 
               ft.Column([
                usuario,
                clave,
                btn_login,
                btn_switch,
                mensaje
                 ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
            ], bgcolor=ft.Colors.GREY_100, horizontal_alignment= ft.CrossAxisAlignment.CENTER, vertical_alignment = ft.MainAxisAlignment.CENTER 
        )
  
    
    def on_hover_btn_login(e): 
        if e.data == "true":
            btn_login.bgcolor = ft.Colors.BLUE_900  # Color al pasar el puntero
        else:
            btn_login.bgcolor = "black"   # Color normal
        btn_login.update()
    # ------------------------------------
    # ELEMENTOS PARA AGREGAR A LAS VISTAS
    # ------------------------------------
    label_text= ft.Text('Usuario',color=ft.Colors.BLACK,weight=ft.FontWeight.BOLD)
    label_text2= ft.Text('Contraseña',color=ft.Colors.BLACK,weight=ft.FontWeight.BOLD)
    icono_password = ft.IconButton(
            icon=ft.Icons.VISIBILITY,
            icon_color="black",  
            on_click=handle_password_icon_click
        )
    icono_password_off = ft.IconButton(
            icon=ft.Icons.VISIBILITY_OFF,
            icon_color="black",  
            on_click=handle_password_icon_click
        )
    usuario = ft.TextField(label=label_text, width=350,color=ft.Colors.BLACK,border_color=ft.Colors.BLACK,height=50,autofocus=True)
    clave = ft.TextField(label=label_text2, password=True, width=350,color=ft.Colors.BLACK,border_color=ft.Colors.BLACK,
                            suffix=icono_password_off,height=50
                            )
    mensaje = ft.Text()
    modo = ft.Text(value="login")  
    contenedor_boton = ft.Container(content=ft.Text(value="Ingresar", size=20))
    btn_login = ft.ElevatedButton(content=contenedor_boton,width=130,color=ft.Colors.WHITE,on_hover= on_hover_btn_login, on_click=lambda e: registrar_click(e) if modo.value == "registro" else login_click(e))
    btn_switch = ft.TextButton(text="¿No tienes cuenta? Regístrate",style=ft.ButtonStyle(
             color="black",          # Color del texto
             text_style=ft.TextStyle(
             weight=ft.FontWeight.BOLD  # Negrita
            ),
            overlay_color= ft.Colors.BLUE_500,
        ), on_click=alternar_modo)

    # ------------------------
    # ACTIVAR LA NAVEGACION
    # ------------------------
    page.on_route_change = route_change
    page.go(page.route)

# ------------------------
# INSERTAR LA INTERFAZ
# ------------------------
ft.app(target=main)
