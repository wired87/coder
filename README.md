# coder

Create a ray remote based actor to analyze and debug an existing codebase.
To do that:

legend: 
"::" next jump in local wf
"->" next pathway step
"-->" edge connect 

extend the following prompt with a clearer workflow definition and detailed tasks to form a currect code pathway:
- create nx.Graph -> walk local dir -> extract content each file add_node file with id=abs filepath includ e entire fiel content-> use ast: identify all present datatypes in each file -> extract its content -> add_node for each with the "parent=[parent file id(abs path.replace(trailing slash all os with __))]" and type=datatype(class, def, comment etc) content=allcontent fo specific datatype(e.g. for def the entire runnable codebase) -> add_edge identified data-type-nodes to its: paren file, child components to its parents (e.g. msthods to(-->) classes -> for each import: get edge-attrs from nid and parent[0](file-abs_path) -> loop compoennts connected to this parent(file-node) -> analyze the content of each specific component (saved in the graph) :: add_edge "imort --> component id" if used by the datatype (e.g. a class uses a imported variable inside its init def) -> add edge  "import --> (component of the file provides them)"

- Step 2 (Query pipe):
  input: filedir, text query -> gem request  prompt(improve)="generate 10 keywords to find the requested component within the provided id list(loop thotugh nx graph and provide all ids as list) using a similarity search(ss). -> embed queries and (all node ids (nid_embed_struct) of the nx.graph (nid_embed_struct)) -> save in two sepparate dicts with format "key:embedding" -> for each component of nid_embed_struct :: perform a similarity search -> save the resutl in (sum the results ) -> return top 5 nid_embed_struct of the with highest score 

extras:
- use clear oneliner comments before each fuction/method call and at the start of each method to intepret
- use creative emojicons
- include a r.txt (requiremens)
