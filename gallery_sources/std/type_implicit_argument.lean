import Std

def identity {α : Type} (x : α) : α := x
example : Nat := identity (α := Nat) True
