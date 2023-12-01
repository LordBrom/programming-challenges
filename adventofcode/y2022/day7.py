
import sys

class Folder():

	def __init__(self, name) -> None:
		self.name = name
		self.childFolders = {}
		self.files = []
		self.size = 0
		self.parent = None

	def getSize(self):
		result = self.size
		for child in self.childFolders:
			result += self.childFolders[child].getSize()
		return result


def makeFolders(data):
	data.pop(0)
	folders = []
	Root = Folder("/")
	currentFolder = Root
	for d in data:

		if d[0] == '$':
			dSplit = d.split(" ")
			if dSplit[1] == "cd":
				if dSplit[2] == "..":
					currentFolder = currentFolder.parent
				else:
					if not dSplit[2] in currentFolder.childFolders:
						currentFolder.childFolders[dSplit[2]] = Folder(dSplit[2])
					currentFolder.childFolders[dSplit[2]].parent = currentFolder
					currentFolder = currentFolder.childFolders[dSplit[2]]
					folders.append(currentFolder)

		elif d[0:3] == "dir":
			pass
		else:
			dSplit = d.split(" ")
			currentFolder.size += int(dSplit[0])
	return folders, Root


def part1(data, test=False) -> str:
	folders = makeFolders(data)[0]

	result = 0
	for folder in folders:
		if folder.getSize() <= 100000:
			result += folder.getSize()

	return str(result)

#1062058

def part2(data, test=False) -> str:
	folders, Root = makeFolders(data)
	totalSize = 70000000
	targetSize = 30000000
	unused = totalSize - Root.getSize()
	best = sys.maxsize
	for folder in folders:
		if folder.getSize() + unused >= targetSize:
			best = min(best, folder.getSize())
	print(unused)
	return str(best)
