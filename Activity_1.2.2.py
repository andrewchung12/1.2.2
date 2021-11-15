# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb
#-----game configuration----
t_color = "red"
t_size = 3
t_shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000
timer_up = False
# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")
#-----initialize turtle-----
tri = trtl.Turtle()
tri.shape(t_shape)
tri.shapesize(t_size)
tri.fillcolor(t_color)

score_write = trtl.Turtle()
score_write.penup()
score_write.goto(160,-195)
score_write.hideturtle()

timer_write = trtl.Turtle()
timer_write.penup()
timer_write.goto(50,180)
timer_write.hideturtle()
#-----game functions--------
def tri_clicked(x,y):
  global timer
  if(timer > 0):
    update_score()
    change_pos()
  else:
    tri.hideturtle()
def change_pos():
  new_x = rand.randint(-200,200)
  new_y = rand.randint(-200,200)
  tri.penup()
  tri.hideturtle()
  tri.goto(new_x,new_y)
  tri.showturtle()
  tri.pendown()
  
def update_score():
  global score
  score += 1
  score_write.clear()
  score_write.write(score,font=font_setup)

def countdown():
  global timer, timer_up
  timer_write.clear()
  if timer <= 0:
    timer_write.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    timer_write.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    timer_write.getscreen().ontimer(countdown, counter_interval)
    # manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global tri

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > int(leader_scores_list[4])):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, tri, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, tri, score)

#-----events----------------
trtl.bgcolor("green")
wn = trtl.Screen()
tri.onclick(tri_clicked)
countdown()
wn.mainloop()