"""
IMMPROVEMENT

Code Pathway: Graph Generation (Step 1)
This step builds a graph representing the file structure and internal component dependencies.

Workflow Step	Action	Details / Tasks
Setup & Initialization	Initialize Graph & Input	Create an empty nx.Graph(). Define the starting directory (local_dir).
File Traversal	Walk Directory & Filter	Recursively traverse local_dir. For each file:
1. Add File Node: graph.add_node(id=abs_filepath, type='file', content=entire_file_content)
2. File ID Sanitization: Create a sanitized file ID (e.g., replace non-alphanumeric chars with '__') for internal linking.
AST Analysis & Component Extraction	Parse File Content	Use ast (or similar language-specific parser) on entire_file_content.
Identify Components: Detect all top-level data types/components: class, function (def), import, variable, etc.
Add Component Nodes: For each identified component:
- graph.add_node(id=component_id, type=datatype_type, content=component_code_or_text)
- Set Attributes: parent=abs_filepath_sanitized (the file's sanitized ID)
Component-File Edges	Link Components to File	Add Edge: graph.add_edge(component_id, abs_filepath, relationship='contained_in')
Internal Component Edges	Link Nested Components	Identify parent-child relationships within the file (e.g., methods within classes, nested functions).
Add Edge: graph.add_edge(child_component_id, parent_component_id, relationship='is_part_of')
Import Analysis & Dependency Edges (:: next jump)	Process Imports	Loop through all import nodes added.
Get Scope: Identify the parent file node and all other component nodes in that same file.
Analyze Usage: For each non-import component (e.g., class, def) in the file, analyze its content (code/text) for usage of the imported name/object.
Add Edge: If usage is detected, graph.add_edge(import_node_id, using_component_id, relationship='uses')
Add Edge (Provider): Identify the actual component (if internal) or file (if external) that provides the imported entity. graph.add_edge(import_node_id, provider_id, relationship='provided_by') (This part often requires external logic for resolving imports, but for local-only, it links to local file nodes).

In Google Sheets exportieren

Code Pathway: Query Pipe (Step 2)
This step uses the generated graph for a similarity-based component search.

Workflow Step	Action	Details / Tasks
Input & Query Prep	Receive Inputs	Get filedir (optional, for context/filtering) and text_query.
Generate Keywords	GEMINI Request: Send the text_query and a list of all non-file node IDs to Gemini with a prompt: "Generate 10 keywords to find the requested component within the provided ID list. Only return the comma-separated keywords."
Output: keyword_list (from Gemini).
Embedding Generation	Process IDs & Queries	1. Collect All Component IDs: Extract all non-file node IDs from the nx.Graph.
2. Embed Queries: Generate an embedding for the original text_query and the keyword_list (either combine or embed separately). Store as query_embeddings.
3. Embed Nodes: Generate an embedding for each component node's ID and/or content (this structure is the nid_embed_struct). Store in a dictionary: component_embeddings = {component_id: embedding_vector}.
Similarity Search (SS)	Perform SS & Score	Loop: Iterate through all component_id in component_embeddings.
Calculate Score: For each component, calculate the similarity (e.g., cosine similarity) between its embedding and all query_embeddings.
Sum Results: Sum the similarity scores from all query embeddings to get a single final_score for the component.
Save: Store results in a dictionary: results = {component_id: final_score}.
Output	Rank & Return	Sort: Sort the results dictionary by final_score in descending order.
Return: Return the top 5 component_ids (the nid_embed_struct entries with the highest scores).


"""