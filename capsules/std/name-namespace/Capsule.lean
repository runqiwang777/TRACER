import Std

namespace Hidden
def proof : True := True.intro
end Hidden

example : True := by
  exact proof
