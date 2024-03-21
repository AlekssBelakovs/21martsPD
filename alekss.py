import PySimpleGUI as sg
 
 




saraksts=[['File',['Close']], ['Help'],['About']]
dalas = [
        [sg.Menu(saraksts)],
        [sg.Text("Ieraksti savu vārdu:"), sg.InputText(key='--vards--')],
        [sg.Text("Ieraksti savu uzvārdu:"), sg.InputText(key='--uzvards--')],
        [sg.Text("Izvēlies  datumu:")],
        [sg.Text("Diena:"),sg.Combo(['1', '2', '3', '4','5', '6', '7', '8','9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21','22', '23', '24', '25', '26', '27', '28', '29', '30', '31'], key='--diena--')],
        [sg.Text("Mēnesis:"),sg.Combo(['Janvāris', 'Februāris', 'Marts', 'Aprīlis', 'Maijs', 'Jūnijs', 'Jūlijs', 'Augusts', 'Septembris', 'Oktobris', 'Novembris', 'Decembris'], key='--menesis--')],
        [sg.Text("Gads:"),sg.Combo(['2000', '2002', '2003', '2004','2005', '2006', '2007', '2008','2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'], key='--gads--')],
        [sg.T("Atzīmē savus mīļākos mācību priekšmetus:")],
        [sg.T("                   "), sg.Checkbox('Matemātika', default=False,key="-mat-")],
        [sg.T("                   "), sg.Checkbox('Latviešu valoda', default=False,key="-lv-")],
        [sg.T("                   "), sg.Checkbox('Bioloģija', default=False,key="-Bio-")],
        [sg.T("                   "), sg.Checkbox('Mājturība', default=False,key="-maj-")],
        [sg.T("                   "), sg.Checkbox('Sports', default=False,key="-sp-")],
        [sg.T("                   "), sg.Checkbox('Vizuālā Māksla', default=False,key="-viz-")],
        [sg.T("                   "), sg.Checkbox('Dabaszinības', default=False,key="-daba-")],
 
        [sg.Button('OK')],
        [sg.Text('', key='--vieta--')]
     ]
 



logs = sg.Window("EGLE", dalas, size=(500,500))
 


while True:
    event, values = logs.read()
 


    if event == sg.WINDOW_CLOSED or event=='Close':
        break
 
    elif event=='About':
        sg.popup('Autors: Alekss Beļakovs')
    elif event=='OK':
        vards=values['--vards--']
        uzvards=values['--uzvards--']
        diena=values['--diena--']
        menesis=values['--menesis--'].lower()
        gads=values['--gads--']


        matematika = values['-mat-']
        latviesu_val = values['-lv-']
        Biologija=values['-Bio-']
        Majturiba=values['-maj-']
        Sports=values['-sp-']
        Vizuala_maksla=values['-viz-']
        Dabaszinibas=values['-daba-']
    


        prieksmeti=[] 
        if matematika:
            prieksmeti.append('Matemātika')
        if latviesu_val:
            prieksmeti.append('Latviešu valoda')
        if Biologija:
            prieksmeti.append('Biologija')
        if Majturiba:
            prieksmeti.append('Mājturība')
        if Sports:
            prieksmeti.append('Sports')
        if Vizuala_maksla:
            prieksmeti.append('Vizuālā māksla')
        if Dabaszinibas:
            prieksmeti.append('Dabaszinības')
      


        logs['--vieta--'].update(f'{vards} {uzvards} - datums:{diena}.{menesis} {gads}.gads\n'
        f'Iecienītie priekšmeti ir: {", ".join(prieksmeti)}.')
 
 
 
 
 
 
logs.close()