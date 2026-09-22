Name: Shradha Dhananjay Kumbhar.

PRN: 25UAM030

# AI Agent Portfolio

## Introduction

This project is developed as part of the AI-Augmented Workflow course.

The main objective of this project is to understand the basic concepts of
Artificial Intelligence Agents and develop a simple AI Agent using Python,
Ollama, and the Llama 3.2 language model.

## Objective

The objectives of this project are:

- Understand the concept of AI Agents.
- Learn how an AI Agent communicates with an AI model.
- Develop a basic AI Agent using Python.
- Use Ollama to run an AI model locally.
- Document the architecture and technology decisions.
- Maintain the project using Git and GitHub.

## What is an AI Agent?

An AI Agent is a software system that can receive information, process it,
make decisions, and perform actions to achieve a particular goal.

A basic AI Agent generally follows this process:

```text
User Input
    ↓
AI Agent
    ↓
Language Model
    ↓
Response
    ↓
User






# SLE-2: Profiling Report – BFS vs DFS

## Course

02AML204 – Introduction to Artificial Intelligence

## Student Details

- **Name:** Shradha Dhananjay Kumbhar
- **PRN:** 25UAM030
- **Division:** A

## Objective

The objective of this SLE-2 activity is to empirically compare the performance of two uninformed search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

Both algorithms are tested on the same graph. Execution time and the number of explored nodes are measured.

## Problem Used

A graph containing 12 nodes is used for the experiment.

- **Start Node:** A
- **Goal Nodes:** A to L

Different goal nodes are tested to observe the best, average, and worst cases.

## Algorithms

### Breadth-First Search (BFS)

BFS explores nodes level by level using a queue.

File:

`src/bfs.py`

Run:

```powershell
python src/bfs.py