# monobudget

## Overview

This is a utility that will help keep track of budgets and spending.  Yes... there are many of these but this one is tailored for my very special kind of thinking.

The aim of the product is to take an OFX file as an input and parse the information into a standardised format for budgeting. `monobudget` would therefore need to be able to:

- Import OFX files
- Store historical data in a database
- Categorise transactions into different spending envelopes
- Specify budgets

## Implementation Strategy
We're doing this piecemeal.  I want to be able to read in an OFX file first, followed by storing the raw transactions into a secure SQL database.