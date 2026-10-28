import Std

theorem local_context (p : Prop) : p → p := by
  intro hp
  clear hp
  exact hp
