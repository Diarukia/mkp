
class mkp:
    def __init__(self, cost, weight, restriccions):
        self.cost = cost 
        self.weight = weight
        self.restriccions = restriccions

    def calcule_fitness(self, objects):
        sum = 0
        for i in range(len(objects)):
            sum += objects[i]*self.cost[i]
        return sum

    def correct_knackpack(self, objects):
        sum = 0
        for i in range(len(self.restriccions)):
            for j in range(len(objects)):
                sum += self.weight[i][j]*objects[j]
            if(sum > self.restriccions[j]):
                return False
            sum = 0
        return True

    @staticmethod
    def create_mkps(file = None):
        with open("problem.txt",'r',encoding = 'utf-8') as f:
            problem = list( map(lambda x: x.rstrip(),f.read().split(" ")) )
            problem = list( map(lambda x: float(x), problem) )
            variables = int(problem[0])
            n_restriccions = int(problem[1])
            cost = list()

            for i in range(3, variables+3):
                cost.append(problem[i])
            
            weight = list()
            iterator = variables+3

            for i in range(n_restriccions):
                weight.append(list())
                for j in range(iterator, iterator+variables):
                    weight[i].append(problem[j])
                iterator = iterator+variables

            restriccions = list()
            for i in range(iterator, iterator+n_restriccions):
                restriccions.append(problem[i])

            return mkp(cost,weight,restriccions)