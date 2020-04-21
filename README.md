# Pur Beurre - Upgrade & Debug
OC - Project 11 - Web Plateform P8 Fork (Debug, Upgrade, Customers Relationship Management)

![](https://img.shields.io/badge/Python-%3E%3D3.7-yellow.svg)  ![](https://img.shields.io/badge/Django-2.2.8-brightgreen.svg) ![](https://img.shields.io/badge/local%20database-MySQL-blue.svg)

-----------------------

This project offers a plateform for people in need of a snack, but are looking for something healthy.

A quick search can be done from the main page, and the site offers a list of substitutes in the same category, ordered from the best nutriscore to the worst.

If the user created its account and profile, it can also add a product to its favourites.

----------------------

This project is a fork of "Pur Beurre" project (P08).

This project is a post development simulation. The exemple case is as follow:

    - The client's team wanted to make some changes directly in production. Those changes triggered some Bugs, and all unitests failed.
    - The client wants to add a few new features.

This senario takes into account the abilities to manage customer relationship, the ability to repair bugs, and to create new features to a project (our own or someone elses).

----------------------

In order to ease the database update, a custom command has been created.
This command will automatically update the products, checking and avoiding duplicates.

    python manage.py update_snacks

