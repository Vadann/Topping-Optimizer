from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional, Union

@dataclass
class CookieConfig:
    """Configuration for a cookie's optimization requirements"""
    name: str
    base_stats: Dict[str, float]
    required_stats: Dict[str, Union[float, Tuple[float, float]]]
    topping_strategy: List[Tuple[str, int]]  # List of (topping_type, count)
    relevant_stats: List[str]
    min_relevant_stats: int = 2
    
    def __post_init__(self):
        # Validate the topping counts add up to 5
        total_toppings = sum(count for _, count in self.topping_strategy)
        if total_toppings != 5:
            raise ValueError(f"Topping strategy must use 5 toppings, got {total_toppings}") 