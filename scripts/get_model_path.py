# get path of the revit model

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import ModelPathUtils


def get_path(doc):
    try:
        if doc.IsWorkshared:
            path = doc.GetWorksharingCentralModelPath()
            return ModelPathUtils.ConvertModelPathToUserVisiblePath(path)
        else:
            return doc.PathName if doc.PathName else "File not saved"
    except:
        return "Failed to get the file path"


OUT = get_path(DocumentManager.Instance.CurrentDBDocument)
