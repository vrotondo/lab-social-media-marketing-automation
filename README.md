# lab-social-media-marketing-automation
Foundations I - Lab: Social Media Marketing Automation

Lab: Social Media Marketing Automation 
Welcome to this lab where you'll create a Python script to automate social media posts for a marketing company. This exercise will help you practice using lists, dictionaries, loops, and functions in Python - all essential skills for a junior software engineer.

By the end of this lab, you'll have written a program that can generate customized social media posts for different products across various platforms. This practical application will reinforce your Python skills and introduce you to a real-world scenario in software development.

Tools and Resources
Python IDE: Visual Studio Code.
Output: A single python file (.py) named:social_media_posts.py
The Scenario
You are a junior software engineer who has recently joined a thriving social media marketing company. The company manages social media campaigns for various clients, promoting a wide range of products across multiple platforms. Your team lead has assigned you an exciting project: to create a Python program that automates the process of generating social media posts for different products across various platforms.

This automation will significantly streamline the company's workflow, allowing the marketing team to focus on strategy and client relations while ensuring consistent and timely posts across all platforms. Your program will need to handle product information (including images and descriptions) and target different social media platforms like Facebook, Twitter, and Instagram.

Your task is to write a script that uses loops to iterate through a list of products and create individual social media posts for each one. You'll need to define two key functions:

print_product_info(): This function will allow users to print product information without specifying the target social media platform.
print_post_by_platform(): This function will print the product information along with the target social media platform.
Instructions
Step 1: Setting Up Your Environment
Open Visual Studio Code. 
Create a new Python file and save it as: social_media_posts.py
Step 2: Creating Data Structures
In your social_media_posts.py file, create two lists:

products: A list of dictionaries containing product information. Each dictionary should have two keys: "image" (string representing the image file name) and "description" (string containing the product description).
platforms: A list of social media platform names where you want to post (e.g., "Facebook", "Twitter", "Instagram").
Example Code:

products = [
    {"image": "product1.jpg", "description": "Introducing our new wireless headphones!"},
    {"image": "product2.png", "description": "The perfect summer sandals are here!"}
]

platforms = ["Facebook", "Twitter", "Instagram"]
Step 3: Creating the First Function
Your task is to create a function called print_product_info() that prints product information without mentioning the platform.

Requirements:

The function should take two parameters: one for the image and one for the description.
It should print a formatted message including both the image and description.
Test your function using the products list you created in Step 2..
Example Code:

for product in products:
    image = product["image"]
    description = product["description"]
    print(f"Product Post: Image - {image}, Description - {description}")
Step 4: Creating the Second Function
Next, create a function called print_post_by_platform() that includes the platform in the output.

Requirements:

This function should take three parameters: one for the platform, one for the image, and one for the description.
It should print a formatted message including the platform, image, and description.
Test your function using both the products and platforms lists from Step 2.
Hint: Consider how you might use the zip() function to iterate through both lists simultaneously.
Example Code (with zip):

for product, platform in zip(products, platforms):
    image = product["image"]
    description = product["description"]
    print(f"Platform: {platform} - Post: Image - {image}, Description - {description}")
Step 5: Running Your Script
After creating both functions, run your script in VS Code. Ensure that you see output demonstrating the functionality of both functions before submitting your assignment.

Submission 
Make sure you have saved the file as social_media_posts.py
Click the Load Lab: Social Media Marketing Automationbutton below to launch this assignment in CodeGrade.
Upload your Python file to theclick here or add files to uploadfield. 
For additional information on submitting assignments in CodeGrade:Getting Started in CanvasLinks to an external site..
Grading Criteria
Use the rubric below as a guide for how this lab is graded.
You submission will be automatically scored in CodeGrade.
You can review your submission in CodeGrade and see your final score in your Canvas grades.