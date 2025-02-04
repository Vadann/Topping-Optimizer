from itertools import combinations
import time

def find_all_valid_combos(chocolate_toppings, caramel_toppings):
    """Find ALL valid combinations for Pinecone."""
    # Base stats
    base_aspd = 46.3 - 3.4
    base_cd = 3
    
    # Requirements
    aspd_range = (57.6, 57.8)  # Very specific ASPD range
    min_cd = 15
    
    valid_combos = []
    close_combos = []
    combinations_checked = 0
    
    print(f"\nChecking all combinations of:")
    print(f"Chocolate toppings: {len(chocolate_toppings)}")
    print(f"Caramel toppings: {len(caramel_toppings)}")
    
    # Strategy: 4 Caramel + 1 Chocolate
    print("\nChecking Strategy: 4 Caramel + 1 Chocolate")
    for caramel_combo in combinations(caramel_toppings, 4):
        for choc in chocolate_toppings:
            combinations_checked += 1
            combo = list(caramel_combo) + [choc]
            
            total_cd = base_cd + sum(t.get('Cooldown', 0) for t in combo)
            total_aspd = base_aspd + sum(t.get('ATK_SPD', 0) for t in combo)
            total_crit = sum(t.get('Crit', 0) for t in combo)
            
            result = {
                'strategy': '4CA1C',
                'combo': combo,
                'total_cd': total_cd,
                'total_aspd': total_aspd,
                'total_crit': total_crit,
                'missing': []
            }
            
            # Check requirements
            if total_aspd < aspd_range[0]:
                result['missing'].append(f'ASPD too low: {total_aspd:.1f}/{aspd_range[0]}')
            elif total_aspd > aspd_range[1]:
                result['missing'].append(f'ASPD too high: {total_aspd:.1f}/{aspd_range[1]}')
            if total_cd < min_cd:
                result['missing'].append(f'CD too low: {total_cd:.1f}/{min_cd}')
            
            if not result['missing']:
                valid_combos.append(result)
            else:
                close_combos.append(result)
            
            if combinations_checked % 1000 == 0:
                print(f"Checked {combinations_checked} combinations...")
    
    # Sort valid combinations
    valid_combos.sort(key=lambda x: (
        abs((aspd_range[0] + aspd_range[1])/2 - x['total_aspd']),  # Closest to middle of ASPD range
        -x['total_cd'],                                            # Higher CD
        -x['total_crit']                                          # Higher Crit as bonus
    ))
    
    # Sort close combinations
    if not valid_combos and close_combos:
        close_combos.sort(key=lambda x: (
            len(x['missing']),                                    # Fewer missing requirements
            abs((aspd_range[0] + aspd_range[1])/2 - x['total_aspd']),  # Closest to target ASPD
            abs(x['total_cd'] - min_cd)                          # Closest to min CD
        ))
    
    return valid_combos, close_combos, combinations_checked

def preprocess_toppings(toppings, min_relevant_stats=2):
    """Filter toppings based on relevance to ATK_SPD and Cooldown."""
    relevant_stats = ['ATK_SPD', 'Cooldown']
    filtered_toppings = []
    discarded_toppings = []
    
    print("\nPreprocessing Toppings:")
    print("-" * 50)
    print(f"Starting with {len(toppings)} total toppings")
    
    for topping in toppings:
        relevant_count = sum(1 for stat in relevant_stats if topping.get(stat, 0) > 0)
        if relevant_count >= min_relevant_stats:
            filtered_toppings.append(topping)
        else:
            discarded_toppings.append((topping, relevant_count))
    
    choc_kept = len([t for t in filtered_toppings if t['type'] == 'chocolate'])
    caramel_kept = len([t for t in filtered_toppings if t['type'] == 'caramel'])
    choc_total = len([t for t in toppings if t['type'] == 'chocolate'])
    caramel_total = len([t for t in toppings if t['type'] == 'caramel'])
    
    print(f"\nDiscarded {len(discarded_toppings)} toppings with fewer than {min_relevant_stats} relevant stats")
    print(f"Chocolate toppings kept: {choc_kept}/{choc_total}")
    print(f"Caramel toppings kept: {caramel_kept}/{caramel_total}")
    print(f"Total toppings kept: {len(filtered_toppings)}/{len(toppings)}")
    
    return filtered_toppings

def print_detailed_results(valid_combos, close_combos, combinations_checked, time_taken):
    """Print detailed analysis of all combinations."""
    print(f"\nSearch completed in {time_taken:.2f} seconds")
    print(f"Total combinations checked: {combinations_checked}")
    print(f"Valid combinations found: {len(valid_combos)}")
    
    if valid_combos:
        print("\nTop 5 Valid Combinations:")
        print("=" * 80)
        for i, result in enumerate(valid_combos[:5], 1):
            print_combo(i, result)
    else:
        print("\nNo valid combinations found. Showing closest matches:")
        print("=" * 80)
        for i, result in enumerate(close_combos[:5], 1):
            print_combo(i, result)
            print(f"Missing requirements: {', '.join(result['missing'])}")

def print_combo(index, result):
    """Helper function to print a single combination."""
    combo = result['combo']
    print(f"\n{index}. {result['strategy']} Combination")
    print(f"ASPD: {result['total_aspd']:.1f}")
    print(f"CD: {result['total_cd']:.1f}")
    print(f"Crit: {result['total_crit']:.1f}")
    print("-" * 50)
    print(f"{'Type':<12}{'ASPD':<8}{'CD':<8}{'Crit':<8}")
    print("-" * 50)
    for topping in combo:
        print(f"{topping['type']:<12}{topping.get('ATK_SPD', 0):<8.1f}"
              f"{topping.get('Cooldown', 0):<8.1f}{topping.get('Crit', 0):<8.1f}")

if __name__ == "__main__":
    # Your toppings list here
    toppings = [
        {'type': 'caramel', 'ATK': 2.0, 'ATK_SPD': 2.9, 'Crit': 2.4, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 2.6, 'Crit': 2.4, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 2.4, 'ATK_SPD': 0.0, 'Crit': 2.5, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.6, 'Cooldown': 1.4, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 2.8, 'Crit': 2.4, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 1.6, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 1.9, 'DMG_Resist': 4.0},
    {'type': 'caramel', 'ATK': 1.8, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 1.4, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 1.2, 'ATK_SPD': 0.0, 'Crit': 2.7, 'Cooldown': 0.0, 'DMG_Resist': 4.3},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 4.2},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.7, 'Cooldown': 2.0, 'DMG_Resist': 4.1},
    {'type': 'caramel', 'ATK': 1.9, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.5},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 2.8, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.4},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 2.6, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 1.9, 'ATK_SPD': 2.6, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 2.6, 'Crit': 2.1, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 2.6, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 2.6, 'ATK_SPD': 2.3, 'Crit': 1.4, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 2.1, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 2.5, 'ATK_SPD': 2.1, 'Crit': 2.6, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 1.8, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 1.6, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 2.2},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 3.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 1.2, 'ATK_SPD': 0.0, 'Crit': 2.6, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 1.2},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 1.1, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 3.3},
    {'type': 'caramel', 'ATK': 2.7, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.4, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 1.2, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.1, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 1.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 1.2, 'ATK_SPD': 0.0, 'Crit': 1.2, 'Cooldown': 0.0, 'DMG_Resist': 5.9},
    {'type': 'caramel', 'ATK': 2.1, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.5},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 2.1, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.3},
    {'type': 'caramel', 'ATK': 1.1, 'ATK_SPD': 0.0, 'Crit': 2.1, 'Cooldown': 0.0, 'DMG_Resist': 5.2},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.4, 'DMG_Resist': 5.2},
    {'type': 'caramel', 'ATK': 1.5, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 2.6, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 2.3},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 1.2, 'ATK_SPD': 2.3, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.9},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 2.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 1.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.1},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 1.8, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 2.3},
    {'type': 'caramel', 'ATK': 2.1, 'ATK_SPD': 0.0, 'Crit': 2.4, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.1, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 1.5, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 1.5, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 2.8, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 1.4},
    {'type': 'caramel', 'ATK': 2.7, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.3},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.7, 'Cooldown': 1.2, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 1.3, 'DMG_Resist': 0.0},
    {'type': 'caramel', 'ATK': 0.0, 'ATK_SPD': 2.2, 'Crit': 0.0, 'Cooldown': 1.3, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 3.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 1.0},
        {'type': 'chocolate', 'ATK': 2.1, 'ATK_SPD': 0.0, 'Crit': 1.7, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 2.6, 'ATK_SPD': 2.8, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 2.2, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.7, 'Crit': 2.1, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.3, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.2, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.7},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 3.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.6, 'Cooldown': 0.0, 'DMG_Resist': 5.2},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.6, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.1, 'Crit': 2.1, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 2.4, 'ATK_SPD': 2.7, 'Crit': 2.1, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 3.0, 'ATK_SPD': 0.0, 'Crit': 2.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.9, 'Cooldown': 0.0, 'DMG_Resist': 4.0},
        {'type': 'chocolate', 'ATK': 2.9, 'ATK_SPD': 1.2, 'Crit': 1.8, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 2.9, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 1.4},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 2.0, 'ATK_SPD': 1.2, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 3.2},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.9, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 2.2},
        {'type': 'chocolate', 'ATK': 2.6, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.7, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 4.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 2.3},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.0, 'Crit': 0.0, 'Cooldown': 1.4, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 1.3, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 1.1, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 1.4, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 6.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 1.0, 'DMG_Resist': 2.6},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 2.9, 'ATK_SPD': 0.0, 'Crit': 2.7, 'Cooldown': 0.0, 'DMG_Resist': 5.7},
        {'type': 'chocolate', 'ATK': 2.9, 'ATK_SPD': 0.0, 'Crit': 1.1, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 2.7, 'ATK_SPD': 3.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 2.6, 'ATK_SPD': 2.3, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.7},
        {'type': 'chocolate', 'ATK': 2.6, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.6},
        {'type': 'chocolate', 'ATK': 2.5, 'ATK_SPD': 2.1, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 2.5, 'ATK_SPD': 1.2, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 2.5, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 2.1},
        {'type': 'chocolate', 'ATK': 2.4, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 2.4, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 2.3, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.1, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 2.3, 'ATK_SPD': 2.1, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 1.7},
        {'type': 'chocolate', 'ATK': 1.5, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 1.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 2.9, 'ATK_SPD': 3.0, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 1.2, 'ATK_SPD': 2.8, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.6, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 5.0},
        {'type': 'chocolate', 'ATK': 2.6, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 2.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.4},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 1.2, 'DMG_Resist': 3.1},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 1.7, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.0, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.1, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 1.3},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 3.0, 'Cooldown': 0.0, 'DMG_Resist': 2.1},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 3.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 2.9, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 4.9},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.8, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.1, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 1.6, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.7, 'Crit': 2.7, 'Cooldown': 1.2, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.1, 'Crit': 2.6, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 1.7, 'ATK_SPD': 0.0, 'Crit': 2.6, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 1.1, 'ATK_SPD': 1.7, 'Crit': 2.5, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 1.6, 'ATK_SPD': 0.0, 'Crit': 2.4, 'Cooldown': 0.0, 'DMG_Resist': 3.1},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.8, 'Crit': 2.3, 'Cooldown': 0.0, 'DMG_Resist': 4.8},
        {'type': 'chocolate', 'ATK': 1.9, 'ATK_SPD': 0.0, 'Crit': 2.2, 'Cooldown': 0.0, 'DMG_Resist': 3.3},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 4.7},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 1.1, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 3.5},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.6, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.3, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.3, 'Crit': 1.1, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.2, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.0, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.6, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.0, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.8, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 1.9, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 1.3, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 5.5},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.7, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.7, 'Cooldown': 1.6, 'DMG_Resist': 1.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 5.7},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.6, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.2, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 1.5, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 2.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.8, 'Cooldown': 1.4, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.4, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.6, 'Cooldown': 1.3, 'DMG_Resist': 2.2},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.3, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.3, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.2, 'DMG_Resist': 5.5},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.2, 'DMG_Resist': 4.4},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 1.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.0, 'Cooldown': 0.0, 'DMG_Resist': 6.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.9},
        {'type': 'chocolate', 'ATK': 1.8, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.1, 'DMG_Resist': 5.8},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 5.8},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.8, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.7},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.4},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.0, 'Cooldown': 0.0, 'DMG_Resist': 5.4},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.1, 'DMG_Resist': 5.3},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 1.1, 'DMG_Resist': 5.3},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.2},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.1},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.7},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.8, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.7},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 4.7},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.6},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.3, 'Cooldown': 0.0, 'DMG_Resist': 4.5},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.2, 'Crit': 0.0, 'Cooldown': 1.4, 'DMG_Resist': 4.5},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.4},
        {'type': 'chocolate', 'ATK': 1.6, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.4},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.4, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 4.3},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.3},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.2},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.1},
        {'type': 'chocolate', 'ATK': 1.6, 'ATK_SPD': 2.2, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.1},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.0, 'DMG_Resist': 4.0},
        {'type': 'chocolate', 'ATK': 1.4, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.0},
        {'type': 'chocolate', 'ATK': 1.8, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.9},
        {'type': 'chocolate', 'ATK': 1.2, 'ATK_SPD': 0.0, 'Crit': 1.3, 'Cooldown': 0.0, 'DMG_Resist': 3.7},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 2.2, 'Cooldown': 0.0, 'DMG_Resist': 3.5},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.5},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.1, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.3},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 3.2},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.0, 'Cooldown': 0.0, 'DMG_Resist': 3.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 3.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 2.9},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 2.3},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 2.3},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.8, 'Cooldown': 0.0, 'DMG_Resist': 2.2},
        {'type': 'chocolate', 'ATK': 1.9, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 1.9},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.2, 'DMG_Resist': 1.3},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 1.2},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.1, 'DMG_Resist': 1.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 1.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.8, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 2.9, 'ATK_SPD': 1.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.6, 'Cooldown': 1.1, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.6, 'Crit': 2.7, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.6, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.1},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.3, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 1.7},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 2.5},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.1, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
        {'type': 'chocolate', 'ATK': 1.4, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
    ]
    
    start_time = time.time()
    filtered_toppings = preprocess_toppings(toppings)
    
    valid_combos, close_combos, combinations_checked = find_all_valid_combos(
        [t for t in filtered_toppings if t['type'] == 'chocolate'],
        [t for t in filtered_toppings if t['type'] == 'caramel']
    )
    
    end_time = time.time()
    print_detailed_results(valid_combos, close_combos, combinations_checked, end_time - start_time) 