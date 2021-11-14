import random
import math

class Simulated_annealing:
    def __init__(self, alpha, init_t, final_t):
        self.alpha = alpha
        self.init_t = init_t
        self.final_t = final_t
        self.best = [0,0,0,0,0,0,0,0,0,0]

    def run_algorithm(self, problem):
        solution = [0,0,0,0,0,0,0,0,0,0]
        while(self.init_t > self.final_t):
            solution = self.accept_criteria( problem,solution,self.new_solution(solution, problem) )
            if( problem.calcule_fitness(self.best) <  problem.calcule_fitness(solution)):
                self.best = solution
            self.init_t = self.init_t*self.alpha
        return self.best

    def accept_criteria(self, problem, best_solution, new_solution):
        if(-1*problem.calcule_fitness(best_solution) < problem.calcule_fitness(new_solution)):
            return new_solution
        elif( math.exp((-1*(problem.calcule_fitness(best_solution)-problem.calcule_fitness(new_solution)) )/self.init_t) < random.uniform(0, 1)):
            return  new_solution
        return best_solution
    
    def new_solution(self, solution, problem):
        new_solution = solution.copy()
        while(True):
            if(new_solution[random.randint(0, len(new_solution)-1)] == 1):
                new_solution[random.randint(0, len(new_solution)-1)] = 0
            else:
                new_solution[random.randint(0, len(new_solution)-1)] = 1
            
            if( problem.correct_knackpack(new_solution) == True ):
                break
        return new_solution

            
            