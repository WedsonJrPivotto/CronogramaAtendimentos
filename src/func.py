from customtkinter import CTkEntry

class Functions():
    def MeioTela(main, x: int, y: int) -> str:
        # Calcula o meio da tela e retorna um texto com a medida "XXXxYYY+x+y"
        main.update_idletasks()
        xTela = main.winfo_screenwidth()
        yTela = main.winfo_screenheight()
        pos_x = (xTela - x) // 2
        pos_y = (yTela - y) // 2
        text = f'{x}x{y}+{pos_x}+{pos_y}'
        return text

    @staticmethod
    def formatar_data(event=None, entry=None):
        if entry is None:
            return  # Se não houver entry, não faz nada

        texto = entry.get().replace("/", "")
        texto_formatado = ""

        for i in range(len(texto)):
            if i == 2 or i == 4:
                texto_formatado += "/"
            texto_formatado += texto[i]

        if len(texto_formatado) > 10:
            texto_formatado = texto_formatado[:10]

        entry.delete(0, "end")
        entry.insert(0, texto_formatado)

    @staticmethod
    def formatar_hora(event=None, entry=None):
        if entry is None:
            return
        texto = entry.get().replace(":", "")
        texto_formatado = ""

        for i in range(len(texto)):
            if i == 2:
                texto_formatado += ":"
            texto_formatado += texto[i]

        if len(texto_formatado) > 5:
            texto_formatado = texto_formatado[:5]

        entry.delete(0, "end")
        entry.insert(0, texto_formatado)

    @staticmethod
    def mudar_foco(proximo_campo=None):
        proximo_campo.focus()   

    
           