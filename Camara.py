from pygame.locals import *
from Variables import *
class Camera(object):
    ''' Camera_func es el tipo de "seguir" que vamos
        a hacer sobre el objeto.
        map, tamaño total del mapa/escena, es decir,
        si nuestra ventana es de 800x600 pero la escena de 1000x700,
        pues ponemos 1000x700
    '''
    def __init__(self, camera_func, map):
        self.camera_func = camera_func
        self.state = Rect(0, 0, map[0], map[1])



    ''' Sobre qué objeto vamos a realizar el seguimiento.
        Se puede cambiar "en vivo"
    '''
    def apply(self, targetrect):
        return targetrect.move(self.state.topleft)

    ''' Función a la que llamamos a la hora de hacer "update"
        para desplazar el resto del mundo con respecto
        a nuestro "objetivo".
    '''
    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

''' Cámara que sigue al objetivo, pero le
    dan igual los límites de la ventana
'''
def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l+w//2, -t+h//2, w, h)

'''camara que sigue al objetivo respetando
    los limites de la ventana
'''

def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+w//2, -t+h//2, w, h
    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-ventana[0]), l)   # stop scrolling at the right edge
    t = max(-(camera.height-ventana[1]), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return Rect(l, t, w, h)
