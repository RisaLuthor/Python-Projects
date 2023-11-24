#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 03:07:56 2023

@author: risaluthor
"""

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [["pepperoni", 2], ["pineapple",6], ["cheese",1], ["sausage",3], ["olives", 2], ["anchovies", 7], ["mushrooms", 2]]
num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)
print(f"We sell {num_pizzas} different kinds of pizza!")
pizza_and_prices = [[2,"pepperoni"], [6,"pineapple"], [1,"cheese"], [3,"sausage"], [2,"olives"], [7,"anchovies"], [2,"mushrooms"]]
print(pizza_and_prices)
pizza_and_prices.sort()
print(pizza_and_prices)
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]
removed_item = pizza_and_prices.pop(4)
pizza_and_prices.insert(2, "peppers")
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
