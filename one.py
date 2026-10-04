def objective_function(x):
    return -(x ** 2) + 4 * x

def hill_climbing(start_x, step_size, max_iterations):
    current_x = start_x
    current_val = objective_function(current_x)
    
    print(f"Initial State: x = {current_x:.4f}, f(x) = {current_val:.4f}")
    
    for iteration in range(1, max_iterations + 1):
        left_neighbor = current_x - step_size
        right_neighbor = current_x + step_size
        
        left_val = objective_function(left_neighbor)
        right_val = objective_function(right_neighbor)
        
        if left_val > current_val and left_val >= right_val:
            current_x = left_neighbor
            current_val = left_val
        elif right_val > current_val and right_val > left_val:
            current_x = right_neighbor
            current_val = right_val
        else:
            print(f"Terminated at local peak at iteration {iteration}")
            break
            
        print(f"Iteration {iteration}: x = {current_x:.4f}, f(x) = {current_val:.4f}")
        
    return current_x, current_val

def main():
    print("Hill Climbing Algorithm for Maximum of Objective Function: F(x) = -x^2 + 4x")
    start_point = 0.0
    step = 0.05
    max_iters = 100
    
    peak_x, max_val = hill_climbing(start_point, step, max_iters)
    print("Optimization Completed:")
    print(f"Optimal x: {peak_x:.4f}")
    print(f"Maximum Function Value: {max_val:.4f}")

if __name__ == '__main__':
    main()
