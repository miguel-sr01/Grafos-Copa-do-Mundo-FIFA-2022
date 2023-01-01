import igraph as ig
import matplotlib.pyplot as plt
import cairo

def menu_geral():
    print("Selecione uma etapa da Copa do Mundo FIFA 2022:")
    print("1 - FASE DE GRUPOS")
    print("2 - OITAVAS DE FINAL")
    print("3 - QUARTAS DE FINAL")
    print("4 - SEMI FINAL")
    print("5 - FINAL")
    print("0 - Encerrar Programa")

def menu():
    print("Selecione um grupo da Copa do Mundo FIFA 2022:")
    print("1 - GRUPO A")
    print("2 - GRUPO B")
    print("3 - GRUPO C")
    print("4 - GRUPO D")
    print("5 - GRUPO E")
    print("6 - GRUPO F")
    print("7 - GRUPO G")
    print("8 - GRUPO H")
    print("0 - Encerrar Programa")



class grafo_fase_de_grupos():
    def __init__(self, t1, t2, t3, t4, grupo):

        self.grupo = grupo
        self.g = ig.Graph([(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)])
        self.g.vs["name"] = [t1, t2, t3, t4]
        self.g.vs["pass"] = ["t", "t", "f", "f", "f"]
        layout = self.g.layout("kk")
        fig, ax = plt.subplots()
        self.g.vs["label"] = self.g.vs["name"]
        color_dict = {"t": "green", "f": "red"}
        self.g.vs["color"] = [color_dict[value] for value in self.g.vs["pass"]]

        self.g.es[0]["color"] = "orange"
        self.g.es[1]["color"] = "purple"
        self.g.es[2]["color"] = "blue"
        self.g.es[3]["color"] = "blue"
        self.g.es[4]["color"] = "purple"
        self.g.es[5]["color"] = "orange"

        ig.plot(self.g, layout=layout, bbox=(300, 300), margin=20)
        ig.plot(self.g, layout=layout, bbox=(300, 300), margin=20, target=ax) 

        ig.plot(self.g, layout=layout)

        string = "COPA DO MUNDO FIFA 2022 - GRUPO "+ grupo

        plt.title(string)
        plt.show()


class grafo_oitavas_de_final():
    def __init__(self, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16):

        self.g = ig.Graph([(0,1), (2,3), (4,5), (6,7), (8,9), (10,11), (12,13), (14,15)])
        self.g.vs["name"] = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16]
        self.g.vs["pass"] = ["t", "f", "t", "f", "f","t", "t", "f", "t", "f", "t","f", "t", "f", "t", "f"]
        layout = self.g.layout("kk")
        fig, ax = plt.subplots()
        self.g.vs["label"] = self.g.vs["name"]
        color_dict = {"t": "green", "f": "red"}
        self.g.vs["color"] = [color_dict[value] for value in self.g.vs["pass"]]

        self.g.es["color"] = "black"


        ig.plot(self.g, layout=layout, bbox=(300, 300), margin=20)
        ig.plot(self.g, layout=layout, bbox=(300, 300), margin=20, target=ax) 

        ig.plot(self.g, layout=layout)

        string = "COPA DO MUNDO FIFA 2022 - OITAVAS DE FINAL"

        plt.title(string)
        plt.show()
    
class grafo_quartas_de_final():
    def __init__(self, t1, t2, t3, t4, t5, t6, t7, t8):

        self.g = ig.Graph([(0,1), (2,3), (4,5), (6,7)])
        self.g.vs["name"] = [t1, t2, t3, t4, t5, t6, t7, t8]
        self.g.vs["pass"] = ["f", "t", "t", "f", "f","t", "t", "f", "t", "f", "t","f", "t", "f", "t", "f"]
        layout = self.g.layout("kk")
        fig, ax = plt.subplots()
        self.g.vs["label"] = self.g.vs["name"]
        color_dict = {"t": "green", "f": "red"}
        self.g.vs["color"] = [color_dict[value] for value in self.g.vs["pass"]]

        self.g.es["color"] = "black"


        ig.plot(self.g, layout=layout, bbox=(300, 300), margin=20)
        ig.plot(self.g, layout=layout, bbox=(300, 300), margin=20, target=ax) 

        ig.plot(self.g, layout=layout)

        string = "COPA DO MUNDO FIFA 2022 - OITAVAS DE FINAL"

        plt.title(string)
        plt.show()


def fase_de_grupos():
    menu()
    opcao = -1
    while opcao != 0:
        opcao = int(input("\nOpção: "))
        match opcao:
            case 1:
                grafo_fase_de_grupos("HOLANDA", "SENEGAL", "EQUADOR", "CATAR", "A")
            case 2:
                grafo_fase_de_grupos("INGLATERRA", "EUA", "IRÃ", "PAÍS DE GALES", "B")
            case 3:
                grafo_fase_de_grupos("ARGENTINA", "POLÔNIA", "MEXICO", "ARÁBIA SAUDITA", "C")
            case 4:
                grafo_fase_de_grupos("FRANÇA", "AUSTRÁLIA", "TUNÍSIA", "DINAMARCA", "D")
            case 5:
                grafo_fase_de_grupos("JAPÃO", "ESPANHA", "ALEMANHA", "COSTA RICA", "E")
            case 6:
                grafo_fase_de_grupos("MARROCOS", "CROÁCIA", "BÉLGICA", "CANADÁ", "F")
            case 7:
                grafo_fase_de_grupos("BRASIL", "SUIÇA", "CAMARÕES", "SÉRVIA", "G")
            case 8:
                grafo_fase_de_grupos("PORTUGAL", "COREIA DO SUL", "URUGUAI", "GANA", "H")
            case 0:
                break

def oitavas_de_final():
    grafo_oitavas_de_final("HOLANDA", "EUA", "ARGENTINA", "AUSTRÁLIA", "JAPÃO", "CROÁCIA", "BRASIL", "COREIA DO SUL", "INGLATERRA", "SENEGAL", "FRANÇA", "POLÔNIA", "MARROCOS", "ESPANHA", "PORTUGAL", "SUIÇA")

def quartas_de_final():
    grafo_quartas_de_final("HOLANDA", "ARGENTINA", "CROÁCIA", "BRASIL", "INGLATERRA", "FRANÇA", "MARROCOS", "PORTUGAL")


def main():
    menu_geral()
    opcao_geral = -1
    opcao_geral = int(input("\nOpção: "))
    match opcao_geral:
        case 1:
            fase_de_grupos()
        case 2:
            oitavas_de_final()
        case 3:
            quartas_de_final()

if __name__ == '__main__':
   main()