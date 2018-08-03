#!/bin/python3

import math
import os
import random
import re
import sys


class Node:
    def __init__(self):
        self.children = {}
        self.count = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        cur = self.root

        for character in word:
            if not character in cur.children:
                cur.children[character] = Node()
            cur = cur.children[character]
            cur.count += 1

    def find(self, word):
        cur = self.root

        for character in word:
            if not character in cur.children:
                return 0
            cur = cur.children[character]

        return cur.count


if __name__ == '__main__':
    tries = Trie()

    n = int(input())

    for n_itr in range(n):
        opContact = input().split()
        op = opContact[0]
        contact = opContact[1]

        if op == 'add':
            tries.add(contact)
        elif op == 'find':
            print(tries.find(contact))
