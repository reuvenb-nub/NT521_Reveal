from .graph import Graph


class Function:
    def __init__(self, function):
        self.name = function["function"]
        self.id = function["id"].split(".")[-1]
        self.indentation = 1
        '''name ast is misleading its the whole cpg'''
        self.ast = Graph(function, self.indentation)


    def __str__(self):
        indentation = self.indentation * "\t"
        return f"{indentation}Function Name: {self.name}\n{indentation}Id: {self.id}\n{indentation}AST:{self.ast}"

    def get_nodes(self):
        return self.ast.nodes

    def get_nodes_types(self):
        return self.ast.get_nodes_type()
