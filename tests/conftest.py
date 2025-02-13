from dataclasses import dataclass


@dataclass
class BinaryTree:
    value: int
    left: "BinaryTree | None" = None
    right: "BinaryTree | None" = None
