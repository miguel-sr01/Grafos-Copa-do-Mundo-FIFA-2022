import igraph as ig
import matplotlib.pyplot as plt

def menu_geral():
    print("\n\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Selecione uma etapa da Copa do Mundo FIFA 2022:")
    print("1 - FASE DE GRUPOS")
    print("2 - OITAVAS DE FINAL")
    print("3 - QUARTAS DE FINAL")
    print("4 - SEMI FINAL")
    print("5 - FINAL")
    print("6 - TERCEIRO LUGAR")
    print("7 - MATA-MATA DA COPA")
    print("0 - Encerrar Programa")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

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
    print("0 - Voltar para Menu Geral")

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

        if grupo == 'A' or grupo == 'D' or grupo == 'G':
            self.g.es[0]["color"] = "orange"
            self.g.es[1]["color"] = "purple"
            self.g.es[2]["color"] = "blue"
            self.g.es[3]["color"] = "blue"
            self.g.es[4]["color"] = "purple"
            self.g.es[5]["color"] = "orange"
        elif grupo == 'B' or grupo == 'E' or grupo == 'H':
            self.g.es[0]["color"] = "black"
            self.g.es[1]["color"] = "blue"
            self.g.es[2]["color"] = "brown"
            self.g.es[3]["color"] = "brown"
            self.g.es[4]["color"] = "blue"
            self.g.es[5]["color"] = "black"

        else:                      
            self.g.es[0]["color"] = "yellow"
            self.g.es[1]["color"] = "red"
            self.g.es[2]["color"] = "green"
            self.g.es[3]["color"] = "green"
            self.g.es[4]["color"] = "red"
            self.g.es[5]["color"] = "yellow"


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
        self.g.vs["pass"] = ["f", "t", "t", "f", "f","t", "t", "f"]
        layout = self.g.layout("kk")
        fig, ax = plt.subplots()
        self.g.vs["label"] = self.g.vs["name"]
        color_dict = {"t": "green", "f": "red"}
        self.g.vs["color"] = [color_dict[value] for value in self.g.vs["pass"]]

        self.g.es["color"] = "black"


        ig.plot(self.g, layout=layout, bbox=(300, 300), margin=20)
        ig.plot(self.g, layout=layout, bbox=(300, 300), margin=20, target=ax) 

        ig.plot(self.g, layout=layout)

        string = "COPA DO MUNDO FIFA 2022 - QUARTAS DE FINAL"

        plt.title(string)
        plt.show()

class grafo_semi_final():
    def __init__(self, t1, t2, t3, t4):

        self.g = ig.Graph([(0,1), (2,3)])
        self.g.vs["name"] = [t1, t2, t3, t4]
        self.g.vs["pass"] = ["t", "f", "t", "f"]
        layout = self.g.layout("kk")
        fig, ax = plt.subplots()
        self.g.vs["label"] = self.g.vs["name"]
        color_dict = {"t": "green", "f": "red"}
        self.g.vs["color"] = [color_dict[value] for value in self.g.vs["pass"]]

        self.g.es["color"] = "black"


        ig.plot(self.g, layout=layout, bbox=(300, 300), margin=20)
        ig.plot(self.g, layout=layout, bbox=(300, 300), margin=20, target=ax) 

        ig.plot(self.g, layout=layout)

        string = "COPA DO MUNDO FIFA 2022 - SEMI FINAL"

        plt.title(string)
        plt.show()

class grafo_final():
    def __init__(self, t1, t2):

        self.g = ig.Graph([(0,1)])
        self.g.vs["name"] = [t1, t2]
        self.g.vs["pass"] = ["f", "t"]
        layout = self.g.layout("kk")
        fig, ax = plt.subplots()
        self.g.vs["label"] = self.g.vs["name"]
        color_dict = {"t": "green", "f": "red"}
        self.g.vs["color"] = [color_dict[value] for value in self.g.vs["pass"]]

        self.g.es["color"] = "black"


        ig.plot(self.g, layout=layout, bbox=(300, 300), margin=20)
        ig.plot(self.g, layout=layout, bbox=(300, 300), margin=20, target=ax) 

        ig.plot(self.g, layout=layout)

        string = "COPA DO MUNDO FIFA 2022 - FINAL \n  Argentina 3 (4x2) 3 França"

        plt.title(string)
        plt.show()

class grafo_terceiro_lugar():
    def __init__(self, t1, t2):

        self.g = ig.Graph([(0,1)])
        self.g.vs["name"] = [t1, t2]
        self.g.vs["pass"] = ["f", "t"]
        layout = self.g.layout("kk")
        fig, ax = plt.subplots()
        self.g.vs["label"] = self.g.vs["name"]
        color_dict = {"t": "green", "f": "red"}
        self.g.vs["color"] = [color_dict[value] for value in self.g.vs["pass"]]

        self.g.es["color"] = "black"


        ig.plot(self.g, layout=layout, bbox=(300, 300), margin=20)
        ig.plot(self.g, layout=layout, bbox=(300, 300), margin=20, target=ax) 

        ig.plot(self.g, layout=layout)

        string = "COPA DO MUNDO FIFA 2022 - TERCEIRO LUGAR \n  Croácia 2 X 1 Marrocos"

        plt.title(string)
        plt.show()

class digrafo_mata_mata():
    def __init__(self, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16):

        self.g = ig.Graph(directed=True)
        self.g.add_vertices(16)
        self.g.add_edges([(1,0), (0,2), (3,2), (5,2), (12,5), (4,5), (6,5), (10,2), (7,6), (9,8), (11,10), (12,10), (13,12), (15,14), (8,10), (14,12)])

        self.g.vs["name"] = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16]
        layout = self.g.layout("kk")
        fig, ax = plt.subplots()
        self.g.vs["label"] = self.g.vs["name"]

        self.g.vs["color"] = "gray"

        self.g.es[0]["color"] = "green"
        self.g.es[1]["color"] = "blue"
        self.g.es[2]["color"] = "green"
        self.g.es[3]["color"] = "red"
        self.g.es[4]["color"] = "purple"
        self.g.es[5]["color"] = "green"
        self.g.es[6]["color"] = "blue"
        self.g.es[7]["color"] = "purple"
        self.g.es[8]["color"] = "green"
        self.g.es[9]["color"] = "green"
        self.g.es[10]["color"] = "green"
        self.g.es[11]["color"] = "red"
        self.g.es[12]["color"] = "green"
        self.g.es[13]["color"] = "green"
        self.g.es[14]["color"] = "blue"
        self.g.es[15]["color"] = "blue"



        ig.plot(self.g, layout=layout, bbox=(300, 300), margin=20)
        ig.plot(self.g, layout=layout, bbox=(300, 300), margin=20, target=ax) 

        ig.plot(self.g, layout=layout)

        string = "COPA DO MUNDO FIFA 2022 - MATA-MATA"

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
                menu_geral()
                break

def oitavas_de_final():
    grafo_oitavas_de_final("HOLANDA", "EUA", "ARGENTINA", "AUSTRÁLIA", "JAPÃO", "CROÁCIA", "BRASIL", "COREIA DO SUL", "INGLATERRA", "SENEGAL", "FRANÇA", "POLÔNIA", "MARROCOS", "ESPANHA", "PORTUGAL", "SUIÇA")

def quartas_de_final():
    grafo_quartas_de_final("HOLANDA", "ARGENTINA", "CROÁCIA", "BRASIL", "INGLATERRA", "FRANÇA", "MARROCOS", "PORTUGAL")

def semi_final():
    grafo_semi_final("ARGENTINA", "CROÁCIA", "FRANÇA", "MARROCOS")

def terceiro_lugar():
    grafo_terceiro_lugar("MARROCOS", "CROÁCIA")

def final():
    grafo_final("FRANÇA", "ARGENTINA")

def mata_mata():
    digrafo_mata_mata("HOLANDA", "EUA", "ARGENTINA", "AUSTRÁLIA", "JAPÃO", "CROÁCIA", "BRASIL", "COREIA DO SUL", "INGLATERRA", "SENEGAL", "FRANÇA", "POLÔNIA", "MARROCOS", "ESPANHA", "PORTUGAL", "SUIÇA")

def main():
    menu_geral()
    opcao_geral = -1
    while opcao_geral != 0:
        opcao_geral = int(input("\nOpção Geral: "))
        match opcao_geral:
            case 1:
                fase_de_grupos()
            case 2:
                oitavas_de_final()
            case 3:
                quartas_de_final()
            case 4:
                semi_final()
            case 5:
                final()
            case 6:
                terceiro_lugar()
            case 7:
                mata_mata()
            case 0:
                break

if __name__ == '__main__':
   main()