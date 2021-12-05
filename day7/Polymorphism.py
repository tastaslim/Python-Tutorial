class Abstract:
    def listMailFolders(self):
        pass

    def getMailFolder(self, folderId):
        pass


class GMail(Abstract):
    def __init__(self) -> None:
        super().__init__()

    def listMailFolders(self):
        return "Gmail mail folders"

    def getMailFolder(self, folderId):
        return "Gmail mail folder"


class OutlookMail(Abstract):
    def __init__(self) -> None:
        super().__init__()

    def listMailFolders(self):
        return "Outlook mail folders"

    def getMailFolder(self, folderId):
        return "Outlook mail folder"
