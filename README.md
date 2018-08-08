# Spanner CI Test Examples

## Introduction

This documentation's goal is to define a set of custom test scripts, to be used by the Spanner CI team as a guideline of what the libraries should look like, what kind of APIs we'd want to provide to our users, and finally how they woud be used in a script.

The secondary goal of these examples is to provide a future documentation to our users, which will help them use our product.

## Test Categories

The test cases are split into three categories:

1. **Basic Tests**, which only perform one action and one test, to showcase that individual test function
2. **Simple Tests**, which perform a simple real-world scenario, i.e. *Turn Light on through Network Command*
3. **Complex Tests**, which perform a more common and complex real-world scenario, and whose goal is to showcase what an actual Functional test for a real product would test, with more than one assertions and using multiple APIs.

Each of these have subcategories, such as GPIO, Networking, etc.
