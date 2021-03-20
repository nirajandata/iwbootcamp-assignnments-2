class Simple_game():
  def __init__(self,width,height):
    self.x_postion=0
    self.y_position=0
    self.power=100
    self.width=width
    self.height=height

  def move_forward(self):
    self.y_postion+=10
  
  def move_right(self):
    self.x_postion+=10

  def move_backward(self):
    self.y_postion-=10
  
  def move_left(self):
    self.x_postion-=10
  
   