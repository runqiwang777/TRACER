import Std

namespace Eval18

theorem and_swap_eval (p q : Prop) : p ∧ q → q ∧ p :=
  -- PROOF_START
  sorry
  -- PROOF_END

theorem or_swap_eval (p q : Prop) : p ∨ q → q ∨ p :=
  -- PROOF_START
  sorry
  -- PROOF_END

theorem eq_transitive_eval {α : Type} {a b c : α} : a = b → b = c → a = c :=
  -- PROOF_START
  sorry
  -- PROOF_END

theorem function_congruent_eval {α β : Type} (f : α → β) {a b : α} : a = b → f a = f b :=
  -- PROOF_START
  sorry
  -- PROOF_END

theorem nat_add_zero_eval (n : Nat) : n + 0 = n :=
  -- PROOF_START
  sorry
  -- PROOF_END

theorem nat_zero_add_eval (n : Nat) : 0 + n = n :=
  -- PROOF_START
  sorry
  -- PROOF_END

theorem nat_succ_ne_zero_eval (n : Nat) : Nat.succ n ≠ 0 :=
  -- PROOF_START
  sorry
  -- PROOF_END

theorem nat_le_transitive_eval {a b c : Nat} : a ≤ b → b ≤ c → a ≤ c :=
  -- PROOF_START
  sorry
  -- PROOF_END

theorem bool_cases_eval (b : Bool) : b = true ∨ b = false :=
  -- PROOF_START
  sorry
  -- PROOF_END

theorem identity_application_eval {α : Type} (x : α) : (fun y => y) x = x :=
  -- PROOF_START
  sorry
  -- PROOF_END

theorem and_assoc_eval (p q r : Prop) : (p ∧ q) ∧ r → p ∧ (q ∧ r) :=
  -- PROOF_START
  sorry
  -- PROOF_END

theorem or_assoc_eval (p q r : Prop) : p ∨ (q ∨ r) → (p ∨ q) ∨ r :=
  -- PROOF_START
  sorry
  -- PROOF_END

theorem not_not_intro_eval (p : Prop) : p → ¬¬p :=
  -- PROOF_START
  sorry
  -- PROOF_END

theorem nat_succ_add_eval (n m : Nat) : Nat.succ n + m = Nat.succ (n + m) :=
  -- PROOF_START
  sorry
  -- PROOF_END

theorem nat_add_comm_eval (n m : Nat) : n + m = m + n :=
  -- PROOF_START
  sorry
  -- PROOF_END

theorem nat_mul_zero_eval (n : Nat) : n * 0 = 0 :=
  -- PROOF_START
  sorry
  -- PROOF_END

theorem nat_lt_succ_self_eval (n : Nat) : n < Nat.succ n :=
  -- PROOF_START
  sorry
  -- PROOF_END

theorem implies_self_eval (p : Prop) : p → p :=
  -- PROOF_START
  sorry
  -- PROOF_END

end Eval18
