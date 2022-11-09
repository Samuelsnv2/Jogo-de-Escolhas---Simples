import PySimpleGUI as sg
import buttons as bt

p='i'
m=[]
# Inicio do jogo
def janela_inicial():
    sg.theme('DarkBrown2')
    layout=[
        [sg.Text('BOAS VINDAS À AVENTURA DA SUA VIDA!\n\nDigite seu nome:',font='Times 18')],
        [sg.Input(key='nome',font='Times 15')],
        [sg.Button('',image_data=bt.play,key='-Continue-',button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0)],
        [sg.Output(font='Times 12')]
    ]
    return sg.Window('Inicio',layout=layout,icon=bt.icone,finalize=True)
def mochila(nome):
    sg.theme('DarkAmber')
    layout=[
        [sg.Text(f'Olá {nome}!\nVocê deve tomar algumas decisões que te levarão para um final!\nAproveite o caminho.\n',font='Times 12')],
        [sg.Text('Sua primeira escolha será de pura sorte:\nEscolha uma mochila:',font='Times 13')],
        [sg.Radio('Mochila 1','mochila',font='Times 10',key='m1'),sg.Radio('Mochila 2','mochila',font='Times 10',key='m2'),sg.Radio('Mochila 3','mochila',font='Times 10',key='m3')],
        [sg.Button('Voltar',font='Times 11'),sg.Button('Continuar',font='Times 11')]
    ]
    return sg.Window('Mochila',layout=layout,icon=bt.bag,finalize=True)
def acomp(nome):
    sg.theme('Topanga')
    layout=[
        [sg.Text(f'{nome}, você está começando sua jornada, à sua frente temos 3 personagens.\n',font='Times 15')],
        [sg.Text('Você deve escolher um para te acompanhar durante sua aventura:',font='Times 13')],
        [sg.Radio('Arqueiro','personagem',font='Times 10',key='arq'),sg.Radio('Feiticeiro','personagem',font='Times 10',key='feit'),sg.Radio('Ninja','personagem',font='Times 10',key='ninja')],
        [sg.Button('Voltar',font='Times 11'),sg.Button('Continuar',font='Times 11')]
    ]
    return sg.Window('Companheiro',layout=layout,icon=bt.icone,finalize=True)
def caminho(nome,p):
    sg.theme('Reds')
    layout=[
        [sg.Text(f'Ok {nome}! O {p} irá te acompanhar durante a sua aventura',font='Times 15')],
        [sg.Text('Vocês encontraram uma bifurcação no caminho, decida para qual caminho irão seguir:',font='Times 13')],
        [sg.Button('',image_data=bt.sombrio,key='sombrio'),sg.Button('',image_data=bt.pantano,key='pantano',size=(100,100))],
        [sg.Button('Voltar',font='Times 11')]
    ]
    return sg.Window('Caminho',layout=layout,icon=bt.way,finalize=True)
def pantano(nome):
    sg.theme('DarkGreen')
    layout=[
        [sg.Text(f'CREDO {nome}!!\nEspero que você saiba sobreviver no meio de animais peçonhentos e seu parceiro também...\n',font='Times 15')],
        [sg.Text('Agora não tem mais volta...',font='Times 13')],
        [sg.Button('Continuar',font='Times 11')]
    ]
    return sg.Window('Pântano',layout=layout,icon=bt.icone,finalize=True)
def fim_pantano(nome):
    sg.theme('Black')
    layout=[
        [sg.Text(f'QUE MÁ SORTE...\nUM JACARÉ COMEU VOCÊ E SEU COMPANHEIRO DE AVENTURA.\n\nBoa sorte na proxima vez, {nome}...', font='Times 20')],
        [sg.Image(bt.died)]
    ]
    return sg.Window('FIM!',layout=layout,icon=bt.skull,finalize=True)
def fim_ruim(nome):
    sg.theme('Black')
    layout=[
        [sg.Text(f'VOCÊ FEZ UMA PÉSSIMA ESCOLHA.\nA BRUXA MATOU VOCÊS DOIS!\n\nBoa sorte na proxima vez, {nome}...',font='Times 15')],
        [sg.Image(bt.died)]
    ]
    return sg.Window('FIM!',layout=layout,icon=bt.skull,finalize=True)
def floresta(nome):
    sg.theme('DarkGrey11')
    layout=[
        [sg.Text(f'\nUI UI UI GOSTA DO ESCURIN NE?!\n{nome}, você sabe que não tem nenhuma tocha ou lanterna ne?\n',font='Times 15')],
        [sg.Text('Agora não tem mais volta...',font='Times 13')],
        [sg.Button('Continuar',font='Times 11')]
    ]
    return sg.Window('Floresta Sombria',layout=layout,icon=bt.icone,finalize=True)
def cont_floresta(nome,m):
    sg.theme('DarkTanBlue')
    layout=[
        [sg.Text('Vocês encontraram uma bruxa, agora chegou a hora de saber o que você tem na sua mochila: \n',font='Times 15')],
        [sg.Text(f'{nome}, a mochila que você escolheu possui: {m[0]}, {m[1]}, {m[2]}.\n',font='Times 13')],
        [sg.Button('Continuar',font='Times 11')]
    ]
    return sg.Window('Floresta Sombria',layout=layout,icon=bt.icone,finalize=True)
def floresta_arq(nome,m):
    sg.theme('DarkGrey12')
    layout=[]
    if m[0]=='espada':
        layout=[
            [sg.Text('O arqueiro usou uma flecha sem sua permissão e a bruxa está atras de vocês agora.\n',font='Times 15')],
            [sg.Text(f'{nome}, você irá usar a espada?',font='Times 13')],
            [sg.Button('',image_data=bt.check,key='-Yes-',button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0),sg.Button('',image_data=bt.cancell,key='-No-',button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0)]
        ]
    elif m[0]=='flechas':
        layout=[
            [sg.Text('O arqueiro está pedindo algumas flechas para poder pegar a bruxa de surpresa.\n',font='Times 15')],
            [sg.Text(f'{nome}, você dará as flechas para ele?',font='Times 13')],
            [sg.Button('',image_data=bt.check,key='-Yes-',button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0),sg.Button('',image_data=bt.cancell,key='-No-',button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0)]
        ]
    elif m[0]=='bombas de fumaça':
        layout=[
            [sg.Text('O arqueiro sugeriu a capa da invisibilidade. Porém, você não poderá usar de novo...\n',font='Times 15')],
            [sg.Text(f'{nome}, você usará a capa?',font='Times 13')],
            [sg.Button('',image_data=bt.check,key='-Yes-',button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0),sg.Button('',image_data=bt.cancell,key='-No-',button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0)]
        ]
    return sg.Window('Floresta Sombria',layout=layout,icon=bt.icone,finalize=True)
def cont_arq(nome,m):
    sg.theme('DarkGrey12')
    layout=[]
    if m[0]=='espada':
        layout=[
            [sg.Text(f'{nome}, você está com sorte, o arqueiro irá te ajudar.\n', font='Times 15')],
            [sg.Text('A bruxa morreu, foi bem fácil...',font='Times 13')],
            [sg.Button('Continuar',font='Times 11',key='Continuar')]
        ]
    elif m[0]=='flechas':
        layout=[
            [sg.Text('A bruxa morreu, foi bem fácil...\n',font='Times 15')],
            [sg.Button('Continuar',font='Times 13',key='Continuar')]
        ]
    elif m[0]=='bombas de fumaça':
        layout=[
            [sg.Text('Vish, a bruxa ouviu vocês e conseguiu rasgar a capa.\nMas você ainda tem um artifício.',font='Times 15')],
            [sg.Text(f'{nome}, você usará a bomba de fumaça?',font='Times 13')],
            [sg.Button('',image_data=bt.check,key='-Yes-',button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0),sg.Button('',image_data=bt.cancell,key='-No-',button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0)]
        ]
    return sg.Window('Floresta Sombria',layout=layout,icon=bt.icone,finalize=True)
def cont1_arq():
    sg.theme('DarkBrown6')
    layout=[
        [sg.Text('A bruxa não viu vocês.\nTiveram sorte e puderam sair da floresta à salvo!\n',font='Times 20')],
        [sg.Button('Continuar',font='Times 15',key='Continuar')]
    ]
    return sg.Window('Floresta Sombria',layout=layout,icon=bt.icone,finalize=True)
def floresta_feit(nome):
    sg.theme('DarkGrey12')
    layout=[
        [sg.Text(f'{nome}, você tem sorte!\nO feiticeiro matou a bruxa antes que ela visse vocês!\n',font='Times 20')],
        [sg.Button('Continuar',font='Times 15',key='Continuar')]
    ]
    return sg.Window('Floresta Sombria',layout=layout,icon=bt.icone,finalize=True)
def floresta_ninja(nome,m):
    sg.theme('DarkGrey12')
    layout=[]
    if m[0]=='espada':
        layout=[
            [sg.Text('O ninja ajudou você a se esconder, está pedindo sua espada para matar a bruxa, escolha:\n',font='Times 20')],
            [sg.Text(f'{nome}, você irá entregar a espada?',font='Times 15')],
            [sg.Button('',image_data=bt.check,key='-Yes-',button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0),sg.Button('',image_data=bt.cancell,key='-No-',button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0)]
        ]
    elif m[0]=='flechas':
        layout=[
            [sg.Text('O ninja sabe atirar flechas com as mãos. E está pedindo elas para atirar na bruxa.\n',font='Times 20')],
            [sg.Text(f'{nome}, você dará as flechas para ele?',font='Times 15')],
            [sg.Button('',image_data=bt.check,key='-Yes-',button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0),sg.Button('',image_data=bt.cancell,key='-No-',button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0)]
        ]
    elif m[0]=='bombas de fumaça':
        layout=[
            [sg.Text('O ninja sabe usar muito bem as bombas. E está pedindo as bombas para vocês fugirem.\n',font='Times 20')],
            [sg.Text(f'{nome}, você entregará as bombas?',font='Times 15')],
            [sg.Button('',image_data=bt.check,key='-Yes-',button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0),sg.Button('',image_data=bt.cancell,key='-No-',button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0)]
        ]
    return sg.Window('Floresta Sombria',layout=layout,icon=bt.icone,finalize=True)
def cont_ninja(nome,m):
    sg.theme('DarkGrey12')
    layout=[]
    if m[0]=='espada':
        layout=[
            [sg.Text(f'{nome}, você está com sorte, o ninja irá te ajudar.\n',font='Times 20')],
            [sg.Text('A bruxa morreu, foi bem fácil...',font='Times 15')],
            [sg.Button('Continuar',font='Times 13',key='Continuar')]
        ]
    elif m[0]=='flechas':
        layout=[
            [sg.Text('A bruxa morreu, mas o ninja não atira flechas muito bem, você terá que perder sua poção da vida para sobreviver...\n',font='Times 20')],
            [sg.Button('Continuar',font='Times 13',key='Continuar')]
        ]
    elif m[0]=='bombas de fumaça':
        layout=[
            [sg.Text('A bruxa não viu vocês. Tiveram sorte e puderam sair da floresta à salvo!\n',font='Times 20')],
            [sg.Button('Continuar',font='Times 13',key='Continuar')]
        ]
    return sg.Window('Floresta Sombria',layout=layout,icon=bt.icone,finalize=True)
def fim_(nome,p,m):
    sg.theme('DarkBrown6')
    layout=[
        [sg.Text('Parabéns por sobreviver à floresta sombria!\n\n',font='Times 15')],
        [sg.Text(f'{nome}, vocês chegaram ao vilarejo que fica a sua casa!',font='Times 15')],
        [sg.Text(f'Parabens, você tem bastante sorte. Agora aproveite sua refeição: {m[1]}!!\n',font='Times 15')],
        [sg.Text(f'O {p} se ofereceu para ser seu guarda. Aceita?',font='Times 13')],
        [sg.Button('',image_data=bt.check,key='-Yes-',button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0),sg.Button('',image_data=bt.cancell,key='-No-',button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0)]
    ]
    return sg.Window('Final',layout=layout,icon=bt.happy,finalize=True)
def fim_sim(nome):
    sg.theme('DarkBrown6')
    layout=[
        [sg.Text('Agora sua casa está mais protegida!\n\n',font='Times 25')],
        [sg.Text(f'Parabéns, {nome}!! Você finalizou o jogo.',font='Times 20')],
        [sg.Image(bt.winner)]
    ]
    return sg.Window('Final',layout=layout,icon=bt.happy,finalize=True)
def fim_nao(nome,p):
    sg.theme('DarkBrown6')
    p=p.capitalize()
    layout=[
        [sg.Text(f'-{p}: "Obrigado por me libertar, {nome}.\nAgora posso retornar para minha família."\n\n',font='Times 25')],
        [sg.Text(f'Parabéns, {nome}!! Você finalizou o jogo.',font='Times 20')],
        [sg.Image(bt.winner)]
    ]
    return sg.Window('Final',layout=layout,icon=bt.happy,finalize=True)

        ########                       ########                 ######                   ####################          ########   
    ################                 ############               ######                   ####################      ################ 
  ######       #######              ######  ######              ######                   ######                  #######      #######
######           ######            ######    ######             ######                   ######                ######           ######
#######           ####            ######      ######            ######                   ######                #######           ####
##########                       ######        ######           ######                   ######                ##########
  ############                  ######          ######          ######                   ######                  ############
    #############              ########################         ######                   ####################      #############
        #############         ##########################        ######                   ####################          #############
           ###########       ######                ######       ######                   ######                           ###########
              #########     ######                  ######      ######                   ######                              #########
#####       ##########     ######                    ######     ######                   ######                #####       ##########
######     #########      ######                      ######    ######                   ######                ######     #########
  ###############        ######                        ######   #######################  ####################    ###############
    ##########          ######                          ######  #######################  ####################      ##########

janela=janela_inicial()
mochi=None
while True:
    event,values=janela.read()
    if event==sg.WIN_CLOSED:
        break
    if event=='-Continue-':
        nome=(values['nome']).capitalize()
        print(f'Seu nome é {nome}')
        mochi=mochila(nome)
        event1,values1=mochi.read()
        if event1=='Voltar':
            mochi.hide()
        if event1=='Continuar':
            if values1['m1']==True:
                m=['espada','maçãs','mapa estranho']
                print('Mochila 1')
            if values1['m2']==True:
                m=['flechas','pães','poção da vida']
                print('Mochila 2')
            if values1['m3']==True:
                m=['bombas de fumaça','ração','capa da invisibilidade']
                print('Mochila 1')
            mochi.hide()
            perso=acomp(nome)
            event2,values2=perso.read()
            if event2=='Voltar':
                perso.hide()
            if event2=='Continuar':
                if values2['arq']==True:
                    p='arqueiro'
                if values2['feit']==True:
                    p='feiticeiro'
                if values2['ninja']==True:
                    p='ninja'
                print(f' Seu companheiro é {p}')
                perso.hide()
                cam=caminho(nome,p)
                event3,values3=cam.read()
                if event3=='Voltar':
                    cam.hide()
                if event3=='pantano':
                    cam.hide()
                    pant=pantano(nome)
                    print('Nojento...')
                    ev4,v4=pant.read()
                    if ev4=='Continuar':
                        pant.hide()
                        janela.hide()
                        final=fim_pantano(nome)
                        ev5,v5=final.read()
                        if ev5==sg.WIN_CLOSED:
                            break
                if event3=='sombrio':
                    cam.hide()
                    sombrio=floresta(nome)
                    ev4,v4=sombrio.read()
                    if ev4=='Continuar':
                        print('Gosta do Escurin')
                        sombrio.hide()
                        sombrio1=cont_floresta(nome,m)
                        ev5,v5=sombrio1.read()
                        if ev5=='Continuar':
                            sombrio1.hide()
                            # Arqueiro
                            if p=='arqueiro':
                                sombrio2=floresta_arq(nome,m)
                                ev6,v6=sombrio2.read()
                                if ev6=='-Yes-':
                                    sombrio2.hide()
                                    sombrio3=cont_arq(nome,m)
                                    ev7,v7=sombrio3.read()
                                    if ev7=='Continuar':
                                        sombrio3.hide()
                                        janela.hide()
                                        fim1=fim_(nome,p,m)
                                        ev8,v8=fim1.read()
                                        if ev8=='-Yes-':
                                            fim1.hide()
                                            fim2=fim_sim(nome)
                                            ev9,v9=fim2.read()
                                            if ev9==sg.WIN_CLOSED:
                                                break
                                        if ev8=='-No-':
                                            fim1.hide()
                                            fim2=fim_nao(nome,p)
                                            ev9,v9=fim2.read()
                                            if ev9==sg.WIN_CLOSED:
                                                break
                                    if ev7=='-Yes-':
                                        sombrio3.hide()
                                        sombrio4=cont1_arq()
                                        ev8,v8=sombrio4.read()
                                        if ev8=='Continuar':
                                            sombrio4.hide()
                                            janela.hide()
                                            fim1=fim_(nome,p,m)
                                            ev9,v9=fim1.read()
                                            if ev9=='-Yes-':
                                                fim1.hide()
                                                fim2=fim_sim(nome)
                                                ev10,v10=fim2.read()
                                                if ev10==sg.WIN_CLOSED:
                                                    break
                                            if ev9=='-No-':
                                                fim1.hide()
                                                fim2=fim_nao(nome,p)
                                                ev10,v10=fim2.read()
                                                if ev10==sg.WIN_CLOSED:
                                                    break
                                    if ev7=='-No-':
                                        sombrio3.hide()
                                        janela.hide()
                                        final=fim_ruim(nome)
                                        ev8,v8=final.read()
                                        if ev8==sg.WIN_CLOSED:
                                            break
                                if ev6=='-No-':
                                    sombrio2.hide()
                                    janela.hide()
                                    final=fim_ruim(nome)
                                    ev7,v7=final.read()
                                    if ev7==sg.WIN_CLOSED:
                                        break
                            # Feiticeiro
                            elif p=='feiticeiro':
                                sombrio2=floresta_feit(nome)
                                ev6,v6=sombrio2.read()
                                if ev6=='Continuar':
                                    sombrio2.hide()
                                    fim1=fim_(nome,p,m)
                                    ev7,v7=fim1.read()
                                    if ev7=='-Yes-':
                                        fim1.hide()
                                        janela.hide()
                                        fim2=fim_sim(nome)
                                        ev8,v8=fim2.read()
                                        if ev8==sg.WIN_CLOSED:
                                            break
                                    if ev7=='-No-':
                                        fim1.hide()
                                        janela.hide()
                                        fim2=fim_nao(nome,p)
                                        ev8,v8=fim2.read()
                                        if ev8==sg.WIN_CLOSED:
                                            break
                            # Ninja
                            elif p=='ninja':
                                sombrio2=floresta_ninja(nome,m)
                                ev6,v6=sombrio2.read()
                                if ev6=='-Yes-':
                                    sombrio2.hide()
                                    sombrio3=cont_ninja(nome,m)
                                    ev7,v7=sombrio3.read()
                                    if ev7=='Continuar':
                                        sombrio3.hide()
                                        fim1=fim_(nome,p,m)
                                        ev8,v8=fim1.read()
                                        if ev8=='-Yes-':
                                            fim1.hide()
                                            fim2=fim_sim(nome)
                                            ev9,v9=fim2.read()
                                            if ev9==sg.WIN_CLOSED:
                                                break
                                        if ev8=='-No-':
                                            fim1.hide()
                                            fim2=fim_nao(nome,p)
                                            ev9,v9=fim2.read()
                                            if ev9==sg.WIN_CLOSED:
                                                break
                                if ev6=='-No-':
                                    final=fim_ruim(nome)
                                    sombrio2.hide()
                                    janela.hide()
                                    ev7,v7=final.read()
                                    if ev7==sg.WIN_CLOSED:
                                        break