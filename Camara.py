class Camera(object):
    ''' Camera_func es el tipo de "seguir" que vamos
        a hacer sobre el objeto.
        Width y Height, tamaño total del mapa/escena, es decir,
        si nuestra ventana es de 800x600 pero la escena de 1000x700,
        pues ponemos 1000x700
    '''
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    ''' Sobre qué objeto vamos a realizar el seguimiento.
        Se puede cambiar "en vivo"
    '''
    def apply(self, target):
        return target.rect.move(self.state.topleft)

    ''' Función a la que llamamos a la hora de hacer "update"
        para desplazar el resto del mundo con respecto
        a nuestro "objetivo".
    '''
    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

''' Cámara que sigue al objetivo, pero le
    dan igual los límites de la ventana
'''
