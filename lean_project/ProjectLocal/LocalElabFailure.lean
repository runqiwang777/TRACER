import Std

namespace ProjectLocal
variable {α : Type}
theorem local_elab_failure : α := by
  infer_instance
end ProjectLocal
