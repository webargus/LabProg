
import re
import genrandomsteps as steps

pattern = r"(F*)T*"
steps = steps.gen_rnd_str()
regexp = re.findall(pattern, steps)

print(regexp)






