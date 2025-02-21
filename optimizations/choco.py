from configs.choco_config import CHOCO_CONFIG
from utils.topping_optimizer import ToppingOptimizer
from utils.result_printer import ResultPrinter
import time

def main():
    toppings = [
        # Your toppings list here
    ]
    
    optimizer = ToppingOptimizer(CHOCO_CONFIG)
    printer = ResultPrinter(CHOCO_CONFIG)
    
    start_time = time.time()
    filtered_toppings = optimizer.preprocess_toppings(toppings)
    valid_combos, combinations_checked = optimizer.find_valid_combinations(filtered_toppings)
    end_time = time.time()
    
    printer.print_results(valid_combos, combinations_checked, end_time - start_time)

if __name__ == "__main__":
    main() 