def clear(label):
    label.config(text="0")

def remove(label):
    texto_atual = label.cget("text")
    if texto_atual and texto_atual != 0:
        label.config(text=texto_atual[:-1] if len(texto_atual) > 1 else "0")

def divide(label):
    texto_atual = label.cget("text")
    label.config(text=texto_atual + "/")

def multiplica(label):
    texto_atual = label.cget("text")
    label.config(text=texto_atual + "*")

def subtracao(label):
    texto_atual = label.cget("text")
    label.config(text=texto_atual + "-")
    
def soma(label):
    texto_atual = label.cget("text")
    label.config(text=texto_atual + "+")

def add_number(label, number):
    texto_atual = label.cget("text")
    if texto_atual: 
        label.config(text=texto_atual + str(number) if texto_atual != "0" else str(number))
        return

def result(label):
    texto_atual = label.cget("text")
    
    try:
        resultado = eval(texto_atual)
    except ZeroDivisionError:
        resultado = "ZeroDivisionError"
    except Exception:
        resultado = "Erro"
    finally:
        label.config(text=str(resultado))