from typing import List, Dict
from models.cookie_config import CookieConfig

class ResultPrinter:
    def __init__(self, config: CookieConfig):
        self.config = config

    def print_results(self, valid_combos: List[Dict], combinations_checked: int, time_taken: float) -> None:
        """Print results based on cookie type."""
        if not valid_combos:
            print("No valid combinations found!")
            return
            
        print(f"\nSearch completed in {time_taken:.2f} seconds")
        print(f"Total combinations checked: {combinations_checked}")
        print(f"Valid combinations found: {len(valid_combos)}")
        
        print("\nTop 5 Combinations:")
        print("=" * 80)
        
        for i, result in enumerate(valid_combos[:5], 1):
            combo = result['combo']
            stats = result['total_stats']
            
            # Print header for this combination
            print(f"\n{i}. {self._get_topping_description()}")
            
            # Print main stats
            for stat in self.config.relevant_stats:
                print(f"{stat}: {stats[stat]:.1f}")
            
            # Print detailed topping breakdown
            print("-" * 60)
            print(self._get_table_header())
            print("-" * 60)
            
            for topping in combo:
                print(self._format_topping_stats(topping))

    def _get_topping_description(self) -> str:
        """Get description of topping combination."""
        descriptions = {
            ('apple_jelly', 5): "5AJ Combination",
            ('chocolate', 5): "5SC Combination",
            ('almond', 5): "5SA Combination",
            ('raspberry', 5): "5SR Combination",
            ('raspberry', 3): "3SR + 2AJ Combination" if ('apple_jelly', 2) in self.config.topping_strategy else "3SR + 2SA Combination",
            ('chocolate', 3): "3SC + 2CA Combination",
        }
        
        for strategy, desc in descriptions.items():
            if strategy in self.config.topping_strategy:
                return desc
        return "Combination"

    def _get_table_header(self) -> str:
        """Get the table header based on relevant stats."""
        headers = {
            'ATK': 'ATK',
            'Cooldown': 'CD',
            'Crit': 'Crit',
            'ATK_SPD': 'ASPD',
            'DMG_Resist': 'DMR',
            'HP': 'HP'
        }
        
        header = "{'Type':<15}"
        for stat in self.config.relevant_stats:
            header += f"{headers[stat]:<8}"
            
        return eval(f"f'{header}'")

    def _format_topping_stats(self, topping: Dict) -> str:
        """Format a single topping's stats."""
        stats = f"{topping['type']:<15}"
        for stat in self.config.relevant_stats:
            stats += f"{topping.get(stat, 0):<8.1f}"
        return stats

    def _print_black_results(self, valid_combos: List[Dict]) -> None:
        """Print Black Sapphire specific results format."""
        print("\nTop 5 Combinations:")
        print("=" * 80)
        
        for i, result in enumerate(valid_combos[:5], 1):
            combo = result['combo']
            stats = result['total_stats']
            print(f"\n{i}. 5AJ Combination")
            print(f"Crit: {stats['Crit']:.1f}")
            print(f"ATK: {stats['ATK']:.1f}")
            print(f"CD: {stats['Cooldown']:.1f}")
            print("-" * 60)
            print(f"{'Type':<15}{'Crit':<8}{'ATK':<8}{'CD':<8}")
            print("-" * 60)
            for topping in combo:
                print(f"{topping['type']:<15}{topping.get('Crit', 0):<8.1f}"
                      f"{topping.get('ATK', 0):<8.1f}"
                      f"{topping.get('Cooldown', 0):<8.1f}")

    def _print_ferret_results(self, valid_combos: List[Dict]) -> None:
        """Print Ferret specific results format."""
        print("\nTop 5 Combinations:")
        print("=" * 80)
        
        for i, result in enumerate(valid_combos[:5], 1):
            combo = result['combo']
            stats = result['total_stats']
            print(f"\n{i}. 5SC Combination")
            print(f"CD: {stats['Cooldown']:.1f}")
            print(f"ATK_SPD: {stats['ATK_SPD']:.1f}")
            print("-" * 60)
            print(f"{'Type':<15}{'CD':<8}{'ASPD':<8}")
            print("-" * 60)
            for topping in combo:
                print(f"{topping['type']:<15}{topping.get('Cooldown', 0):<8.1f}"
                      f"{topping.get('ATK_SPD', 0):<8.1f}")

    def _print_default_results(self, valid_combos: List[Dict]) -> None:
        """Default print format for cookies without specific format."""
        print("\nTop 5 Combinations:")
        print("=" * 80)
        
        for i, result in enumerate(valid_combos[:5], 1):
            combo = result['combo']
            stats = result['total_stats']
            print(f"\n{i}. Combination")
            for stat in self.config.relevant_stats:
                print(f"{stat}: {stats[stat]:.1f}")
            print("-" * 60)
            print("Toppings:")
            for topping in combo:
                stat_str = " ".join(f"{stat}: {topping.get(stat, 0):.1f}" 
                                  for stat in self.config.relevant_stats)
                print(f"{topping['type']}: {stat_str}") 