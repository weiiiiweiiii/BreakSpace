
class RecentFiles:
    recentFileName = "recentFiles.spacebreaker"
    def __init__(self):
        pass
    
    @staticmethod
    def getRecentFiles():
        result = []
        try:
            f = open(RecentFiles.recentFileName, "r")
            for line in f:
                result.append(line.rstrip())
            f.close()
        except:
            f = open(RecentFiles.recentFileName, "w")
            f.close()
        return result
    
    @staticmethod
    def addOpenedFile(file_name):
        rF = RecentFiles.getRecentFiles()
        if file_name in rF:
            rF.remove(file_name)
            rF.append(file_name)
        else:
            if len(rF) >= 10:
                rF.pop(0)
            rF.append(file_name)
        RecentFiles.saveRecentFile(rF)
    
    @staticmethod
    def saveRecentFile(file_names):
        f = open(RecentFiles.recentFileName, "w")
        for file_name in file_names:
            f.write(file_name)
            f.write("\n")
        f.close()