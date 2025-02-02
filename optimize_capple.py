from itertools import combinations
import time

def preprocess_toppings(toppings, min_relevant_stats=2):
    """
    Filter toppings based on relevance to Crit, Cooldown, and DMG_Resist.
    Only keep toppings that have at least min_relevant_stats of these stats.
    """
    relevant_stats = ['Crit', 'Cooldown', 'DMG_Resist']
    filtered_toppings = []
    discarded_toppings = []
    
    print("\nPreprocessing Toppings:")
    print("-" * 50)
    print(f"Starting with {len(toppings)} total toppings")
    
    for topping in toppings:
        # Count how many relevant stats this topping has
        relevant_count = sum(1 for stat in relevant_stats if topping.get(stat, 0) > 0)
        
        if relevant_count >= min_relevant_stats:
            filtered_toppings.append(topping)
        else:
            discarded_toppings.append((topping, relevant_count))
    
    # Print summary by type
    jelly_kept = len([t for t in filtered_toppings if t['type'] == 'apple_jelly'])
    choc_kept = len([t for t in filtered_toppings if t['type'] == 'chocolate'])
    jelly_total = len([t for t in toppings if t['type'] == 'apple_jelly'])
    choc_total = len([t for t in toppings if t['type'] == 'chocolate'])
    
    print(f"\nDiscarded {len(discarded_toppings)} toppings with fewer than {min_relevant_stats} relevant stats")
    print(f"Apple Jelly toppings kept: {jelly_kept}/{jelly_total}")
    print(f"Chocolate toppings kept: {choc_kept}/{choc_total}")
    print(f"Total toppings kept: {len(filtered_toppings)}/{len(toppings)}")
    
    return filtered_toppings

def find_all_valid_combos(jelly_toppings, raspberry_toppings):
    """Find valid combinations for 3 Raspberry + 2 Jelly strategy."""
    cd_range = (24.0, 25.0)
    min_dmr = 15.0
    crit_range = (27.0, 28.0)
    
    # Strategy: 3 Raspberry + 2 Jelly
    base_cd = 17.1
    base_crit = 18
    base_dmr = 0
    
    valid_combos = []
    combinations_checked = 0
    
    print(f"\nChecking all combinations of:")
    print(f"Apple Jelly toppings: {len(jelly_toppings)}")
    print(f"Raspberry toppings: {len(raspberry_toppings)}")
    
    print("\nChecking Strategy: 3 Raspberry + 2 Jelly")
    for rasp_combo in combinations(raspberry_toppings, 3):
        for jelly_combo in combinations(jelly_toppings, 2):
            combinations_checked += 1
            combo = list(rasp_combo) + list(jelly_combo)
            
            total_cd = base_cd + sum(t.get('Cooldown', 0) for t in combo)
            total_crit = base_crit + sum(t.get('Crit', 0) for t in combo)
            total_dmr = base_dmr + sum(t.get('DMG_Resist', 0) for t in combo)
            total_atk = sum(t.get('ATK', 0) for t in combo)
            
            if (cd_range[0] <= total_cd <= cd_range[1] and 
                total_dmr >= min_dmr and
                crit_range[0] <= total_crit <= crit_range[1]):
                valid_combos.append({
                    'strategy': '3R2J',
                    'combo': combo,
                    'total_cd': total_cd,
                    'total_crit': total_crit,
                    'total_dmr': total_dmr,
                    'total_atk': total_atk
                })
            
            if combinations_checked % 1000 == 0:
                print(f"Checked {combinations_checked} combinations...")
    
    # Sort by ATK first
    valid_combos.sort(key=lambda x: x['total_atk'], reverse=True)
    
    return valid_combos, combinations_checked

def print_detailed_results(valid_combos, combinations_checked, time_taken):
    """Print detailed analysis of all valid combinations."""
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
        print(f"\n{i}. {result['strategy']} Combination (ATK: {result['total_atk']:.1f}, "
              f"CD: {result['total_cd']:.1f}, "
              f"Crit: {result['total_crit']:.1f}, "
              f"DMR: {result['total_dmr']:.1f}):")
        print("-" * 60)
        print(f"{'Type':<12}{'ATK':<8}{'CD':<8}{'Crit':<8}{'DMR':<8}")
        print("-" * 60)
        for topping in combo:
            print(f"{topping['type']:<12}{topping.get('ATK', 0):<8.1f}"
                  f"{topping.get('Cooldown', 0):<8.1f}"
                  f"{topping.get('Crit', 0):<8.1f}"
                  f"{topping.get('DMG_Resist', 0):<8.1f}")

def test_preprocess():
    """Test the preprocessing function with detailed output."""
    test_toppings = [
        {'type': 'apple_jelly', 'Crit': 3.0, 'Cooldown': 1.8, 'DMG_Resist': 2.5},
        {'type': 'chocolate', 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 5.0},
    ]
    
    print("\nTesting Preprocess Function")
    print("=" * 50)
    print("\nOriginal Toppings:")
    print("-" * 50)
    print(f"{'Type':<12}{'Crit':<8}{'CD':<8}{'DMG_Resist':<10}")
    print("-" * 50)
    
    for topping in test_toppings:
        print(f"{topping['type']:<12}{topping.get('Crit', 0):<8.1f}"
              f"{topping.get('Cooldown', 0):<8.1f}{topping.get('DMG_Resist', 0):<10.1f}")
    
    # Run preprocessing
    filtered_toppings = preprocess_toppings(test_toppings)
    
    print("\nKept Toppings:")
    print("-" * 50)
    print(f"{'Type':<12}{'Crit':<8}{'CD':<8}{'DMG_Resist':<10}")
    print("-" * 50)
    
    for topping in filtered_toppings:
        print(f"{topping['type']:<12}{topping.get('Crit', 0):<8.1f}"
              f"{topping.get('Cooldown', 0):<8.1f}{topping.get('DMG_Resist', 0):<10.1f}")

    print("\nTest complete!")
    print("=" * 50)

if __name__ == "__main__":
    # Your toppings list goes here
    toppings = [
        
     {'type': 'apple_jelly', 'ATK': 2.4, 'ATK_SPD': 0.0, 'Crit': 2.5, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 1.7, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.5},
    {'type': 'apple_jelly', 'ATK': 2.1, 'ATK_SPD': 2.9, 'Crit': 1.7, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 1.7, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.0, 'ATK_SPD': 3.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.1},
    {'type': 'apple_jelly', 'ATK': 2.2, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.2, 'ATK_SPD': 1.5, 'Crit': 2.5, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.2, 'ATK_SPD': 1.8, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 1.7, 'ATK_SPD': 1.2, 'Crit': 2.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 1.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.8, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.8, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.6, 'Crit': 1.6, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.6, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.2},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.4, 'ATK_SPD': 2.3, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 1.3, 'ATK_SPD': 2.3, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 1.2, 'ATK_SPD': 2.3, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.1},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.1, 'Crit': 0.0, 'Cooldown': 1.4, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.0, 'Crit': 1.7, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.3, 'ATK_SPD': 2.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 1.1, 'ATK_SPD': 2.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 1.8, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 1.7, 'ATK_SPD': 1.7, 'Crit': 2.6, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 1.6, 'ATK_SPD': 1.4, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 1.4, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.1, 'Crit': 2.8, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.9, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 1.4, 'Crit': 2.8, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.6, 'Cooldown': 0.0, 'DMG_Resist': 3.8},
    {'type': 'apple_jelly', 'ATK': 1.3, 'ATK_SPD': 0.0, 'Crit': 2.3, 'Cooldown': 1.2, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.0, 'ATK_SPD': 0.0, 'Crit': 2.3, 'Cooldown': 0.0, 'DMG_Resist': 2.3},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 2.2, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.8, 'ATK_SPD': 0.0, 'Crit': 2.2, 'Cooldown': 1.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 1.9, 'ATK_SPD': 0.0, 'Crit': 2.1, 'Cooldown': 0.0, 'DMG_Resist': 3.4},
    {'type': 'apple_jelly', 'ATK': 1.7, 'ATK_SPD': 1.8, 'Crit': 2.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.7, 'Cooldown': 1.3, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.0, 'Crit': 1.2, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 1.6, 'ATK_SPD': 0.0, 'Crit': 1.1, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.0, 'Cooldown': 2.0, 'DMG_Resist': 2.6},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.2, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 1.9, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 1.6, 'ATK_SPD': 2.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 1.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.1, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 1.6, 'ATK_SPD': 2.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 1.6, 'ATK_SPD': 1.1, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 4.5},
    {'type': 'apple_jelly', 'ATK': 1.7, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.8},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 1.8, 'Crit': 2.4, 'Cooldown': 0.0, 'DMG_Resist': 5.5},
    {'type': 'apple_jelly', 'ATK': 2.1, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.4},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.3},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.1},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.0},
    {'type': 'apple_jelly', 'ATK': 2.9, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.9, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.4},
    {'type': 'apple_jelly', 'ATK': 2.8, 'ATK_SPD': 0.0, 'Crit': 2.5, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.8, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.6},
    {'type': 'apple_jelly', 'ATK': 2.7, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.5},
    {'type': 'apple_jelly', 'ATK': 2.5, 'ATK_SPD': 1.9, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.4, 'ATK_SPD': 0.0, 'Crit': 1.2, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.3, 'ATK_SPD': 0.0, 'Crit': 1.8, 'Cooldown': 0.0, 'DMG_Resist': 1.9},
    {'type': 'apple_jelly', 'ATK': 2.2, 'ATK_SPD': 0.0, 'Crit': 1.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.2, 'ATK_SPD': 1.6, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.8, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.0, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 2.9},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 1.6, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 1.9, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 1.4, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 1.5, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 1.8, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 1.2, 'Crit': 2.7, 'Cooldown': 0.0, 'DMG_Resist': 5.5},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.4, 'Cooldown': 0.0, 'DMG_Resist': 3.0},
    {'type': 'apple_jelly', 'ATK': 1.7, 'ATK_SPD': 0.0, 'Crit': 2.2, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.1, 'Cooldown': 0.0, 'DMG_Resist': 5.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 1.7, 'Crit': 1.7, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 5.5},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 4.1},
    {'type': 'apple_jelly', 'ATK': 2.2, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 1.8, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 1.9, 'Crit': 2.7, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0, 'Cooldown': 1.8, 'DMG_Resist': 3.5},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.5, 'Cooldown': 1.8, 'DMG_Resist': 1.3},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 1.8, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.8, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 1.4, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 1.2, 'ATK_SPD': 1.7, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 1.1, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 3.2},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.4, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.4, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 4.3},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 1.1, 'Crit': 2.7, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 6.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.8},
    {'type': 'apple_jelly', 'ATK': 1.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.1, 'DMG_Resist': 5.6},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 1.1, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 5.1},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.1, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.8},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.7},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.7, 'Cooldown': 0.0, 'DMG_Resist': 4.7},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.6},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.5},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.2, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.4},
    {'type': 'apple_jelly', 'ATK': 0.0, 'ATK_SPD': 2.3, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.4},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.8, 'Crit': 2.6, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.4, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 1.9},
    {'type': 'raspberry', 'ATK': 2.5, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 1.7},
    {'type': 'raspberry', 'ATK': 2.6, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.0, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 1.2, 'ATK_SPD': 2.2, 'Crit': 2.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.1, 'Crit': 0.0, 'Cooldown': 1.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.6, 'ATK_SPD': 2.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.6, 'Cooldown': 1.1, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.5, 'Crit': 2.4, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.4, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 3.0, 'Crit': 2.4, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.2, 'ATK_SPD': 0.0, 'Crit': 2.2, 'Cooldown': 0.0, 'DMG_Resist': 2.1},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.1, 'Cooldown': 0.0, 'DMG_Resist': 5.7},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.7, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 1.9, 'DMG_Resist': 2.5},
    {'type': 'raspberry', 'ATK': 2.2, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 5.4},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.5, 'Crit': 2.4, 'Cooldown': 1.3, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 6.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.4, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 6.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.2, 'Cooldown': 0.0, 'DMG_Resist': 6.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 6.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 6.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.2, 'DMG_Resist': 6.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.4, 'Cooldown': 0.0, 'DMG_Resist': 6.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.1, 'Cooldown': 1.2, 'DMG_Resist': 5.1},
    {'type': 'raspberry', 'ATK': 2.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.4},
    {'type': 'raspberry', 'ATK': 1.8, 'ATK_SPD': 1.3, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.4},
    {'type': 'raspberry', 'ATK': 1.3, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.2},
    {'type': 'raspberry', 'ATK': 3.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.8, 'ATK_SPD': 1.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.4},
    {'type': 'raspberry', 'ATK': 2.7, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.3},
    {'type': 'raspberry', 'ATK': 2.7, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.4, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.7},
    {'type': 'raspberry', 'ATK': 2.4, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 1.2, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.3, 'ATK_SPD': 0.0, 'Crit': 1.3, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.3, 'ATK_SPD': 0.0, 'Crit': 2.4, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.3, 'ATK_SPD': 1.2, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.3, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.2, 'ATK_SPD': 0.0, 'Crit': 1.0, 'Cooldown': 0.0, 'DMG_Resist': 4.4},
    {'type': 'raspberry', 'ATK': 2.2, 'ATK_SPD': 0.0, 'Crit': 2.6, 'Cooldown': 0.0, 'DMG_Resist': 5.9},
    {'type': 'raspberry', 'ATK': 2.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.3},
    {'type': 'raspberry', 'ATK': 1.9, 'ATK_SPD': 0.0, 'Crit': 1.1, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 1.2, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 1.1},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.7, 'ATK_SPD': 0.0, 'Crit': 2.5, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.3},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.5, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 1.3, 'ATK_SPD': 0.0, 'Crit': 1.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 3.0, 'Crit': 1.5, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.6, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 2.0, 'Cooldown': 0.0, 'DMG_Resist': 4.0},
    {'type': 'raspberry', 'ATK': 1.9, 'ATK_SPD': 2.8, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.8, 'Crit': 1.2, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.8, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.6, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 1.4, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 2.4, 'Cooldown': 0.0, 'DMG_Resist': 4.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.5},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.2, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.9},
    {'type': 'raspberry', 'ATK': 2.9, 'ATK_SPD': 2.3, 'Crit': 1.3, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.1, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.7, 'Crit': 2.6, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.4, 'ATK_SPD': 1.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 3.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 3.0, 'Cooldown': 0.0, 'DMG_Resist': 4.5},
    {'type': 'raspberry', 'ATK': 1.6, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.6, 'ATK_SPD': 1.1, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 3.0, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 0.0, 'DMG_Resist': 2.2},
    {'type': 'raspberry', 'ATK': 1.5, 'ATK_SPD': 0.0, 'Crit': 2.6, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.3, 'Crit': 2.5, 'Cooldown': 1.2, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.9, 'ATK_SPD': 0.0, 'Crit': 2.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.3, 'Crit': 1.7, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.1, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 4.7},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 1.8, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.9, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.2, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.3, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.3, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.4, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.9, 'ATK_SPD': 2.0, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 2.8},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.5, 'Cooldown': 1.7, 'DMG_Resist': 1.3},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.3, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.7, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.6, 'ATK_SPD': 2.8, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.0, 'ATK_SPD': 1.7, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.5, 'Cooldown': 1.4, 'DMG_Resist': 5.1},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.7, 'Cooldown': 1.4, 'DMG_Resist': 3.7},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.9},
    {'type': 'raspberry', 'ATK': 2.7, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.7},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.7},
    {'type': 'raspberry', 'ATK': 2.2, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.5},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 1.6, 'DMG_Resist': 5.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.2, 'Cooldown': 0.0, 'DMG_Resist': 5.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.8},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.3, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.4},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.4},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.3, 'Cooldown': 0.0, 'DMG_Resist': 4.1},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.0, 'DMG_Resist': 3.3},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.7, 'Cooldown': 0.0, 'DMG_Resist': 3.2},
    {'type': 'raspberry', 'ATK': 2.6, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.1},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.1},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 3.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 2.8},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 2.5},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.0, 'Cooldown': 0.0, 'DMG_Resist': 1.4},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.6, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 1.1},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 2.8},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.0, 'Crit': 2.2, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.8, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 2.7},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.3, 'Crit': 1.8, 'Cooldown': 0.0, 'DMG_Resist': 3.7},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.2, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 1.8},
    {'type': 'raspberry', 'ATK': 2.0, 'ATK_SPD': 0.0, 'Crit': 2.2, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 1.5, 'ATK_SPD': 0.0, 'Crit': 2.4, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 3.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 1.0},
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
        #{'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 4.9},
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
        #{'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 4.7},
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
        # {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 5.7},
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
        {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.1}

    ]
    
    start_time = time.time()
    filtered_toppings = preprocess_toppings(toppings)
    
    # Find all valid combinations
    valid_combos, combinations_checked = find_all_valid_combos(
        [t for t in filtered_toppings if t['type'] == 'apple_jelly'],
        [t for t in filtered_toppings if t['type'] == 'raspberry']
    )
    
    end_time = time.time()
    
    # Print detailed results
    print_detailed_results(valid_combos, combinations_checked, end_time - start_time)