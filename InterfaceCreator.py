'''
Created on 17 kwi 2018

@author: JakubF
'''

class InterfaceCreator(object):
    '''
    Klasa generujaca interfejs z wynikami gry
    
    ogolne uzycie
        utworz instancje klasy
        zmieniaj punkty za pomoca points_increase/decrease
        zwieksz wynik za pomoca score_increase
        
        zwroc string z interfejsem za pomoca
            return_interface
        wydrukuj go za pomoca 
            print_interface
            
        funkcje line sa uzywane w return_interface
        kazda z nich drukuje inna jego czesc 
    '''
    
    
    def __init__(self, plansza_size=80,plansza_symbol="*"):
        
        '''
        Constructor
        Przyjmuje 2 parametry 
        plansza_size czyli ile znakow wydrukuje w jednej lini musi conwertowac na inta
        plansza_symbol za pomoca jakiego smbolu bedzie wypisywal linie musi byc krotszy od rozmiaru planszy/2 - 6(najszerszy punkt interfejsu)
        i dopisuje je do zmiennych prywatnych o tych samych nazwach
        
        '''
        try:
            self._plansza_size=int(plansza_size)
            self._plansza_symbol=str(plansza_symbol)
            if self._plansza_size<(len(self._plansza_symbol)*2+6):
                raise AssertionError
            self.set_up_Int()
        except ValueError:
            print("Rozmiar planszy musi byc konwertowalny na inta") 
            raise ValueError
        except AssertionError:
            print("Dlugosc symbolu nie moze przekroczyc rozmiaru planszy")
            raise AssertionError
    
    def set_up_Int(self):
        '''
        ustawia poczatkowe statystyki
        punkty graczy p1Points,p2Points
        wynik ogolny wynik
        '''
        self.p1Points=0
        self.p2Points=0
        self.score="|"
        
        
    def points_increase(self,side):
        '''
        zwieksza punkty gracza o 1
        param:
            side :bool 
        lewego jezeli TRUE 
        Prawego jezeli FALSE
        '''
        if side:
            self.p1Points+=1  
        else: 
            self.p2Points+=1
            
    
    def points_decrease(self,side):
        '''
        zmniejsza punkty gracza o 1 jezeli sa wieksze od zera
        param:
            side :bool 
        lewego jezeli TRUE 
        Prawego jezeli FALSE
        '''
        if side and self.p1Points>0:
            self.p1Points-=1  
        elif side==False and self.p2Points>0: 
            self.p2Points-=1
    
            
    def score_increase(self,side):
        '''
        zwieksza wynik gracza o 1 po czym zeruje punkty obu graczom 
        wynik jest w postaci ilosci gwiazdek po kazdej ze stron
        param:
            side :bool 
        lewego jezeli TRUE 
        Prawego jezeli FALSE
        '''
        if side:
            self.score="*"+self.score  
        else: 
            self.score=self.score+"*"
        self.p2Points=0
        self.p1Points=0

            
    def return_interface(self):
        '''
        funkcjka zwracajaca stringa zlozonego z funkcji line
        ogolny wyglad interfejsu
        '''
        string_interface=self.line_breaker()
        string_interface+=self.line_sides()
        string_interface+=self.line_score()
        string_interface+=self.line_sides()
        string_interface+=self.line_points()
        string_interface+=self.line_sides()
        string_interface+=self.line_breaker()
        return string_interface
        
    def print_interface(self):
        '''
        funkcja drukujaca interfej
        wywoluje funkcje tworzaca iterfejs
        '''
        print(self.return_interface())    
        
        
    def line_breaker(self):
        '''
        funkcja drukujaca interfej
        tworzy ciagla linie
        zwraca stringa
        '''
        text=self._plansza_symbol*self._plansza_size
        return text[:self._plansza_size]+"\n"
    
    
    def line_sides(self):
        '''
        funkcja drukujaca interfej
        tworzy boczne sciany
        zwraca stringa
        '''
        return self._plansza_symbol+(" "*(self._plansza_size-2*len(self._plansza_symbol)))+self._plansza_symbol+"\n"
    
    
    def line_score(self):
        '''
        funkcja drukujaca interfej
        tworzy 2 line od wyniku gry
        zwraca stringa
        '''
        text=self._plansza_symbol+"SCORE".center(self._plansza_size-2*len(self._plansza_symbol), ' ')+self._plansza_symbol+"\n"
        text+=self._plansza_symbol+self.score.center(self._plansza_size-2*len(self._plansza_symbol), ' ')+self._plansza_symbol+"\n"
        return text
    
    
    def line_points(self):
        '''
        funkcja drukujaca interfej
        tworzy 2 linie od punktow gry
        zwraca stringa
        '''
        text=self._plansza_symbol+"P1"+(" "*(self._plansza_size-4-2*len(self._plansza_symbol)))+"P2"+self._plansza_symbol+"\n"
        text+=self._plansza_symbol+str(self.p1Points).zfill(3)+(" "*(self._plansza_size-6-2*len(self._plansza_symbol)))+str(self.p2Points).zfill(3)+self._plansza_symbol+"\n"
        return text