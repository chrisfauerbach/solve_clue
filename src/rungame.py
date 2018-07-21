import pyglet
from pyglet.window import mouse, key

import sys

from pyglet.gl import *
import pyglet
from pyglet.window import key
pyglet.resource.path = ['imgs']
pyglet.resource.reindex()


BALLROOM_IMG = "ballroom.jpg"
HALL_IMG = "hall.jpg"
MUSTARD_IMG = "mustard.jpg"
BILLIARDROOM_IMG = "billiardroom.jpg"
KITCHEN_IMG = "kitchen.jpg"
PEACOCK_IMG = "peacock.jpg"
STUDY_IMG = "study.jpg"
CANDLESTICK_IMG = "candlestick.jpg"
KNIFE_IMG = "knife.jpg"
PLUM_IMG = "plum.jpg"
WHITE_IMG = "white.jpg"
CONSERVATORY_IMG = "convervatory.jpg"
LEADPIPE_IMG = "leadpipe.jpg"
REVOLVER_IMG = "revolver.jpg"
WRENCH_IMG = "wrench.jpg"
DININGROOM_IMG = "diningroom.jpg"
LIBRARY_IMG = "library.jpg"
ROPE_IMG = "rope.jpg"
GREEN_IMG = "green.jpg"
LOUNGE_IMG = "lounge.jpg"
SCARLETT_IMG = "scarlett.jpg"


ROOM_IMGS = [BILLIARDROOM_IMG, BALLROOM_IMG, HALL_IMG, LOUNGE_IMG, LIBRARY_IMG, 
             DININGROOM_IMG, CONSERVATORY_IMG, STUDY_IMG, KITCHEN_IMG, ]
SUSPECT_IMGS = [MUSTARD_IMG, PEACOCK_IMG, PLUM_IMG, WHITE_IMG, GREEN_IMG, SCARLETT_IMG]
WEAPON_IMGS = [ROPE_IMG, WRENCH_IMG, KNIFE_IMG, CANDLESTICK_IMG, REVOLVER_IMG, LEADPIPE_IMG]

def draw_rect(x, y, width, height):
    glBegin(GL_LINE_LOOP)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

class Control(pyglet.event.EventDispatcher):
    x = y = 0
    width = height = 10

    def __init__(self, *args, **kwargs):
        super().__init__()
        parent = args[0]
        self.parent = parent

    def hit_test(self, x, y):
        return (self.x < x < self.x + self.width and  
                self.y < y < self.y + self.height)

    def capture_events(self):
        print("Captured events.")
        self.parent.push_handlers(self)

    def release_events(self):
        print("Released events.")
        self.parent.remove_handlers(self)


class Button(Control):
    charged = False

    def draw(self):
        if self.charged:
            glColor3f(1, 0, 0)
        draw_rect(self.x, self.y, self.width, self.height)
        glColor3f(1, 1, 1)
        self.draw_label()

    def on_mouse_press(self, x, y, button, modifiers):
        self.capture_events()
        self.charged = True

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.charged = self.hit_test(x, y)

    def on_mouse_release(self, x, y, button, modifiers):
        self.release_events()
        if self.hit_test(x, y):
            self.dispatch_event('on_press')
        self.charged = False

Button.register_event_type('on_press')
    
class TextButton(Button):
    def __init__(self, *args, **kwargs):
        super(TextButton, self).__init__(*args, **kwargs)
        self._text = pyglet.text.Label('', anchor_x='center', anchor_y='center')

    def draw_label(self):
        self._text.x = self.x + self.width / 2
        self._text.y = self.y + self.height / 2
        self._text.draw()

    def set_text(self, text):
        self._text.text = text

    text = property(lambda self: self._text.text,
                    set_text)

class ImageButton(Button):
    def __init__(self, *args,**kwargs):
        super(ImageButton, self).__init__(*args, **kwargs)
        pth = kwargs.get('img_pth')
        self.image_path  = pth
        self._img = pyglet.image.load("./imgs/{}".format(pth))
        self.width, self.height = self._img.width, self._img.height
        # self._text = pyglet.text.Label('', anchor_x='center', anchor_y='center')
        self.sprite = pyglet.sprite.Sprite(img=self._img)
        self.clicked = False

    def draw_label(self): 
        if not self.clicked:
            self.sprite.x = self.x# + self.width / 2
            self.sprite.y = self.y# +self.height / 2
            self.sprite.draw()
      #  self._img.blit(self._img.x, self._img.y)

    def on_mouse_press(self, x, y, button, modifiers):
        print("My image got clicked: ", self.image_path)
        # image_part = self._img.get_region(x=10, y=10, width=10, height=10)
        #  self._img = image_part
        self.clicked = True
        if self.clicked and self.sprite:
            try:
                self.sprite.delete()
            except:
                pass
        else:
            self.sprite.draw()



     

                   
class GameWindow(pyglet.window.Window):
    GUI_WIDTH = 400
    GUI_HEIGHT = 40
    GUI_PADDING = 4
    GUI_BUTTON_HEIGHT = 16

    def __init__(self, width=None, height=None):
        super().__init__(width=width, height=height, caption='Clue Player',
                                           visible=False, 
                                           resizable=True, )
        
        self.controls = [ 
            ]

        base_x =  self.GUI_PADDING
        now_x = base_x
        now_y = self.GUI_PADDING
        for nm in ROOM_IMGS:
            img_btn = ImageButton(self, img_pth=nm) 
            img_btn.x = now_x
            img_btn.y = now_y
            now_x += img_btn.width + self.GUI_PADDING
            self.controls.append(img_btn)
            if now_x + img_btn.width > self.width:
                now_x = base_x
                now_y +=  img_btn.height + self.GUI_PADDING

        now_x = base_x
        now_y +=  img_btn.height + self.GUI_PADDING

        for nm in SUSPECT_IMGS:
            img_btn = ImageButton(self, img_pth=nm) 
            img_btn.x = now_x
            img_btn.y = now_y
            now_x += img_btn.width + self.GUI_PADDING
            self.controls.append(img_btn)
            if now_x + img_btn.width > self.width:
                now_x = base_x
                now_y +=  img_btn.height + self.GUI_PADDING

        now_x = base_x
        now_y +=  img_btn.height + self.GUI_PADDING

        for nm in WEAPON_IMGS:
            img_btn = ImageButton(self, img_pth=nm) 
            img_btn.x = now_x
            img_btn.y = now_y
            now_x += img_btn.width + self.GUI_PADDING
            self.controls.append(img_btn)
            if now_x + img_btn.width > self.width:
                now_x = base_x
                now_y +=  img_btn.height + self.GUI_PADDING

      

      
      
 
    def on_mouse_press(self, x, y, button, modifiers):
        # print("On mouse click: {} {}".format(x,y))
        for control in self.controls:
            if control.hit_test(x,y):
                control.on_mouse_press(x, y, button, modifiers)
 
    def on_button_press(self):
        for control in self.controls:
            pass#control.
        print("Can I get a what what")


    def on_draw(self):
        self.clear()
        for control in self.controls:
            control.draw()
             

if __name__ == "__main__":
    window = GameWindow(1280,720)
    window.set_visible(True)
    pyglet.app.run()

 