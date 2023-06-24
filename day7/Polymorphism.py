from abc import abstractmethod, ABC


class Abstract(ABC):
    @abstractmethod
    def list_mail_folders(self):
        pass

    @abstractmethod
    def get_mail_folder(self, folder_id: str):
        pass


class GMail(Abstract):
    def __init__(self) -> None:
        super().__init__()

    def list_mail_folders(self):
        return "Gmail mail folders"

    def get_mail_folder(self, folder_id: str):
        print(folder_id)
        return "Gmail mail folder"


class OutlookMail(Abstract):
    def __init__(self) -> None:
        super().__init__()

    def list_mail_folders(self):
        return "Outlook mail folders"

    def get_mail_folder(self, folder_id: str):
        print(folder_id)
        return "Outlook mail folder"
