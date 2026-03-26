from ldr_lint import parse_file, write_to_file
from ldr_lint.lines import SubFileReference

model = parse_file("ShopsPair/Roof_Left.ldr")

new_model = []
for line in model:
	print(line)
	if isinstance(line, SubFileReference):
		line.x *= -1
	# 	line.y *= 1
	
	new_model.append(line)

write_to_file(new_model, "ShopsPair/Roof_Right.ldr")

model = parse_file("ShopsPair/FF_Left.ldr")

new_model = []
for line in model:
	print(line)
	if isinstance(line, SubFileReference):
		line.x *= -1
	# 	line.y *= 1
	
	new_model.append(line)

write_to_file(new_model, "ShopsPair/FF_Right.ldr")
