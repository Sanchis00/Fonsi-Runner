'''Programa que simula un editor de texto como VSCode, con opciones para abrir 
y guardar archivos igual que el real'''

import tkinter as tk
from tkinter import messagebox,filedialog



class EditorDeTexto:
    def __init__(self,ventana):

        # Creamos la interfaz gráfica
        self.ventana = ventana
        ventana.title("Editor de texto")
        # Añadimos las opciones necesarias
        # para que se redimensionen los widgets
        # al maximizar la ventana
        ventana.columnconfigure(0,weight=1)
        ventana.columnconfigure(1,weight=1)
        ventana.columnconfigure(2,weight=1)

        ventana.rowconfigure(0,weight=1)
        ventana.rowconfigure(1,weight=1)
        ventana.rowconfigure(2,weight=1)
        ventana.rowconfigure(3,weight=20)



        # Modulo donde se crearán los widgets

        self.crear_widgets()
    
    def crear_widgets(self):
       
        # Etiqueta que te da la bienvenida
        self.etiqueta_bienvenida = tk.Label(ventana, text="Bienvenido a Fonsicode",bg='lightblue')
        self.etiqueta_bienvenida.grid(row=0,column=0,sticky="nswe",columnspan=30)

        # Barra de opciones superior
        #boton abrir archivo
        self.boton_abrir = tk.Button(ventana,text="Abrir archivo",bg='gray',command= self.abrir_archivo)
        self.boton_abrir.grid(row=1,column=0,sticky='nswe')

        #boton guardar archivo
        self.boton_guardar = tk.Button(ventana,text="Guardar archivo",bg="gray",command = self.guardar_archivo)
        self.boton_guardar.grid(row=1,column=1,sticky='nswe')

        #boton cerrar programa
        self.boton_cerrar = tk.Button(ventana,text="Cerrar app",bg="gray",command=lambda: ventana.quit())   
        self.boton_cerrar.grid(row=1,column=2,sticky='nswe')     

        # Barra de opciones inferior
        #boton para subrayar texto
       
        def underline_text():
            try:
                start_index = self.caja_texto.index(tk.SEL_FIRST)
                end_index = self.caja_texto.index(tk.SEL_LAST)

                if start_index and end_index:
                    tags = self.caja_texto.tag_names(start_index)
                    if "underline" in tags:
                        self.caja_texto.tag_remove("underline",start_index,end_index)
                    else:
                        self.caja_texto.tag_add("underline",start_index,end_index)
                        self.caja_texto.tag_config("underline",underline=True)
            except:
                tk.messagebox.showerror(title="Error",message = "No hay texto seleccionado")
        
        self.boton_subrayar = tk.Button(ventana,text='S',width=2,bg="gray",command = underline_text)
        self.boton_subrayar.grid(row=2,column=0)

        #boton para poner en negrita

        def bold_text():
            try:
                start_index = self.caja_texto.index(tk.SEL_FIRST)
                end_index = self.caja_texto.index(tk.SEL_LAST)

                if start_index and end_index:
                    tags = self.caja_texto.tag_names(start_index)
                    if "bold" in tags:
                        self.caja_texto.tag_remove("bold",start_index,end_index)
                    else:
                        self.caja_texto.tag_add("bold",start_index,end_index)
                        self.caja_texto.tag_config("bold",font=("bold"))
            except:
                tk.messagebox.showerror(title="Error",message="No se ha encontrado texto seleccionado")

        self.boton_negrita = tk.Button(ventana,text='B',width=2,bg="gray",command=bold_text)
        self.boton_negrita.grid(row = 2,column = 1)


        #boton para poner en cursiva

        def italics_text():
            try:
                start_index = self.caja_texto.index(tk.SEL_FIRST)
                end_index = self.caja_texto.index(tk.SEL_LAST)

                if start_index and end_index:
                    tags = self.caja_texto.tag_names(start_index)
                    if "italic" in tags:
                        self.caja_texto.tag_remove("italic",start_index,end_index)
                    else:
                        self.caja_texto.tag_add("italic",start_index,end_index)
                        self.caja_texto.tag_config("italic",font=("Helvetica",12,"italic"))
            except:
                tk.messagebox.showerror(title="Error",message="No se ha encontrado texto seleccionado")

        self.boton_cursiva = tk.Button(ventana,text='k',width=2,bg="gray",command=italics_text)
        self.boton_cursiva.grid(row = 2,column = 2)
    
        # Caja de texto que simulará el input de código

        self.caja_texto = tk.Text(ventana,bg='white',font=('Helvetica',12),selectbackground='black',wrap=tk.WORD)
        self.caja_texto.grid(row=3,columnspan=3,sticky='nswe')

        



        # Funcion para abrir archivo
    def abrir_archivo(self):

        file_path = filedialog.askopenfilename(filetypes=[("Archivos de Texto","*.txt"),("Todos los archivos","*.txt")])
        if file_path:
            try:
                with open(file_path,"r")as f:
                        texto = f.read()
                        self.caja_texto.delete("1.0",tk.END)
                        self.caja_texto.insert(tk.END,texto)
            except:
                messagebox.showerror("No se pudo abrir el archivo")


    def guardar_archivo(self):
        file_save = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Archivos de texto","*.txt"),
                                                            ("Todos los archivos","*.*")])
        if file_save:
            with open(file_save,'w')as f:
                texto = self.caja_texto.get("1.0",tk.END)
                f.write(texto)
        
                

           
            










ventana = tk.Tk()
mi_app = EditorDeTexto(ventana)
ventana.mainloop()