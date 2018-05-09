def obslugaPunktow(dlaKogo):
    if dlaKogo:
        interfacePrinter.points_increase(True) # zwieksz wynik w interfejsie
        gameStateDict['P1Points']=gameStateDict['P1Points']+1  # oraz stanie gry 
        if gameStateDict['P1Points']>7: # jak zdobedzie wiekszosc kluczy 
            interfacePrinter.score_increase(True) # zwieksz Score wyzeruj punkty
            gameStateDict['P1Points']=0
            gameStateDict['P2Points']=0
            gameStateDict['P1Score']=gameStateDict['P1Score']+1
            if gameStateDict['P1Score']>2: # jak wygra 3 rundy 
                clscr()
                interfacePrinter.print_interface()  # pokazuje interface
                print('***PLAYER1 WINS***')
                printingTheMap(lista)  # wczytywanie mapy
                return False # zakoncz gre
            else:
                clscr()
                interfacePrinter.print_interface()  # pokazuje interface
                print('***PLAYER1 GETS POINTS***')
                printingTheMap(lista)  # wczytywanie mapy
                time.sleep(5) # ustaw mape na nowo
                gracz_1.przestaw(1,20,lista)
                gracz_2.przestaw(20,20,lista)
                init_keys(lista)
        return True
    else:
        interfacePrinter.points_increase(False) # zwieksz wynik w interfejsie
        gameStateDict['P2Points']=gameStateDict['P2Points']+1 # oraz stanie gry 
        if gameStateDict['P2Points']>7: # jak zdobedzie wiekszosc kluczy 
            interfacePrinter.score_increase(False) # zwieksz Score wyzeruj punkty
            gameStateDict['P2Points']=0
            gameStateDict['P1Points']=0
            gameStateDict['P2Score']=gameStateDict['P2Score']+1
            if gameStateDict['P2Score']>2: # jak wygra 3 rundy 
                clscr()
                print('***Player2 WINS***')
                interfacePrinter.print_interface()  # pokazuje interface
                printingTheMap(lista)  # wczytywanie mapy
                return False # zakoncz gre
            else:
                clscr()
                interfacePrinter.print_interface()  # pokazuje interface
                print('***PLAYER2 GETS POINTS***')
                printingTheMap(lista)  # wczytywanie mapy
                time.sleep(5) # ustaw mape na nowo
                gracz_1.przestaw(1,20,lista)
                gracz_2.przestaw(20,20,lista)
                init_keys(lista)
        return True