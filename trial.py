def shortenPath(path):
	pathListTokens = path.split("/")
	shortenPathStack = []
	shortenPathStack.append("/",) if pathListTokens[0] == "" else None 
	print(pathListTokens)
	for token in pathListTokens:
		if token == "":
			continue
		if token == ".." and len(shortenPathStack) > 1:
			# print("before: ", shortenPathStack)
			shortenPathStack.pop()
			shortenPathStack.pop()
			# print("after: ", shortenPathStack)
		elif token == "." and len(shortenPathStack) > 1:
			continue
		else:
			shortenPathStack.append(token)
			shortenPathStack.append("/")
		print(shortenPathStack)
	if len(shortenPathStack) > 2:
		shortenPathStack.pop()
	return "".join(shortenPathStack)


print(shortenPath("/foo/../test/../test/../foo//bar/./baz"))
## "/foo/bar/baz")