from Problem.mkp import mkp
from Metaheuritics.simulated_annealing import Simulated_annealing
if __name__ == '__main__':
    problem = mkp.create_mkps()
    sa = Simulated_annealing(0.9,100,0.1)
    hola =  sa.run_algorithm(problem)
    print(hola)
    print( problem.calcule_fitness( hola ) )

