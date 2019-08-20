class Scene:
    '''Representa un escena abstracta del videojuego.

    Una escena es una parte visible del juego, como una pantalla
    de presentación o menú de opciones.
    '''

    def __init__(self, director):
        #Contiene el director para poder acceder a cosas como
        #el reloj o la pantalla
        self.director = director

    def on_update(self, time):
        ''' Actualización lógica que se llama automáticamente desde el director
        '''
        raise NotImplemented("Tiene que implementar el método on_update.")

    def on_event(self, time, event):
        ''' Se llama cuando llega un evento especifico al bucle
            Le pasamos también la variable "time" por que para
            actualizaciones de movimiento, etc nos vendrá bien
        '''
        raise NotImplemented("Tiene que implementar el método on_event.")

    def on_draw(self, screen):
        ''' Se llama cuando se quiere dibujar la pantalla
        '''
        raise NotImplemented("Tiene que implementar el método on_draw.")
