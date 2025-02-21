from typing import List, Dict, Tuple
from itertools import combinations
import time
from models.cookie_config import CookieConfig

class ToppingOptimizer:
    def __init__(self, config: CookieConfig):
        self.config = config
        
    def preprocess_toppings(self, toppings: List[Dict]) -> List[Dict]:
        """Filter toppings based on cookie's relevant stats requirements."""
        filtered_toppings = []
        discarded_toppings = []
        
        print(f"\nPreprocessing Toppings for {self.config.name}:")
        print("-" * 50)
        print(f"Starting with {len(toppings)} total toppings")
        
        for topping in toppings:
            relevant_count = sum(1 for stat in self.config.relevant_stats 
                               if topping.get(stat, 0) > 0)
            
            if relevant_count >= self.config.min_relevant_stats:
                filtered_toppings.append(topping)
            else:
                discarded_toppings.append((topping, relevant_count))
        
        self._print_preprocessing_summary(filtered_toppings, toppings)
        return filtered_toppings
    
    def find_valid_combinations(self, toppings: List[Dict]) -> Tuple[List[Dict], int]:
        """Find valid combinations based on cookie's requirements."""
        toppings_by_type = self._group_toppings(toppings)
        valid_combos = []
        combinations_checked = 0
        
        # Generate all possible combinations based on strategy
        for combo in self._generate_combinations(toppings_by_type):
            combinations_checked += 1
            
            # Calculate total stats
            total_stats = self._calculate_total_stats(combo)
            
            # Check if combination meets requirements
            if self._is_valid_combination(total_stats):
                valid_combos.append({
                    'combo': combo,
                    'total_stats': total_stats
                })
                
        # Sort based on cookie's priorities
        valid_combos.sort(key=self._get_sort_key, reverse=True)
        
        return valid_combos, combinations_checked
    
    def _is_valid_combination(self, total_stats: Dict[str, float]) -> bool:
        """Check if stats meet cookie's requirements."""
        for stat, requirement in self.config.required_stats.items():
            if isinstance(requirement, tuple):
                min_val, max_val = requirement
                if not (min_val <= total_stats[stat] <= max_val):
                    return False
            elif total_stats[stat] < requirement:
                return False
        return True 

    def _print_preprocessing_summary(self, filtered_toppings: List[Dict], original_toppings: List[Dict]) -> None:
        """Print summary of preprocessing results by topping type."""
        # Count toppings by type for filtered and original
        filtered_by_type = {}
        original_by_type = {}
        
        for topping in filtered_toppings:
            topping_type = topping['type']
            filtered_by_type[topping_type] = filtered_by_type.get(topping_type, 0) + 1
            
        for topping in original_toppings:
            topping_type = topping['type']
            original_by_type[topping_type] = original_by_type.get(topping_type, 0) + 1
        
        # Print summary for each type
        for topping_type in original_by_type:
            kept = filtered_by_type.get(topping_type, 0)
            total = original_by_type[topping_type]
            print(f"{topping_type} toppings kept: {kept}/{total}")
        
        print(f"Total toppings kept: {len(filtered_toppings)}/{len(original_toppings)}") 

    def _group_toppings(self, toppings: List[Dict]) -> List[Dict]:
        """Group toppings by their type."""
        return [t for t in toppings if t['type'] in 
                [strategy[0] for strategy in self.config.topping_strategy]]

    def _generate_combinations(self, toppings_by_type: List[Dict]) -> List[List[Dict]]:
        """Generate combinations based on cookie's strategy."""
        all_combos = []
        
        for topping_type, count in self.config.topping_strategy:
            type_toppings = [t for t in toppings_by_type if t['type'] == topping_type]
            type_combos = list(combinations(type_toppings, count))
            if not all_combos:
                all_combos = [[*combo] for combo in type_combos]
            else:
                new_combos = []
                for existing_combo in all_combos:
                    for new_combo in type_combos:
                        new_combos.append(existing_combo + [*new_combo])
                all_combos = new_combos
        
        return all_combos

    def _calculate_total_stats(self, combo: List[Dict]) -> Dict[str, float]:
        """Calculate total stats for a combination."""
        total_stats = self.config.base_stats.copy()
        
        for topping in combo:
            for stat in self.config.relevant_stats:
                total_stats[stat] = total_stats.get(stat, 0) + topping.get(stat, 0)
        
        return total_stats

    def _get_sort_key(self, combo: Dict) -> tuple:
        """Get the sorting key based on cookie's requirements."""
        stats = combo['total_stats']
        
        if self.config.name == "Black Sapphire":
            # Sort by Crit first, then ATK
            return (
                round(stats['Crit'], 1),
                round(stats['ATK'], 1)
            )
        
        # Default sorting (can be expanded for other cookies)
        return tuple(stats[stat] for stat in self.config.relevant_stats) 