# Copyright 2021 Émilia BEGUIN Arthur Schneider
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

def convert(n : int, b : int) -> str :
    rep=''
    q=-1
    if b>16:
        return 'la base est sup a 16'
    if b==10:
        return str(n)

    while q !=0: #q pour quotient
        q=n//b
        r=n%b
        n=q
        if r<10 or b<10:
            rep+=str(r)
        elif r==10 and b>10:
            rep+='A'
        elif r==11 and b>11:
            rep+='B'
        elif r==12 and b>12:
            rep+='C'
        elif r==13 and b>13:
            rep+='D'
        elif r==14 and b>14:
            rep+='E'
        elif r==15 and b>15:
            rep+='F'
        else:
            return ('erreur',r)
    return rep[::-1]

def printRectangle(width: int, height: int) :
    for i in range(height):
        for y in range(width):
            print('*',end='')
        print()

def printRectangleOutline(width: int, height: int) :
    for i in range(width):
        print('*',end='')
    print()
    for i in range(height-2):
        print('*',end='')
        for i in range(width-2):
            print(" ",end='')
        print('*')
    for i in range(width):
        print('*',end='')

def printTriangle(size: int):
    for i in range(1, size+1):
        p = ""
        for _ in range(i):
            p += "*"
        print(p)

def printTriangleOutline(size: int):
    for i in range(1, size+1):
        p = ""
        if i < 3 or i == size:
            for _ in range(i):
                p += "*"
        else:
            p += "*"
            for _ in range(i-2):
                p += " "
            p += "*"
        print(p)

