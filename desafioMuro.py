import os
import math
import sys
from datetime import datetime
from random import randrange
from time import sleep

clear = lambda: os.system("cls" if os.name == "nt" else "clear")


class Wall:
    PERSON = "*"
    DOOR = "H"
    WALL = "_"
    BEGIN = "^"


class MainClass:
    def __init__(self):
        self.doorPosition = 1
        self.wallSize = 51
        self.wall = []
        self.counter = 0
        self.firstPosition = 0
        self.personPosition = 0

    # Algorítmo O(n²)
    def findDoor(self, begin, reach, distance):
        self.personPosition = begin
        self.counter += 1
        sleep(0.05)
        clear()
        self.updateWall()
        self.printScreen()

        if begin == self.doorPosition:  # sucesso
            return begin
        elif begin == 0:  # simular limite infinito do muro
            reach = len(self.wall)
        elif begin == len(self.wall) - 1:
            reach = 0

        if begin == reach:
            distance += 1
            if reach > math.floor(self.wallSize / 2):
                reach -= distance
            else:
                reach += distance

        n = 1 if reach > begin else -1

        return self.findDoor(begin + n, reach, distance)

    # Algorítmo O(n)
    def findDoorOptmized(self, begin, reach, distance):
        self.personPosition = begin
        self.counter += 1
        sleep(0.05)
        clear()
        self.updateWall()
        self.printScreen()

        if begin == self.doorPosition:  # sucesso
            return begin
        elif begin == 0:  # simular limite infinito do muro
            reach = len(self.wall)
        elif begin == len(self.wall) - 1:
            reach = 0

        if begin == reach:
            distance *= 2
            if reach > math.floor(self.wallSize / 2):
                reach -= distance
            else:
                reach += distance

        n = 1 if reach > begin else -1

        return self.findDoorOptmized(begin + n, reach, distance)

    # Algorítmo para gerar o array da porta
    def generateWall(self):
        self.firstPosition = math.ceil(self.wallSize / 2)
        self.personPosition = math.ceil(self.wallSize / 2)
        self.counter = 0
        self.doorPosition = randrange(0, self.wallSize)
        self.updateWall()

    # Algorítmo para atualizar o array da porta
    def updateWall(self):
        self.wall = []
        for position in range(0, self.wallSize):
            if self.doorPosition == position:
                self.wall.append(Wall.DOOR)
            elif self.personPosition == position:
                self.wall.append(Wall.PERSON)
            elif self.firstPosition == position:
                self.wall.append(Wall.BEGIN)
            else:
                self.wall.append(Wall.WALL)

    # Algorítmo para imprimir o estado atual da porta
    def printScreen(self):
        displayString = ""

        for position in self.wall:
            displayString += position

        print(displayString)
        print("\n")

    # Algorítmo para executar o programa
    def begin(self):
        while True:
            self.updateWall()
            self.printScreen()

            print("Legenda: ")
            print("* = Pessoa")
            print("H = Porta")
            print("^ = Início")
            print("_ = Parede")

            print("\n**** Desafio do Muro ****")
            print("Escolha uma opção (somente número): ")
            print("1 - Executar algorítmo otimizado O(n)")
            print("2 - Executar algorítmo O(n²)")
            print("3 - Resetar posição da porta")
            print(f"""4 - Definir posição da porta (entre 0 e {self.wallSize - 1})""")
            print("5 - Sair")
            option = input()

            startDate = datetime.now()
            if option == "1":
                self.findDoorOptmized(self.personPosition, self.personPosition + 1, 1)
                pass
            elif option == "2":
                self.findDoor(self.personPosition, self.personPosition + 1, 1)
            elif option == "3":
                clear()
                self.generateWall()
                self.begin()
                break
            elif option == "4":
                clear()
                print("Digite a posição da porta")
                newPosition = int(input())
                if (
                    not isinstance(newPosition, int)
                    or newPosition < 0
                    or newPosition >= self.wallSize
                ):
                    print("Posição inválida")
                    self.begin()
                    break

                self.doorPosition = newPosition
                self.begin()
                break
            elif option == "5":
                break
            else:
                print("Comando inválido")
                continue

            dateDiff = datetime.now() - startDate

            print(
                f"""Porta encontrada em {dateDiff.seconds} segundos ({dateDiff.microseconds} microsegundos)"""
            )
            print(f"""Posição: {self.doorPosition}""")
            print(f"""Passos: {self.counter}""")
            print(
                f"""Distância: {abs(math.floor(self.wallSize / 2) - self.doorPosition)}"""
            )
            input()
            clear()


# para prevenir erros devido a demora de execução dos algorítmos
sys.setrecursionlimit(2000)

program = MainClass()
program.generateWall()
program.begin()
