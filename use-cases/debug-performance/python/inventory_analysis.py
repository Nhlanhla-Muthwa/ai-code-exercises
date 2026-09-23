import time
import random
from bisect import bisect_left, bisect_right

def find_product_combinations_fast(products, target_price, price_margin=10):
    """
    Find all pairs of products within the target price range in O(N log N) time.
    """
    # Sort products by price to enable binary search
    sorted_products = sorted(products, key=lambda x: x['price'])
    prices = [p['price'] for p in sorted_products]
    
    results = []
    n = len(sorted_products)
    
    min_combined = target_price - price_margin
    max_combined = target_price + price_margin

    for i in range(n):
        product1 = sorted_products[i]
        p1_price = product1['price']
        
        # Calculate the required price range for product2
        target_min_p2 = min_combined - p1_price
        target_max_p2 = max_combined - p1_price
        
        # Use binary search to find the slice of valid prices in O(log N) time
        # We start search from i + 1 to avoid self-pairing and duplicates (A, B vs B, A)
        left_idx = bisect_left(prices, target_min_p2, lo=i + 1)
        right_idx = bisect_right(prices, target_max_p2, lo=i + 1)
        
        for j in range(left_idx, right_idx):
            product2 = sorted_products[j]
            combined_price = p1_price + product2['price']
            
            results.append({
                'product1': product1,
                'product2': product2,
                'combined_price': combined_price,
                'price_difference': abs(target_price - combined_price)
            })

    # Sort results by closeness to the target price
    results.sort(key=lambda x: x['price_difference'])
    return results

# Example usage
if __name__ == "__main__":
    print("Generating Product List...")
    product_list = []
    for i in range(5000):
        product_list.append({
            'id': i,
            'name': f'Product {i}',
            'price': random.randint(5, 500)
        })

    print(f"Finding product combinations for {len(product_list)} products...")
    start_time = time.time()
    combinations = find_product_combinations_fast(product_list, 500, 50)
    end_time = time.time()

    print(f"Found {len(combinations)} product combinations")
    print(f"Execution time: {end_time - start_time:.4f} seconds")