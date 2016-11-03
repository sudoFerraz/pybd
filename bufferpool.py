#/usr/env/python2.7

class bufferpool():
    """Armazenamento de paginas na memoria."""

    def __init__(self):
        """Definindo estrutura do bufferpool."""
        pass


    def buscapagina(self):
        """Busca pagina pelo gerenciador de arquivos."""
        pass


    def controle_concorrencia(self):
        """Chama subsistema responsavel pelo controle de concorrencia."""
        pass


    def substitui_frame(self, frame):
        """Define politica de substituicao de frames e aloca novo."""
        pass

    

class frame():

    def __init__():
        """Definindo estrutura de cada frame."""
        pass


    def torna_ativo():
        """Chamada para definir se o frame esta sendo utilizado."""
        pass


    def modificado():
        """Chamada para dizer que o frame foi modificado."""
        pass
