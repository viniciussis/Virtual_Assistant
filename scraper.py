import webbrowser as wb

url = "https://www.todamateria.com.br/media/#:~:text=M%C3%A9dia%20Aritm%C3%A9tica%20Simples,2%2C...%2Cxn%3A%20valores%20dos%20dados"

def atuar_area(acao, objeto, _):
    executado = False

    if acao == "área" and objeto == "região nordeste":  
        executado = True
        
        wb.open(url)
        print("É claro! A área da {objeto} é...")

    return executado

def atuar_flora(acao, objeto, _):
    executado = False

    if acao == "flora" and objeto == "região nordeste" or objeto == "região sudeste" or objeto == "região sul" or objeto == "região centro-oeste" or objeto == "região norte":  
        executado = True
        
        wb.open(url)
        print("É claro! A flora da {objeto} é...")

    return executado

def atuar_fauna(acao, objeto, _):
    executado = False
    
    if acao == "fauna" and objeto == "região nordeste" or objeto == "região sudeste" or objeto == "região sul" or objeto == "região centro-oeste" or objeto == "região norte":  
        executado = True
        
        wb.open(url)
        print("É claro! A fauna da {objeto} é...")

    return executado

def atuar_afluentes(acao, objeto, _):
    executado = False
    
    if acao == "afluentes" and objeto == "região nordeste" or objeto == "região sudeste" or objeto == "região sul" or objeto == "região centro-oeste" or objeto == "região norte":  
        executado = True
        
        wb.open(url)
        print("É claro! Os principais afluentes da {objeto} são...")

    return executado

def atuar_clima(acao, objeto, _):
    executado = False
    
    if acao == "clima" and objeto == "região nordeste" or objeto == "região sudeste" or objeto == "região sul" or objeto == "região centro-oeste" or objeto == "região norte":  
        executado = True
        
        wb.open(url)
        print("É claro! O clima da {objeto} é...")

    return executado

def atuar_população(acao, objeto, _):
    executado = False
    
    if acao == "população" and objeto == "região nordeste" or objeto == "região sudeste" or objeto == "região sul" or objeto == "região centro-oeste" or objeto == "região norte":  
        executado = True
        
        wb.open(url)
        print("É claro! A população da {objeto} é...")

    return executado