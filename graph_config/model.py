from pydantic import BaseModel
from typing import Optional,Dict



class GraphState(BaseModel):
    srs_docx_path:str
    analysis:Optional[str] = None
    project_root:str
    unit_test:Optional[str]=None
    generated_code:Optional[Dict[str,str]]=None
    test_results:Optional[str]=None
    debug_logs:Optional[str]=None
