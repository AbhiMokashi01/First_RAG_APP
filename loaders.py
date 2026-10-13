import warnings

warnings.filterwarnings(
    "ignore",
    category=DeprecationWarning,
    message=r".*langchain-community.*"
)

from langchain_community.document_loaders import PyMuPDFLoader, DirectoryLoader
from langchain_core.documents import Document

def file_loading(path:str)->list[Document]:
    try:
        file_loader=DirectoryLoader(path=path,glob="**/*.pdf",loader_cls=PyMuPDFLoader,show_progress=True)
        documents=file_loader.load()
        print(f"{len(documents)}documents loaded successfully")
        return documents
    except Exception as e:
        print(f"document loading failed with--->{e}")

    