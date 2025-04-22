# social_media_posts.py - Social Media Marketing Automation

# Step 2: Creating Data Structures
products = [
    {"image": "product1.jpg", "description": "Introducing our new wireless headphones!"},
    {"image": "product2.png", "description": "The perfect summer sandals are here!"},
    {"image": "product3.jpg", "description": "Try our organic skincare line for radiant skin!"},
    {"image": "product4.png", "description": "Boost your productivity with our smart home devices!"}
]

platforms = ["Facebook", "Twitter", "Instagram", "LinkedIn"]

# Step 3: Creating the First Function
def print_product_info(image, description):
    """
    Prints product information without mentioning the platform.
    
    Args:
        image (str): The filename of the product image
        description (str): The product description
    """
    print(f"Product Post: Image - {image}, Description - {description}")

# Step 4: Creating the Second Function
def print_post_by_platform(platform, image, description):
    """
    Prints product information along with the target social media platform.
    
    Args:
        platform (str): The social media platform name
        image (str): The filename of the product image
        description (str): The product description
    """
    print(f"Platform: {platform} - Post: Image - {image}, Description - {description}")

# Test the first function
print("Testing print_product_info function:")
print("-" * 50)
for product in products:
    image = product["image"]
    description = product["description"]
    print_product_info(image, description)

print("\n")

# Test the second function
print("Testing print_post_by_platform function:")
print("-" * 50)

# Option 1: Using nested loops
print("Method 1: Using nested loops")
for platform in platforms:
    for product in products:
        image = product["image"]
        description = product["description"]
        print_post_by_platform(platform, image, description)

print("\n")

# Option 2: Using zip (limited to matching pairs)
print("Method 2: Using zip (Note: This only works if lists are same length)")
# For demonstration purposes only, using first items if lists aren't same length
min_length = min(len(products), len(platforms))
for i in range(min_length):
    product = products[i]
    platform = platforms[i]
    image = product["image"]
    description = product["description"]
    print_post_by_platform(platform, image, description)

print("\n")

# Option 3: Generate specific combinations
print("Method 3: Specific product-platform combinations")
# Example: Post first product on all platforms
product = products[0]
for platform in platforms:
    print_post_by_platform(platform, product["image"], product["description"])