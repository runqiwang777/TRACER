import Std

namespace ProjectLocal

def local_helper (n : Nat) : Nat := n + 1

theorem local_failure : local_helper 1 = 3 := by
  rfl

end ProjectLocal
