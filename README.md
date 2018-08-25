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

Once transactions can be read and stored, the budget categories can be created.  Each transaction should then be mapped to a category and basic accounting principles applied to check balances.

The rules engine can then be created to help automatically associate transactions with budget categories.  Regular expressions and knowledge of the transaction metadata can be used.

## Data Architecture
Raw data that is extracted from the database is stored as is in the database using the unique id's provided by the bank.  The database stores:

### Raw data
- The account type (e.g. so that credit and current accounts can be used simultaneously)
- Transaction data
- Account metadata (e.g. balances)

### Budget data
Different spending categories need to exist be maintained.  The allocated budget as well as transactions associated with the categories need to be maintained.

### Payee data
A list of beneficiaries with unique identifiers.  Each transaction is linked to a payee that will be matched manually or by using the rules engine.

### Rules data
A set of rules (e.g. regular expressions) that is used to map the raw data of a transaction to budget and payee data.