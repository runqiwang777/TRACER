
namespace Eval18

theorem and_swap_eval (p q : Prop) : p ∧ q → q ∧ p :=
  -- PROOF_START
  by
    intro h
    exact And.intro h.right h.left
  -- PROOF_END

end Eval18
