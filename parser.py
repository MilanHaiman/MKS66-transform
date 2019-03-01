from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    lines=open(fname,'r').read().split('\n')
    for i in range(len(lines)):
      if lines[i]=="line":
        i+=1
        data=lines[i].split(' ')
        x0,y0,z0,x1,y1,z1=int(data[0]),int(data[1]),int(data[2]),int(data[3]),int(data[4]),int(data[5])
        add_edge( points, x0, y0, z0, x1, y1, z1 )
        continue
      if lines[i]=="ident":
        ident(transform)
        continue
      if lines[i]=="scale":
        i+=1
        data=lines[i].split(' ')
        x,y,z=int(data[0]),int(data[1]),int(data[2])
        matrix_mult( make_scale(x,y,z), transform )
        continue
      if lines[i]=="translate":
        i+=1
        data=lines[i].split(' ')
        x,y,z=int(data[0]),int(data[1]),int(data[2])
        matrix_mult( make_translate(x,y,z), transform )
        continue
      if lines[i]=="rotate":
        i+=1
        data=lines[i].split(' ')
        t=int(data[1])
        if data[0]=='x':
          matrix_mult( make_rotX(t), transform )
          continue
        if data[0]=='y':
          matrix_mult( make_rotY(t), transform )
          continue
        if data[0]=='z':
          matrix_mult( make_rotZ(t), transform )
          continue
      if lines[i]=="apply":
        matrix_mult( transform, points )
        continue
      if lines[i]=="display":
        clear_screen( screen )
        draw_lines( points, screen, color )
        display( screen )
        continue
      if lines[i]=="save":
        i+=1
        tosave=lines[i]
        clear_screen( screen )
        draw_lines( points, screen, color )
        save_extension( screen, tosave )
        continue
      if lines[i]=="quit":
        return
      


