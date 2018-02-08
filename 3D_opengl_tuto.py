#!coding: utf-8
from __future__ import print_function, division
from OpenGL.GL import *
from OpenGL.GL import shaders
from vec3_utils import *
# créer un compte sur github.com, fork gitub.com/robertvandeneynde/parascolaire-students, clone, modif, commit, push, pull request

import pygame
pygame.init()

pygame.display.set_mode((1280, 720), pygame.OPENGL | pygame.DOUBLEBUF)

NOIR = [0, 0, 0]
BLANC = [1, 1, 1]
ROUGE = [1, 0, 0]
VERT = [0, 1, 0]
BLEU = [0, 0, 1]

vertex_shader = '''
#version 330
// contenu du vertex shader
in vec4 position;

void main() {
    gl_Position = position;
}
'''

fragment_shader = '''
#version 330
// contenu du fragment shader

out vec4 pixel;

void main() {
    pixel = vec4(1, 0.6, 0, 1);
}
'''

shader_program = shaders.compileProgram(
    shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
    shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))

vertices = farray([
    0.6, 0.6, 0.0, 1.0,
    -0.6, 0.6, 0.0, 1.0,
    0.0, -0.6, 0.0, 1.0,
])


vertex_array_object = glGenVertexArrays(1)
glBindVertexArray(vertex_array_object)

vertex_buffer = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
glBufferData(GL_ARRAY_BUFFER, ArrayDatatype.arrayByteCount(vertices), vertices, GL_STATIC_DRAW)

position = glGetAttribLocation(shader_program, 'position')
if position != -1:
    glEnableVertexAttribArray(position)
    glVertexAttribPointer(position, 4, GL_FLOAT, False, 0, ctypes.c_void_p(0))
else:
    print('inactive attribute {}'.format(position))

glBindBuffer(GL_ARRAY_BUFFER, 0)
glBindVertexArray(0)



# DÉBUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK

    # DESSIN
    glClearColor(1, 0.8, 0.8, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    glUseProgram(shader_program)
                         
    glBindVertexArray(vertex_array_object)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glBindVertexArray(0)
                         
    glUseProgram(0)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
