from tkinter import *
from tkinter import messagebox
from requests import *

############ WEB SCRAPING ############

url = get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL')
url_format = url.json()

dolar_hj = url_format['USDBRL']['bid']
dolar_hj = float(dolar_hj)
dolar_hj = round(dolar_hj,2)

euro_hj = url_format['EURBRL']['bid']
euro_hj = float(euro_hj)
euro_hj = round(euro_hj,2)

############ INTERFACE GRAFICA (GUI) ###########

janela_principal = Tk()
janela_principal.title('Conversor de Moedas')
janela_principal.geometry('310x430+400+200')
janela_principal.resizable(False, False)
janela_principal.config(background='#eeb90c')

############ FUNCOES ###########

def converter():
    try:
        if text_real.get() == '' and text_euro.get() == '':
            dolar = float(text_dolar.get())
            
            real = dolar * dolar_hj
            text_real.insert(0,round(real,3))

            euro = real / euro_hj
            text_euro.insert(0,round(euro,3))

        elif text_dolar.get() == '' and text_euro.get() == '':
            real = float(text_real.get())
           
            dolar = real / dolar_hj
            text_dolar.insert(0,round(dolar,3))

            euro = real / euro_hj
            text_euro.insert(0,round(euro,3))

        elif text_real.get() == '' and text_dolar.get() == '':
            euro = float(text_euro.get())

            real = euro * euro_hj
            text_real.insert(0,round(real,3))

            dolar = real / dolar_hj
            text_dolar.insert(0,round(dolar,3))

    except ValueError:
        messagebox.showerror('Atenção', 'Por favor, coloque um valor numérico!')


def limpar():
    text_dolar.delete(0,END)
    text_real.delete(0,END)
    text_euro.delete(0,END)

############ COMPONENTES (WIDGETS) ###########

logo = PhotoImage(file='/home/pazzi/python_tk/Conversor_moedas/moeda.png')
logo = logo.subsample(4,4)
figura1 = Label(image=logo, bg='#eeb90c')

lixeira = PhotoImage(file='/home/pazzi/python_tk/Conversor_moedas/lixeira.png')
lixeira = lixeira.subsample(33,33)
figura2 = Label(image=lixeira, bg='#eeb90c')

frame_dolar = Frame(janela_principal, borderwidth=1.5, relief='solid', bg='#eeb90c')
label_dolar = Label(janela_principal, text='Dolar', bg = '#eeb90c')
text_dolar = Entry(frame_dolar, width=34)

frame_real = Frame(janela_principal, borderwidth=1.5, relief='solid', bg = '#eeb90c')
label_real = Label(janela_principal, text='Real', bg = '#eeb90c')
text_real = Entry(frame_real, width=34)

frame_euro = Frame(janela_principal, borderwidth=1.5, relief='solid', bg = '#eeb90c')
label_euro = Label(janela_principal, text='Euro', bg = '#eeb90c')
text_euro = Entry(frame_euro, width=34)

botao_converter = Button(janela_principal, text='Converta', font=('Georgia', 15),
                    highlightthickness=0, bd = 0, bg = '#eeb90c', command=converter)

botao_limpar = Button(janela_principal, image=lixeira,
                        highlightthickness=0, bd = 0, bg = '#eeb90c', command=limpar)                    

############ LAYOUT - POSICIONAMENTO ###########
figura1.place(x=86, y=15)

frame_dolar.place(x=5, y=165, width=295, height=48)
label_dolar.place(x=8, y=155)
text_dolar.place(x=5, y=15)

frame_real.place(x=5, y=235, width=295, height=48)
label_real.place(x=8, y=225)
text_real.place(x=5, y=15)

frame_euro.place(x=5, y=306, width=295, height=48)
label_euro.place(x=8, y=296)
text_euro.place(x=5, y=15)

botao_converter.place(x=85, y=370)
botao_limpar.place(x=270, y=365)



janela_principal.mainloop()