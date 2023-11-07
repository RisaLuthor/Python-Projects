#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 20:58:38 2023

@author: luthorcorp
"""
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from the to-do list.")
        else:
            print(f"Task '{task}' not found in the to-do list.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("Tasks in the to-do list:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

# Example usage
todo_list = ToDoList()
todo_list.display_tasks()
todo_list.add_task("Buy groceries")
todo_list.add_task("Pay bills")
todo_list.add_task("Call mom")
todo_list.display_tasks()
todo_list.remove_task("Pay bills")
todo_list.display_tasks()
todo_list.remove_task("Walk the dog")
