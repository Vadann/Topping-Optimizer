from configs.rebel_config import REBEL_CONFIG
from utils.topping_optimizer import ToppingOptimizer
from utils.result_printer import ResultPrinter
import time
import io
import sys

def main(toppings=None):
    if toppings is None:
        toppings = []
    
    optimizer = ToppingOptimizer(REBEL_CONFIG)
    printer = ResultPrinter(REBEL_CONFIG)
    
    start_time = time.time()
    filtered_toppings = optimizer.preprocess_toppings(toppings)
    valid_combos, combinations_checked = optimizer.find_valid_combinations(filtered_toppings)
    end_time = time.time()
    
    # Capture the output instead of printing directly
    output = io.StringIO()
    sys.stdout = output
    
    printer.print_results(valid_combos, combinations_checked, end_time - start_time)
    
    # Restore stdout and return the captured output
    sys.stdout = sys.__stdout__
    return output.getvalue()

if __name__ == "__main__":
    main() 