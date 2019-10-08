from pygame.locals import *
from Variables import *
class Camera(object):

    def __init__(self, camera_func, map):
        self.camera_func = camera_func   #macera_func is the type of camera we will use (simple or complex)
        self.state = Rect(0, 0, map[0], map[1])   #map is the total size of the map (scene)


    def apply(self, targetrect):       #defines the objective that the camara will follow (can be changed in-live)
        return targetrect.move(self.state.topleft)


    def update(self, target):     #when we update we move all the elements with repect to our objective
        self.state = self.camera_func(self.state, target.rect_spr)


def simple_camera(camera, target_rect):   #follow objective going away from limits of the window
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l+ventana[0]//2, -t+ventana[1]//2, w, h)


def complex_camera(camera, target_rect):  #camara that follows objective without going away of the limits of the window

    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+ventana[0]//2, -t+ventana[1]//2, w, h
    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-ventana[0]), l)   # stop scrolling at the right edge
    t = max(-(camera.height-ventana[1]), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return Rect(l, t, w, h)
