from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
ident(transform)
edges = new_matrix(4,0)

parse_file( 'script', edges, transform, screen, color )
