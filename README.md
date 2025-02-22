# Online Shopping Cart System

## Description
This program allows users to add, remove, and view products in their shopping cart, as well as calculate the total cost and apply discounts.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Class Structure](#class-structure)
- [Usage](#usage)
- [Example](#example)
- [Conclusion](#conclusion)

## Overview
The Online Shopping Cart System is designed to mimic a real-world online shopping experience. Users can manage their shopping cart by adding or removing products, view the current contents of their cart, calculate the total cost, and apply discount codes.

## Features
1. Add Product
2. Remove Product
3. View Cart
4. Calculate Total
5. Apply Discount
6. Generate Receipt
7. Exit

## Class Structure

### `class Product`
- **Attributes**:
  - `name`
  - `price`
  - `quantity`

### `class ShoppingCart`
- **Attributes**:
  - `products` (list of `Product` instances)
  - `discount` (store discount percentage)
- **Methods**:
  - `add_product(self, name, price, quantity)`
  - `remove_product(self, product_name)`
  - `view_cart(self)`
  - `calculate_total(self)`
  - `apply_discount(self, discount_code)`
  - `generate_receipt(self)`

## Usage
1. Run the `main()` function to start the Online Shopping Cart System.
2. Follow the on-screen prompts to add, remove, view, or manage products in your shopping cart.

## Example
```python
if __name__ == "__main__":
    main()
